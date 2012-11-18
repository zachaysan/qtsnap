import subprocess

for i in range(100):
    process_call = "python -m qt.crawlers.user"
    subprocess.call(process_call, shell=True)
