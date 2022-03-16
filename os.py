import os

a = r'''C:\Users\user\Desktop\Etiket ve Kılavuz\COSTUMER LABELS,USER MANUALS,WARANTY\U-Ü\UNIVERSAL - DABAN\PR-191021-AG'''
b = r'''\\10.0.0.5\3-kalite\Etiket ve Kılavuz'''

os.chdir(a)

# liste = ["Ocek", "Şubat", "Mart"]
# a = os.sep.join(liste)

c = os.listdir(a)

for i in c:
    print(os.path.lexists(i))



# a = os.getcwd()
# b = os.listdir(a)
# for i in b:
#     if i.endswith(".lnk"):
#         print(os.path.realpath(i))