import subprocess, sys
from pathlib import Path

base = sys.argv[1] if len(sys.argv) > 1 else 'HEAD~1'
r = subprocess.run(['git', 'diff', '--name-only', base, 'HEAD'],
                   capture_output=True, text=True)
if r.returncode != 0:
    print('tests'); sys.exit(0)  # cannot diff: run everything (safe fallback)
files = r.stdout.split()

src = {p.stem: p for p in Path('src').glob('*.py') if p.stem != '__init__'}
changed = {Path(f).stem for f in files if f.startswith('src/') and f.endswith('.py')}

grew = True
while grew:  # add modules that import a changed module
    grew = False
    for name, path in src.items():
        if name not in changed and any(f'src.{c}' in path.read_text() for c in changed):
            changed.add(name); grew = True

chosen = {str(t) for t in Path('tests').glob('test_*.py')
          if any(f'src.{c}' in t.read_text() for c in changed)}
chosen |= {f for f in files if f.startswith('tests/test_') and Path(f).exists()}
print(' '.join(sorted(chosen)) if chosen else 'tests')