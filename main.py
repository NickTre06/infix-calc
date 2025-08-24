import polz
from polz import check_brackets_balance
import math
from polz import parse_math_expression
from alg_polsk_zap import infix_to_rpn
from alg_counting import alg_count


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
         if not check_brackets_balance(linewithoutexecute):
            print("Ошибка! Неверная структура скобок.")
            continue
         
         tokens = parse_math_expression(linewithoutexecute)

         rpn = infix_to_rpn(tokens, variables)
         count =  alg_count(rpn, variables)
         print(count)


      
       



      

