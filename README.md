# AverageColor (v0.1) - A lightweight utility built from real-world data recovery needs.

AverageColor is a small Windows utility that renames image files by calculating their average RGB color and adding a numeric prefix to the filename.

This tool was created as a simple, local-first solution for organizing images — especially useful after data recovery when directory structures or filenames may be lost.

---

## ✨ What it does

- Drag image files onto the executable. (No installation required)
- Opens the image using Pillow (PIL)
- Converts the image to RGB
- Calculates the average color of all pixels
- Maps the color into a numeric bucket (00000–99999)
- Prefixes the filename with that value

before: apicure.jpg
after:  02973-apicture.jpg


⚠️ **Version 0.1 was tested primarily with JPG files.**  
Other formats are included in code but were not formally tested.

---

## 🔧 Build (v0.1)

Written in Python and packaged as a standalone Windows executable


---

## 🔒 Privacy

AverageColor works entirely locally.

- No cloud services
- No uploads
- No internet connection required

---

## 🧱 Design Philosophy

This project follows a simple KISS approach:

> Small tools that do one job well.

---

## 👤 Author

Lance Johnson  
Veteran IT technician and independent computer repair specialist.

