# ============================
# CONFIGURATION DU SYSTÈME
# ============================

CONFIG = {
    "f_ref_hz": 40e6,
    "modulus": 400,            # M pour F/M
    "cp_current": 0b1111,       # 5.12 mA (RSET typique)
    "r_counter": 1,            # f_ref en MHz → R = 10

    "band_select_div": 0x10,    # BS ~50kHz
    "ld_mode": 0b01,            # 01 = digital
    "mux_msb": 0,
    "mux_lsb": 0b110,

    "reg3_default": 0x00000013,  # CDM off, VCO auto
    "reg5_default": 0x00040000,  # valeur par défaut pour reg5
    "rf_power": {
        "APWR": 0b11, "BPWR": 0b11, "RFA_EN": 1, "RFB_EN": 1
    }
}

# ============================
# GÉNÉRATION DES REGISTRES SPI
# ============================

def reg0(int_n, N, F):
    return (int(int_n) << 31) | ((N & 0xFFFF) << 15) | ((F & 0xFFF) << 3) | 0b000

def reg1(M, CPOC=1, CPL=0b01, P=0):
    return (CPOC << 31) | ((CPL & 0x03) << 29) | ((P & 0xFFF) << 15) | ((M & 0xFFF) << 3) | 0b001

def reg2(R, CP, LDF=1, LDP=0, PDP=1, SHDN=0, TRI=0, RST=0, SDN=0b00, LDS=1, DBR=0, RDIV2=0):
    reg = 0
    reg |= (LDS & 0x1) << 31
    reg |= (SDN & 0x3) << 29
    reg |= CONFIG["mux_lsb"] << 26
    reg |= (DBR & 0x1) << 25
    reg |= (RDIV2 & 0x1) << 24
    reg |= (R & 0x3FF) << 14
    reg |= 1 << 13  # REG4DB
    reg |= (CP & 0xF) << 9
    reg |= (LDF & 0x1) << 8
    reg |= (LDP & 0x1) << 7
    reg |= (PDP & 0x1) << 6
    reg |= (SHDN & 0x1) << 5
    reg |= (TRI & 0x1) << 4
    reg |= (RST & 0x1) << 3
    reg |= 0b010
    return reg

def reg3():
    return CONFIG["reg3_default"]

def reg4(DIVA):
    pwr = CONFIG["rf_power"]
    reg = 0
    reg |= 0b011000 << 26
    reg |= 0 << 23  # FB
    reg |= (DIVA & 0x7) << 20
    reg |= (CONFIG["band_select_div"] & 0xFF) << 12
    reg |= 0 << 9  # BDIV
    reg |= (pwr["RFB_EN"] & 0x1) << 8
    reg |= (pwr["BPWR"] & 0x3) << 6
    reg |= (pwr["RFA_EN"] & 0x1) << 5
    reg |= (pwr["APWR"] & 0x3) << 3
    reg |= 0b100
    return reg

def reg5():
    return CONFIG["reg5_default"]

def reg_to_hex(reg):
    return f"{reg:08X}"

def choose_divider(f_out):
    if f_out < 46.875e6: return 0b111
    elif f_out < 93.75e6: return 0b110
    elif f_out < 187.5e6: return 0b101
    elif f_out < 375e6: return 0b100
    elif f_out < 750e6: return 0b011
    elif f_out < 1500e6: return 0b010
    elif f_out < 3000e6: return 0b001
    else: return 0b000

# ============================
# FONCTION PRINCIPALE
# ============================

def generate_spi_registers(f_out_hz, int_n=False):
    f_ref = CONFIG["f_ref_hz"]
    M = CONFIG["modulus"]
    CP = CONFIG["cp_current"]
    R = CONFIG["r_counter"]

    DIVA = choose_divider(f_out_hz)
    diva_factor = 2 ** DIVA
    f_vco = f_out_hz * diva_factor
    f_pfd = f_ref

    N_float = f_vco / f_pfd
    N = int(N_float)
    F = 0 if int_n else int(round((N_float - N) * M))

    print(f"[INFO] f_out = {f_out_hz/1e6:.3f} MHz | DIVA = {diva_factor} | fVCO = {f_vco/1e6:.3f} MHz")
    print(f"[INFO] Mode = {'Int-N' if int_n else 'Frac-N'} | N = {N} | F = {F} | M = {M} | R = {R}")

    regs = [
        reg0(int_n, N, F),
        reg1(M),
        reg2(R, CP, LDF=int(int_n)),
        reg3(),
        reg4(DIVA),
        reg5()
    ]

    return [reg_to_hex(r) for r in regs]

# ============================
# TEST
# ============================

if __name__ == "__main__":
    f_out_mhz = 5904.1
    regs = generate_spi_registers(f_out_hz=f_out_mhz * 1e6, int_n=False)
    for i, hexval in enumerate(regs):
        print(f"Reg{i}: {hexval}")
