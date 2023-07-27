import re

frase = input("Introduce una cadena para pasarla a lenguaje de HACKER 8): ")

frase = frase.lower()

frase = re.sub("a","4",frase)
frase = re.sub("b","I3",frase)
frase = re.sub("c","[",frase)
frase = re.sub("d","|)",frase)
frase = re.sub("e","3",frase)
frase = re.sub("f","|=",frase)
frase = re.sub("g","&",frase)
frase = re.sub("h","#",frase)
frase = re.sub("i","1",frase)
frase = re.sub("j",",_|",frase)
frase = re.sub("k","|<",frase)
frase = re.sub("l","1",frase)
frase = re.sub("m","|\/|",frase)
frase = re.sub("n","/\/",frase)
frase = re.sub("o","0",frase)
frase = re.sub("p","|*",frase)
frase = re.sub("q","(_,)",frase)
frase = re.sub("r","I2",frase)
frase = re.sub("s","5",frase)
frase = re.sub("t","7",frase)
frase = re.sub("u","(_)",frase)
frase = re.sub("v","\/",frase)
frase = re.sub("w","vv",frase)
frase = re.sub("x","><",frase)
frase = re.sub("y","Ч",frase)
frase = re.sub("z","2",frase)

print(frase)

# a="4"
# b="I3"
# c="["
# d="|)"
# e="3"
# f="|="
# g="&"
# h="#"
# i="1"
# j=",_|"
# k="|<"
# l="1"
# m="|\/|"
# n="/\/"
# o="0"
# p="|*"
# q="(_,)"
# r="I2"
# s="5"
# t="7"
# u="(_)"
# v="\/"
# w="vv"
# x="><"
# y="Ч"
# z="2"
