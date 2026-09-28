import subprocess

DETIK = 10

print(f"Laptop akan mati dalam {DETIK} detik.")
print("Batalkan dengan mengetik: shutdown /a")
subprocess.run(["shutdown", "/s", "/t", str(DETIK)])