from openai import OpenAI # นำเข้าOpenAIคลาสจากopenai เพื่อเข้าถึงโมเดลของ OpenAI API 
import os # นำเข้าosโมดูลซึ่งมีฟังก์ชันสำหรับการโต้ตอบกับระบบปฏิบัติการ

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY")) # สร้างอินสแตนซ์ของOpenAIคลาสและตั้งapi_keyค่าคุณสมบัติเป็นค่าที่ดึงมาจากตัวแปรสภาพแวดล้อมOPENAI_API_KEY หรือดึงมาจากไฟล์.env

def generate_response(user_input): # ฟังก์ชันนี้รจะรับอินพุตของผู้ใช้เป็นอาร์กิวเมนต์สตริง ( user_input) และสร้างข้อความตอบจากโมเดล AI
  """Generates a response from the AI based on the user's input."""
  completion = client.chat.completions.create(
      model="gpt-3.5-turbo", # โมเดลของ AI
      messages=[
          {"role": "user", "content": user_input}, # เป็นการกำหนดการสนทนาเป็นข้อความที่จะสร้างตาม "role" ที่เราตั้ง เช่น "user"
      ],
      temperature=0.5, # เป็นการกำหนดว่าจะให้ai มีการเติมเนื้อหามากน้อยเพียงใด
      max_tokens=128, # จำกัดคำที่Aiสร้าง
      top_p=1 # เป็นค่า parameter ที่มีมาให้เพื่อควบคุมการสุ่ม (random) สร้างข้อความขึ้นมา
  
  )

  return completion.choices[0].message # ฟังก์ชันส่งคืนข้อความที่สร้างโดยโมเดลซึ่งจัดเก็บไว้ในmessage คุณสมบัติขององค์ประกอบแรก([0])ในchoicesรายการที่ส่งคืนโดย API

def is_exit_command(user_input): # เป็นฟังก์ชันที่จะกำหนดข้อความเพื่อใช้ออกจากการแชท
  """Checks if the user input is an exit command."""
  return user_input.lower() in ["exit", "quit", "bye"] # กำหนดคำที่ใช้ในการออกจากแชท

# พิมพ์ข้อความให้ AI เริ่มทักทายประโยคแรก
print("AI: Hello!") 
while True: # เป็นการเริ่มต้นการวนซ้ำแบบไม่สิ้นสุดตราบใดที่ True ตรงตามเงื่อนไข
  # รับข้อความจากผู้ใช้
  user_input = input("User: ")

  # ตรวจสอบว่าข้อความเป็นคำสั่งออกโดยใช้ฟังก์ชัน is_exit_command หรือไม่
  if is_exit_command(user_input):
    break

  # ให้ AI สร้างข้อความ
  ai_response = generate_response(user_input)

  # พิมพ์ข้อความของ AI ด้วยคำนำหน้า "AI: "
  print("AI:", ai_response)
