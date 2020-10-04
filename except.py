
try:
    print x
except NameError:
    print "Variable x not defined"
except:
    print "Something unexpected happened..."
finally:
    print "Execution completed!"
