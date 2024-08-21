import sys
from pylint import lint
THRESHOLD = 9
run = lint.Run(["factorial1.py"],exit=False)
score = run.linter.stats.global_note
if score<THRESHOLD:
    print("Linter failed: score < THRESHOLD value")
    sys.exit(1)
sys.exit(0)