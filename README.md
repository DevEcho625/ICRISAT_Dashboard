ICRISAT Field Dashboard – Django + Leaflet
=========================================

This project is a web-based interactive field dashboard built for an
ICRISAT internship project. The website displays all agricultural fields
on the ICRISAT Hyderabad campus using a map, and allows users to click
on any field to view detailed field-level data sourced from a spreadsheet.

The backend is built using Django, and the frontend map uses Leaflet.js
with GeoJSON field boundaries.

--------------------------------------------------
FEATURES
--------------------------------------------------

- Interactive Leaflet map centered on the ICRISAT campus (Hyderabad)
- All campus fields displayed as polygons from a GeoJSON file
- Clickable fields that show field-specific data in a side panel
- Field data is dynamically loaded from an Excel spreadsheet
- Clean separation of backend (Django) and frontend (HTML + JS)

--------------------------------------------------
TECH STACK
--------------------------------------------------

Backend:
- Python 3
- Django
- Pandas (for Excel processing)

Frontend:
- HTML
- CSS
- JavaScript
- Leaflet.js
- OpenStreetMap tiles

Data:
- GeoJSON file for field boundaries
- Excel spreadsheet (FLDREQ2013.xlsx) for field metadata

--------------------------------------------------
PROJECT STRUCTURE (IMPORTANT)
--------------------------------------------------

maps/
│
├── map/                    ← Django project
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── dashboard/              ← Django app
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── dashboard/
│   │       └── map.html
│   ├── data/
│   │   ├── final.json      ← GeoJSON field polygons
│   │   └── FLDREQ2013.xlsx ← Spreadsheet with field data
│   └── ...
│
└── manage.py

--------------------------------------------------
HOW TO RUN THE WEBSITE
--------------------------------------------------

1. Make sure your virtual environment is activated (if you use one)

2. Navigate to the directory containing manage.py:

   Example:
   cd maps

3. Start the Django development server:

   python manage.py runserver

4. Open a browser and go to:

   http://127.0.0.1:8000/dashboard/

IMPORTANT:
Do NOT forget the trailing `/dashboard/` — this is where the map lives.

--------------------------------------------------
HOW THE MAP WORKS
--------------------------------------------------

- The map loads field boundaries from:
  
  /dashboard/fields/

  (served by Django as GeoJSON)

- Each polygon contains a field identifier from the GeoJSON property:
  
  Field_no_j

- When a polygon is clicked:
  - The field number is sent to:
    
    /dashboard/field-details/<FIELD_NO>/

  - Django looks up the matching row in the Excel spreadsheet
  - Field information is returned as JSON
  - The side panel (top-right) updates with field details

--------------------------------------------------
FIELD IDENTIFIERS (VERY IMPORTANT)
--------------------------------------------------

GeoJSON field identifier:
- Property name: Field_no_j

Excel field identifier:
- Column name: FIELDNO

These two values MUST MATCH for data to appear.

If a field exists on the map but shows:
"Error loading spreadsheet data"

Then the FIELDNO in the spreadsheet does NOT match
the Field_no_j value in the GeoJSON.

This is a data consistency issue, not a code bug.

--------------------------------------------------
DATA DISPLAYED PER FIELD
--------------------------------------------------

The following data is displayed when available:

- FIELDNO
- REQNO
- DATEPTD
- PLANTDATE
- HARVESTDAT
- ACTUALPDAT
- EXPDETAIL
- PESTNAME
- HERBNAME

--------------------------------------------------
COMMON ISSUES & TROUBLESHOOTING
--------------------------------------------------

1. 404 Error when opening the site
   ✔ Make sure you are visiting /dashboard/
   ✔ Ensure dashboard is included in map/urls.py

2. Fields appear but no data loads
   ✔ Check that Field_no_j matches FIELDNO exactly
   ✔ Check Excel file path:
     dashboard/data/FLDREQ2013.xlsx

3. Server crashes on startup
   ✔ Confirm pandas is installed:
     pip install pandas openpyxl

4. GeoJSON not loading
   ✔ Confirm final.json exists in:
     dashboard/data/final.json

--------------------------------------------------
DEVELOPMENT NOTES
--------------------------------------------------

- Excel data is loaded once at server startup for performance
- Field numbers may contain spaces and hyphens and are URL-encoded
- Leaflet automatically handles polygon projection
- Map auto-zooms to all loaded fields



--------------------------------------------------
AUTHOR / CONTEXT
--------------------------------------------------

Built as part of an internship-related project for ICRISAT,
focused on agricultural field visualization and data integration.

--------------------------------------------------
END OF README
--------------------------------------------------
