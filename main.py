from datetime import datetime

from pip import main
import test_div
from ro_pollard_method import floyd as ro_pollard_method
import solovey_stassen_test
import brilhart_morrison
from algorythm import algorythm

    
def main():
    variant = [17807879769] #додати значення треба !!!
    
    pol = [9172639163, 8627969789, 8937716743, 278874899, 99400891, 116381389, 4252083239, 6633776623, 227349247, 3568572617]
    for i in pol:
        start_time = datetime.now()
        print('Дільник числа ', pol[i], ' : ', ro_pollard_method(pol[i]))
        print('Час роботи алгоритму факторизації Ро-метод Полларда для числа ', i, ' складає: ', datetime.now() - start_time, 'c')
    for i in pol:
        start_time = datetime.now()
        print('Дільник числа ', pol[i], ' : ', brilhart_morrison(pol[i]))
         print('Час роботи алгоритму факторизації Брілхарта-Морісона для числа ', i, ' складає: ', datetime.now() - start_time, 'c')
    
    
    
if __name__ == '__main__':
    main()