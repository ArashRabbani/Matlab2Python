def Main():
        # 1
    z=calc_sum(3,5)
    print(z)
    # 2
    z=calc_sum2(3)
    print(z)
    # 3
    [z1,z2]=calc_sum_prod(3,5)
    print(z1,z2)
    # 4
    [z1,z2]=calc_sum_prod_nested(3,5)
    print(z1,z2)

# 1
def calc_sum(x,y):
    z=x+y;
    return z

# 2
def calc_sum2(x,y=5):
    z=x+y;
    return z

# 3
def calc_sum_prod(x,y):
    z1=x+y;
    z2=x*y;
    return z1,z2

# 4
def calc_sum_prod_nested(x,y):

    def calc_sum_nested(x,y):
        return x+y
    
    def calc_prod_nested(x,y):
        return x*y
    
    z1=calc_sum_nested(x,y)
    z2=calc_prod_nested(x,y)
    return z1,z2

Main()
        