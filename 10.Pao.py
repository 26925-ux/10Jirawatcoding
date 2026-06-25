print("\nโปรแกรมคำนวณค่าBMI")

weight = int(input("\nกรุณากรอกน้ำหนักของคุณ (กิโลกรัม): "))
height = int(input("กรุณากรอกส่วนสูงของคุณ (เซนติเมตร): "))

BMI = weight / ((height / 100) ** 2)

print("\nค่าBMI ของคุณคือ: ", BMI)

if BMI < 18.5:
    print("คุณมีน้ำหนักน้อย ")

elif BMI >= 18.5 and BMI < 25:
    print("คุณมีน้ำหนักปกติ ")

elif BMI >= 25 and BMI < 30:
    print("คุณมีน้ำหนักเกิน")

else:
    print("คุณอ้วนมาก")
