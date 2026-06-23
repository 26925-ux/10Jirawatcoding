print("โปรแกรมช่วยคำนวณคะแนนรวม")

English = int(input("กรอกคะแนนวิชาภาษาอังกฤษ: "))

Math = int(input("กรอกคะแนนวิชาคณิตศาสตร์: "))

Computer = int(input("กรอกคะแนนวิชาวิทยาการคำนวณ: "))

total_point =  English + Math + Computer 

print("คะแนนรวมของคุณคือ:", total_point)

if total_point >= 80 :
    print("ระดับคะแนน: ดีเยี่ยม")

elif total_point >= 60 :
    print("ระดับคะแนน: ผ่าน")

else:
    print("ระดับคะแนน: ควรปรับปรุง")