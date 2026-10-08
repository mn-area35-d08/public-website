# Validate all TOML files without modifying them.
uv run --no-project python -c "import pathlib, tomllib; files = sorted(pathlib.Path('updates').rglob('*.toml')); [tomllib.loads(p.read_text(encoding='utf-8')) for p in files]; print(f'Validated {len(files)} TOML files.')"

# Generate the website HTML locally.
uv run --no-project python _build/build.py
