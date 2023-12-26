import cowsay
import sys

if len(sys.argv) != 2:
    sys.exit
    cowsay.tux("hello, " + sys.argv[1])
