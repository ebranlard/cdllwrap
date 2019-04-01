ifeq ($(OS),Windows_NT)
	OS=Windows
	LIBEXT='.dll'
	EXEEXT='.exe'
else
    OS=$(shell uname -s)
    ifeq ($(OS),Linux)
	LIBEXT='.so'
	LIBPRE='lib'
    else ifeq ($(OS),Darwin)
	LIBEXT='.dylib'
    endif
endif
LIB_FILE=$(LIBPRE)testlib$(LIBEXT)
LIB_HDR =$(LIBPRE)testlib.h

all: test

test:
	@echo "------------------------------------------------------------"
	python test_wraplib.py $(LIB_FILE) $(LIB_HDR)
	@echo "------------------------------------------------------------"
