Absolutely! Here's a **detailed README** for your City Info app with weather and Google Maps landmarks integration. I’ve structured it so that someone can set up, run, and understand the project easily.

---

# City Info Finder

A web app that allows users to search for a city and view:

* Current weather conditions (using **OpenWeather API**)
* Nearby landmarks/places of interest (using **Google Maps Places API**)
* Interactive map with markers for landmarks
* Slider/gallery view of landmarks with images

Built using **Python (Flask)** and **Leaflet.js**.

---

## Features

1. **City Weather**: Shows temperature, weather description, and other details for any city worldwide.
2. **Nearby Landmarks**: Fetches top landmarks using Google Maps Places API and displays them on a map.
3. **Interactive Map**: Clickable markers show landmark names.
4. **Landmark Slider**: Users can view landmark images in a horizontal scrollable slider.
5. **Responsive UI**: Works on desktop and mobile.

---

## Tech Stack

* **Backend**: Python, Flask
* **Frontend**: HTML, CSS, JavaScript, Leaflet.js
* **APIs**:

  * OpenWeatherMap API (Weather Data)
  * Google Maps Places API (Landmarks)

---

## Requirements

* Python 3.10+
* pip
* Internet connection

### Python Packages

```bash
pip install flask requests python-dotenv
```

---

## Setup

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd City-Info-Finder
```

2. **Set API keys**:

You can use the provided batch script to set your API keys:

```bat
setup_keys.bat
```

It will ask for:

* **OpenWeather API Key**
* **Google Maps Places API Key**

The keys will be stored in a `.env` file.

3. **Verify .env**:

After running the script, your `.env` file should look like:

```env
OPENWEATHER_KEY=your_openweather_api_key_here
GOOGLE_API_KEY=your_google_maps_api_key_here
```

---

## Run the App

```bash
python det.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## File Structure

```
City-Info-Finder/
│
├── det.py                # Flask backend
├── templates/
│   └── index.html        # Frontend HTML
├── static/               # Optional CSS/JS/images
├── .env                  # Environment variables for API keys
├── setup_keys.bat        # Batch script to set API keys
└── README.md             # This file
```

---

## Frontend Interaction

1. Enter a city in the search bar.
2. Click **Search**.
3. The weather is displayed on the top.
4. Landmarks appear on the map as markers.
5. Scroll through the landmark slider to view images.

---

## Notes

* Google Maps Places API requires a **valid billing account** for full access. Ensure your API key has the Places API enabled.
* If landmarks images are missing, some places may not have photos available.
* The app currently shows top 10 landmarks within ~3 km radius of the city center.

---

## Future Improvements

* Add **autocomplete city search**.
* Show **weather forecast** for next 7 days.
* Add **categories for landmarks** (restaurants, museums, parks, etc.).
* Improve UI with **Material Design / Tailwind CSS**.
* Enable **dark mode**.

---

## License

MIT License
© 2025 Your Name

---

If you want, I can also **write a version of the README with screenshots and a live slider demo layout**, which will make it look professional like a GitHub project page.

Do you want me to do that next?
