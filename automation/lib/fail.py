import sys
def fail(msg:str,code:int=1)->None:
    print(f"ERROR: {msg}")
    sys.exit(code)
