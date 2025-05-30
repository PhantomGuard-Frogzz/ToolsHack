import time
import random

def generate_otp():
    return random.randint(11111, 999999)

def kirim_otp(nomor):
    otp = generate_otp()
    print(f"[+] OTP Terkirim ke {nomor}: {otp}")
    

def main():
    print("=== Sistem Kirim OTP Via SMS===")
    nomor = input("Masukkan Nomor Target: ")
    max_kirim = 30
    delay_per_kirim = 1

    for i in range(max_kirim):
        kirim_otp(nomor)
        time.sleep(delay_per_kirim)

    print(f"[-] Selesai kirim {max_kirim} OTP ke {nomor}")

if __name__ == "__main__":
    main()