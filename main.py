import polz
from polz import check_brackets_balance
import math
#CONSTANTS = {"M_PI": math.pi, "M_E": math.e}
from polz import parse_math_expression
from alg_polsk_zap import infix_to_rpn

#print.print_array("DEFINE: A=5;"+
                #  "DEFINE: B=6; "+
                #  "EXECUTE: A+B;")
#print.print_array(polz.parse_math_expression("31+5*(7^2)"))


#Тестируем функцию
#for idx, element in polz.parse_math_expression(" A7 + 31 + 22225 *(7^2)"):
#   print(f"{idx}: {element}")
variables = {}
tokens = []

with open("./input.txt", 'r', encoding='UTF-8') as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
      linewithoutspace = line.replace(' ', '')
      if "DEFINE:" in linewithoutspace:
         print ('Start to handle DEFINE')
         linewithoutdefine = linewithoutspace.replace('DEFINE:', '')
         delimeter_index = linewithoutdefine.find('=') 
         name_variables = linewithoutdefine[:delimeter_index]
         if name_variables == ("M_PI" or "M_E"):
            break
         value_variable = linewithoutdefine[delimeter_index+1:]
         variables[name_variables] = value_variable
         print ('Parsed next define:  {' + name_variables + ' : ' + value_variable + '}')

      if "EXECUTE:" in linewithoutspace:
         print ('This string is EXECUTE')
         linewithoutexecute = linewithoutspace.replace('EXECUTE:', '')
         if linewithoutexecute.find('M_PI'):
            linewithoutexecute = linewithoutexecute.replace('M_PI','3.14')
         if linewithoutexecute.find('M_E'):
            linewithoutexecute = linewithoutexecute.replace('M_E','2.72')
         if not check_brackets_balance(linewithoutexecute):
            print("Ошибка! Неверная структура скобок.")
            continue
         
         tokens = parse_math_expression(linewithoutexecute)

         rpn = infix_to_rpn(tokens)
         print(rpn)


      
       



      

