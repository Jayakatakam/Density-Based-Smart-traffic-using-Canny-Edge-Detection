# 🚦 Density Based Smart Traffic Control System  

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Smart%20City-blue?style=for-the-badge&logo=googlemaps">
  <img src="https://img.shields.io/badge/Technology-Image%20Processing-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OpenCV-Used-blue">
  <img src="https://img.shields.io/badge/Smart%20Traffic-Automation-orange">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey">
</p>

---

## 🌐 Project Overview  

Traffic congestion is a major problem in urban areas. Traditional traffic signal systems operate on **fixed-time intervals**, which do not adapt to real-time traffic conditions. This results in unnecessary waiting times, fuel wastage, and increased pollution.

The **Density Based Smart Traffic Control System** is designed to overcome these limitations by **dynamically controlling traffic signal timings** based on the **actual vehicle density on the road** using **image processing techniques**.

---

## 🧠 Core Idea (In Simple Words)

> 💡 *More traffic → more green signal time.*

Instead of using fixed timers:
- The system captures traffic images at road junctions
- Detects vehicle density using **Canny Edge Detection**
- Calculates traffic density by counting pixels
- Allocates green signal time dynamically

✅ High-density roads get more green time  
✅ Low-density roads get less green time  
✅ Traffic flow becomes smoother and faster  

---

## ❌ Problems with Traditional Traffic Systems  

- Fixed signal timings regardless of traffic
- Long waiting times even when roads are empty
- Poor utilization of road infrastructure
- Increased fuel consumption and pollution

---

## ✅ Proposed Solution  

This project introduces an **intelligent traffic signal control system** that:
- Uses cameras instead of manual control
- Detects real-time traffic density
- Automatically adjusts signal timings
- Reduces congestion and waiting time

---

## 🏗️ System Architecture  

The system consists of the following components:

### 📷 Camera Input  
- Captures live or static traffic images

### 🧠 Image Processing Module  
- Converts images to grayscale  
- Applies noise reduction  
- Uses **Canny Edge Detection** to detect vehicles  

### 📊 Density Calculation Module  
- Counts non-zero (edge) pixels  
- Compares with a reference image  
- Determines traffic density level  

### 🚦 Signal Control Module  
- Allocates green signal time based on density  
- Higher density → longer green time  

---

## 🔄 Working Flow  

1️⃣ Capture traffic image  
2️⃣ Preprocess image (grayscale, filtering)  
3️⃣ Detect edges using Canny algorithm  
4️⃣ Count pixels representing vehicles  
5️⃣ Calculate traffic density  
6️⃣ Decide green signal time  
7️⃣ Display output results  

---

## 🛠️ Technologies Used  

| Category | Technology |
|-------|------------|
| Programming Language | Python |
| Image Processing | OpenCV |
| Numerical Computing | NumPy |
| GUI | Tkinter |
| Visualization | Matplotlib |
| Development Tools | GitHub |

---

## 🧪 Key Features  

✅ Real-time traffic density detection  
✅ Dynamic signal timing control  
✅ Reduced traffic congestion  
✅ Efficient road usage  
✅ Smart city–oriented solution  
✅ Easy to extend to real-time video  

---

## 🌍 Real-World Applications  

🚥 Smart City Traffic Management  
🚑 Emergency Vehicle Priority Systems  
🛣️ Urban Road Infrastructure Planning  
🌱 Pollution and Fuel Consumption Reduction  
🚗 Intelligent Transportation Systems (ITS)  

---

## ▶️ How to Run the Project  

### Prerequisites  
- Python 3.x  
- Required libraries installed  

### Installation  
```bash
pip install -r requirements.txt
Run

python src/main.py


---

📊 Results & Output

Edge-detected images highlighting vehicles

Traffic density percentage

Dynamic green signal timings based on density


📌 This leads to reduced waiting time and smoother traffic flow.


---

🚀 Future Enhancements

✨ Real-time video processing
✨ AI-based vehicle counting
✨ Emergency vehicle detection
✨ IoT-based signal integration
✨ Cloud-based traffic monitoring
✨ Deep learning for higher accuracy


---

🎯 One-Line Summary

> An intelligent traffic control system that dynamically adjusts signal timings based on real-time traffic density using image processing.




---

📌 Learning Outcomes

Understanding image processing techniques

Hands-on experience with OpenCV

Traffic analysis using computer vision

System design for smart city solutions

Practical problem-solving skills



---
🤝 Connect with Me 📬 Email: kamjaya1703@gmail.com 💼 LinkedIn: https://www.linkedin.com/in/jaya-lakshmi-katakam-b40258299

🔗 GitHub: https://github.com/Jayakatakam

🌐 Portfolio: https://portfolio-jaya.lovable.app/ 🧠 “Technology isn’t just about building tools — it’s about building futures.”
⭐ If you like this project, give it a star!

---
