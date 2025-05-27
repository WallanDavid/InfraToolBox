# monitor_cpu_memoria.py
# Monitora uso de CPU e Memória no sistema

import psutil

cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory()

print(f"Uso de CPU: {cpu}%")
print(f"Uso de Memória: {mem.percent}%")
