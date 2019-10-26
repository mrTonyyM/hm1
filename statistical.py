def abs_average(vector):
    a_vector = 0
    l_vector = len(vector)
    for i in range(l_vector):
        a_vector = a_vector+abs(vector[i])/l_vector
    return a_vector

def err(vector,index):
    e_vector = vector[index] - abs_average(vector)
    return e_vector

def disp (vector):
    l_vector = len(vector)
    d_vector = 0
    for i in range(l_vector):
        e_vector = err(vector,i)
        d_vector = d_vector + e_vector*e_vector/(l_vector-1)
    return d_vector

def cov (vector1,vector2):
    cov_vector = 0
    l_vector = len(vector1) # todo сделать исключение для случая, когда длина вектора не равна длине вектора2
    for i in range(l_vector):
        cov_vector = cov_vector + err(vector1,i)*err(vector2,i)/(l_vector-1)
    return cov_vector

def r_coef (vector1,vector2):
    r_coef = cov(vector1,vector2)/pow(disp(vector1)*disp(vector2),0.5)
    return r_coef

