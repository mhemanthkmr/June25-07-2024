
try:
        a =0
        b = 5
        print(b/a)
except Exception as err:
        print("error occured", err)
else:
        print("done")
finally:
        print("executed successfully")