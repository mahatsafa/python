import subprocess
import time

DETIK = 5

print(f"Laptop akan sleep dalam {DETIK} detik. Tekan Ctrl+C untuk membatalkan.")
try:
    time.sleep(DETIK)
except KeyboardInterrupt:
    print("Dibatalkan.")
else:
    subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"])