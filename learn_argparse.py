"""
Learnings:
-argparse is used to add arguments/parameters to a python script execution
-the arguments can then be used in the script
-there are mandatory positional arguments (without leading -/--) and optional arguments (with leading -/--)
-by default the arguments are assumed to be strings, hence the type parameters is needed to identify them when they're something else
-for positional arguments the order does matter, but not for optional arguments (you can put the flag anywhere in the command)

-try the following commands:
python learn_argparse.py -h
python learn_argparse.py useless 8
python learn_argparse.py useless 8 -v
python learn_argparse.py useless -v 8
"""

import argparse

parser = argparse.ArgumentParser()
# the order of the arguments needs to be mirrored in the command
parser.add_argument("echo", help="just a test")
parser.add_argument("square", help="display a square of a given number", type=int)
# the leading -/-- make the argument optional
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
answer = args.square**2

if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)