MATH        = 1-math
STRING      = 2-string
RANDOM      = 3-random
MEOW        = 4-meow
RETURN2FLAG = 5-return2flag
ECHOOO      = 6-echooo

all:
	cd $(RANDOM) && make
	chmod +x $(MATH)/*.py $(STRING)/*.py $(STRING)/*.sh $(RANDOM)/*.py \
		$(MEOW)/*.py $(MEOW)/*.sh $(RETURN2FLAG)/*.py $(ECHOOO)/*.py

clean:
	cd $(RANDOM) && make clean
