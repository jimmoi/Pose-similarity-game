สร้าง folder  "im ref pose" สำหรับเก็บ image reference pose  

แบ่งเป็น 2 ส่วน
1. ส่วนไว้ get ค่า pose reference
	1.1 ดึงรูปจาก im ref pose
	1.2 get ค่า (x,y) จาก pose reference ใช้ mediapipe
	1.3 เก็บข้อมูลที่ ไว้ที่ ตัวแปร ref_pose_data
2.แสดงภาพ
	2.2 ทำ CV video cap และ insert ref pose 
	2.3 insert im ref และ im show โดยใช้ร่วม กับ mediapipe
	2.4 ทำการเปรียบเทียบ video cap และ im ref โดยให้อยู่ในรูป % ไม่ก็ percent strip
	2.5 ถ้าpercentมากกว่า 95 % ขึ้นเป็นตัวอักษรสีเขียว74
	




นำ image_ref ทำ pose landmark
นำ webcam ทำ pose landmark
show pose_ref and webcam by imshow
score calculate by math equation
show score overlay on imshow