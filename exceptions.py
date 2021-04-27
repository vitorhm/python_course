# Try block with except, else and finally
try:
    print("try block")
except NameError:
    print("NameError Exception")
except:
    print("catch all")
else:
    print("else block")
finally:
    print("finally block")