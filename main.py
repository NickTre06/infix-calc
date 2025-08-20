import polz
import print

print.print_array("DEFINE: A=5;"+
                  "DEFINE: B=6; "+
                  "EXECUTE: A+B;")
print.print_array(polz.parse_math_expression("31+5*(7^2)"))


#Тестируем функцию
#for idx, element in polz.parse_math_expression("31+5*(7^2)"):
#    print.print_array(f"{idx}: {element}")

#for idx, element in polz.parse_math_expression("31+5"):
#    print(f"{idx}: {element}")