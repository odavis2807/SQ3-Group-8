import sys
import glob
from pylint.lint import Run

THRESHOLD = 9

# Collect all .py files in your project, but skip virtual environment
python_files = [
    f for f in glob.glob("../SQ3-GROUP-8/**/*.py", recursive=True)
    if "sq3env" not in f and "__pycache__" not in f and "site-packages" not in f
]

if not python_files:
    print("No Python files found!")
    sys.exit(0)

print(f"Found {len(python_files)} Python files to lint.\n")

run = Run(python_files)
score = run.linter.stats.get("global_note", 0)

if score < THRESHOLD:
    print(f"\n❌ Linter failed: Score {score:.2f}/10 < threshold ({THRESHOLD})")
    sys.exit(1)

print(f"\n✅ Linter passed! Global score: {score:.2f}/10")
sys.exit(0)
