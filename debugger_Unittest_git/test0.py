from prime import is_prime

def test_prime(n,expected):
  if is_prime(n) != expected :
    print(f"ERROR on is_prime{n}, expected {expected}")

"""    
test_prime(1,False)
test_prime(2,True)
test_prime(8,False)
test_prime(11,True)
test_prime(25,False)
test_prime(28,False)
"""



# Create a test0.sh and chmod +x test0.sh and ./test0.sh to run all the test
#python3 -c "from test0 import test_prime; test_prime(1,False)"
#python3 -c "from test0 import test_prime; test_prime(2,True)"
#python3 -c "from test0 import test_prime; test_prime(8,False)"
#python3 -c "from test0 import test_prime; test_prime(11,True)"
#python3 -c "from test0 import test_prime; test_prime(25,False)"
#python3 -c "from test0 import test_prime; test_prime(28,False)"
