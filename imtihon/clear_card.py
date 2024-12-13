import json
import re
def clear_kart():

    a=input("Karta qo'shish uchun 1 yoki O'chirish uchun 2 bosing: ")
    if a=='1':
        karts = {}
        with open("Bank_karta.json","r") as file:
            karts=json.load(file)
            while True:
                Karta_raqami = input("Plastik karta raqamingizni kiriting (XXXX XXXX XXXX XXXX formatida): ")
                if re.match(r"(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)",Karta_raqami):
                    break
                else:
                    print("Plastik karta raqami noto'g'ri! Iltimos, 4569403961014710 formatida kiriting.")
            while True:
                Ismi = input("Ismingizni kiriting (Bosh harf katta bo'lishi kerak): ")
                if re.match(r"^[A-Z][a-zA-Z]*$", Ismi):
                    break
                else:
                    print("Ism noto'g'ri! Iltimos, bosh harfi katta bo'lgan ism kiriting.")
            while True:
                Muddati = input("Muddatini kiriting ( XX/XX tartibida bo'lishi kerak): ")
                if re.match(r"^(0[1-9]|1[0-2])/([0-9]{2})$", Muddati):
                    break
                else:
                    print("Ism noto'g'ri! Iltimos, 12/25, 00/20, 10/20 formatda kiriting.")
            while True:
                Password = input("Parolingizni kiriting ( XXXX shu tartibda bo'lishi kerak): ")
                if re.match(r"^\d{4}$", Password):
                    break
                else:
                    print("Parol noto'g'ri! Iltimos, 0000, 1234, formatida kiriting.")

            while True:
                Balans= input("Balansingizni kiriting (1000, 10,000, 1,000.50 formatida): ")
                if re.match(r"^\d{1,3}(,\d{3})*(\.\d{2})?$", Balans):
                    break
                else:
                    print("Balans noto'g'ri! Iltimos, 1000, 10,000, 500.00 formatida kiriting.")

        karts[Karta_raqami]={
            'Karta_raqami': Karta_raqami,
            'Ismi': Ismi,
            'Muddati': Muddati,
            'Password': Password,
            'Balans': Balans
        }
        with open("Bank_karta.json","w") as file:
            json.dump(karts,file,indent=4)

    elif a=='2':
        with open('Bank_karta.json','r') as file:
            karts=json.load(file)
        Karta_raqami=input("O'chirish uchun karta raqamini kiriting: ")
        if Karta_raqami in karts:
            del karts[Karta_raqami]
            print("Karta o'chirildi")
        else:
            print("Bu raqamli karta topilmadi.")

        with open('Bank_karta.json','w') as file:
            json.dump(karts,file,indent=4)


clear_kart()
