CONTIKI_PROJECT = xxx
all: $(CONTIKI_PROJECT)
CONTIKI=xxx

MAKE_MAC = xxx
MAKE_NET = xxx
MAKE_ROUTING = xxx

MODULES += xxx

include $(CONTIKI)/Makefile.include
include $(CONTIKI/Makefile.identify-target)
