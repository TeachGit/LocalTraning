def celsius(T):
    return (5.0 / 9.0) * (T - 32.0)


f_temp = [0, 10, 20, 30, 40, 50]
c_temp = map(celsius, f_temp)
print(list(c_temp))