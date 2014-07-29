import lggr

LOGGING = lggr.Lggr()
CONSOLE = lggr.Printer()
LOGGING.add(LOGGING.INFO, CONSOLE)

