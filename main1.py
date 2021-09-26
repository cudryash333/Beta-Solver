import time
import matplotlib.pyplot as plt
import numpy as np

overflow = 1
timeout = False


def derivative(array):
    arr_size = len(array)
    new_arr = []
    for id, element in enumerate(array[:-1]):
        new_arr.append(element*(arr_size-id-1))
    return new_arr


def solve(x, array, debug=False):
    arr_size = len(array)
    result = 0
    for id, element in enumerate(array):
        if debug:
            print(result, element)
        result += element*x**(arr_size-id-1)
    return result


def divide_arr(big, small):
    big_num = len(big)
    small_num = len(small)
    ret_arr = []
    for id, element in enumerate(big):
        tmp_div = element / small[0]
        if id != big_num-1:
            big[id+1] -= tmp_div * small[1]
        ret_arr.append(tmp_div)
    return ret_arr


def newton_c(x_0, array, debug=False):
    x_n = x_0
    der_arr = derivative(array)
    t0 = time.process_time()
    while True:
        try:
            x_n = x_n - solve(x_n, array)/solve(x_n, der_arr)
        except:
            x_n += 0.1
            continue
        if debug:
            print(round(x_n, 4))
        if round(solve(x_n, array).real, 8) + round(solve(x_n, array).imag, 8)*1j == 0j:
            break
        global overflow
        if time.process_time() - t0 > overflow:
            global timeout
            timeout = True
            break
    return round(x_n.real, 4) + round(x_n.imag, 4)*1j


# ax^2+bx+c = [a , b , c]
# ax^3+bx^2+cx+d = [a , b , c , d]
# ax^n + bx^n-1 + cx^n ... = [a , b , c ...]
# You must put 0's if there is not ax^z ex:
# ax^3 + bx + c = [a , 0 , b , c]

a = input()
coeff = a.split(sep=None, maxsplit=-1)
my_arr = [int(item) for item in coeff]
print("Eqaution:")
eq = ""
for i in range(len(my_arr)-1):
    if my_arr[i] != 0:
        if my_arr[i] != 1:
            eq += str(my_arr[i])
        eq += "x"
        if len(my_arr)-i-1 != 1:
            eq += "^" + str(len(my_arr)-i-1)
        eq += "+"

eq += str(my_arr[len(my_arr) - 1]) + "=0"
print(eq)
print("Derivative's coefficients: ", derivative(my_arr))

x_n = -2j

second_arr = my_arr[:]

while True:
    print("----")
    if len(second_arr) == 1 or len(second_arr) < 1:
        break
    result = newton_c(x_n, second_arr, False)
    if timeout:
        print("Process stopped for running too long.")
        break
    if result.imag == 0:
        result = result.real
    print(result)
    second_arr = divide_arr(second_arr, [1, -1*result])[:-1]
print("All roots have been shown!")

x = np.linspace(-5, 5, 40)
y = 0
for i in range(len(my_arr)):
    y += my_arr[i] * x**(len(my_arr)-i-1)

plt.plot(x, y, color="red", label="Линия 1")
plt.grid()
plt.show()
