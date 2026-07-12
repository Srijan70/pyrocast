from pptx import Presentation

def main():
    prs = Presentation("new-ppt-dw.pptx")

    # Slide 3: METHODOLOGY PROPOSED (Shape 1)
    prs.slides[2].shapes[1].text_frame.text = (
        "Overview: A real-time, purely client-side wildfire spread simulator and impact dashboard. It uses a lightweight cellular-automata-style spread model based on Rothermel principles, running entirely in the browser over a MapLibre dark map.\n"
        "How it resolves the problem: It fetches live data (NASA FIRMS, OpenWeatherMap, Open-Elevation) directly in the browser. Given an ignition point, it applies a Rothermel-inspired formula combining fuel, wind, dryness, and slope to instantly forecast fire growth (+3h / +6h / +12h).\n"
        "Innovative features: No backend required. It runs fast locally, degrading gracefully to synthetic data if APIs fail. It forecasts burn area, population impact, and road intersections in real-time, making it an accessible, zero-infrastructure solution."
    )

    # Slide 4: TECHNICAL APPROACH (Shape 1)
    prs.slides[3].shapes[1].text_frame.text = (
        "Architecture: A 100% client-side Web Application built with Vite, React, and TypeScript. A data ingestion layer fetches live active fires (NASA FIRMS / VIIRS), current weather conditions (OpenWeatherMap), and terrain/slope (Open-Elevation) directly to the browser. Visualized using MapLibre.\n"
        "Core algorithms: spread.ts implements a lightweight, Rothermel-inspired estimator. Rate of spread is calculated from fuel, wind, dryness, and slope. The front geometry uses an anisotropic (elliptical) model, elongated downwind and uphill, sampled on a grid with stochastic boundary jitter. Byram flame length is computed from fireline intensity.\n"
        "Workflow & validation: Data sources are isolated behind clean function signatures, allowing easy backend swapping later. The model prioritizes being directionally correct, explainable, and lightning fast."
    )

    # Slide 5: FINAL REFLECTIONS AND FUTURE STEPS (Shape 2)
    prs.slides[4].shapes[2].text_frame.text = (
        "Tools, platforms, and what comes next:\n"
        "Software tools & frameworks: TypeScript, React, Vite, Tailwind CSS, MapLibre GL JS.\n"
        "Hardware: None required -- runs entirely on standard laptops or mobile browsers, no servers or specialized equipment needed.\n"
        "Development & deployment: Built locally; deployable as a static site on any cloud platform (Vercel, GitHub Pages) without backend maintenance.\n"
        "Languages: TypeScript / JavaScript for both the simulation engine and the live map visualization.\n"
        "Future steps: Integrate a real backend for heavy computations, add more sophisticated fuel mapping, and incorporate real-time mobile push alerts for at-risk communities."
    )

    # Slide 6: EXPECTED DELIVERABLE (Shape 0)
    prs.slides[5].shapes[0].text_frame.text = (
        "World View: A high-performance, dark-mode global map interface. Aggregates and visualizes live NASA FIRMS active fire detections, pulsing fire fronts, amber high-risk markers, and features a collapsible watch-location panel.\n"
        "Region View (Simulation Engine): A three-zone layout allowing users to adjust scenario controls (wind, fuel, moisture). Features a heatmap with a forecast timeline scrubber (+3h / +6h / +12h), and an interactive impact panel detailing burn area and population risk.\n"
        "Active Threat & Warning Matrix: Live impact assessment that instantly generates estimated burn area (acres), counts people in the path (using regional population density), and checks mocked road-intersections structured for real OSM data."
    )

    # Slide 7: EXPECTED DELIVERABLE (Shape 0)
    prs.slides[6].shapes[0].text_frame.text = (
        "Interactive Real-Time Dashboard (Deployment):\n"
        "A fully functional, open-source web application that can be used immediately by disaster management teams and the general public without installation or GIS training.\n\n"
        "Documentation & Source Code:\n"
        "Clean, documented TypeScript codebase with isolated data fetching modules, allowing future developers to easily swap in proprietary backends or more complex models."
    )

    # Slide 9: REFERENCES (Shape 0)
    prs.slides[8].shapes[0].text_frame.text = (
        "Sources referenced for this project:\n"
        "Fire Spread Modeling: Rothermel's surface fire spread model and Byram's fireline intensity equations.\n"
        "Data APIs: NASA FIRMS active fire data (VIIRS), OpenWeatherMap API for live wind/humidity, Open-Elevation API for terrain and slope data.\n"
        "Libraries & Frameworks: React, MapLibre GL JS documentation, Vite and TypeScript manuals.\n"
        "Industry benchmark: Directionally inspired by FARSITE, adapted for lightweight, instant browser-based execution."
    )

    prs.save("PyroCast-Final-Presentation.pptx")
    print("Updated presentation saved to PyroCast-Final-Presentation.pptx")

if __name__ == "__main__":
    main()
