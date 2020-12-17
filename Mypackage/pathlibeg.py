from pathlib import Path

p = Path()
for file in p.glob('*.*'):
    print(file)

