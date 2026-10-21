# Səbəb: input() funksiyası məlumatı həmişə 'str' (mətn) tipində alır. 
# Mətnlə rəqəmi birbaşa toplamaq və ya birləşdirmək mümkün olmadığı üçün 
# age dəyişənini int() vasitəsilə rəqəmə çevirməliyik.

age = int(input("Yaşınız: "))

# Düzgün versiya:
print(f"5 ildən sonra {age + 5} yaşınız olacaq")