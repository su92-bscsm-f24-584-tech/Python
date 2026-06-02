Here’s a concise **installation and run instruction** for your project:

---

## **TOUR Region Info – Quick Setup Guide**

### **1. Requirements**

* Python 3.10+
* Pip (Python package manager)
* Google Maps API key
* OpenWeatherMap API key

---

### **2. Install Python Dependencies**

Open a terminal or PowerShell in your project folder:

```bash
pip install flask python-dotenv requests
```

---

### **3. Set API Keys**

Run the batch script you created to set API keys in `.env`:

```bash
setup_keys.bat
```

It will ask you for:

* **OpenWeather API key**
* **Google Maps API key**

> These keys will be saved in `.env` automatically.

---

### **4. Run the Flask App**

In the same terminal:

```bash
python det.py
```

* You will see:

  ```
  * Running on http://127.0.0.1:5000
  ```
* Open this link in your browser.

---

### **5. How to Use**

1. Enter a city name in the left sidebar.
2. Click **Search**.
3. Weather info will appear in the center.
4. Landmark images appear in the left slider.
5. Click **See More** to expand weather details.
6. Map shows all landmarks with markers.

---

### **6. Notes**

* Make sure your Google Maps API key has **Places API enabled**.
* Make sure your OpenWeatherMap API key is valid.
* Sidebar and slider are scrollable if there are many landmarks.

---

If you want, I can also **write this in a ready-to-copy README.md file** with proper markdown formatting and badges.

Do you want me to do that?
