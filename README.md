## Overview
This web app provides information about bus routes starting from kempegowda bus stand in Bengaluru, including platform numbers, destinations, and VIA details. The app also displays a map with labeled placemarks of bus platform numbers.

## Motivation
Google Maps is awesome but at the time of this app being developed it didn't have 2 main things specific to kempegowda bus stand area in Bengaluru
1. The bus route doesn't show the platform number at which the Bus is gonna start it's journey
2. The maps doesn't indicate or have labels for the platform numbers on the map

The above 2 are inconvenient for people and they generally get through by asking around or spending too much of time exploring themselves. So I wanted to create an absolute simple web application as  quickly as possible.

## Data Source Credits
1. Bus Route Data Reference: https://data.opencity.in/dataset/bengaluru-public-transport-infrastructure/resource/bmtc-majestic-bus-stand-platform--routes
2. Base Map Reference: https://data.opencity.in/dataset/bengaluru-public-transport-infrastructure/resource/bmtc-majestic-bus-stand-platform--map

## Usage

Make sure you have python installed in your computer
and create your own virtual environment 
### Clone the repo
`git clone git@github.com:ausurya/bengaluru_kbs_platform.git`
### Change directory 
`cd bengaluru_kbs_platform`
### Install dependencies if required
`pip install streamlit`

`pip install -r requirements.txt`
### Run the app
`streamlit run app/app.py`

You should see the app opened in your default web browser at localhost

## Deployment

The app is deployed to the streamlit community cloud at https://kbsplatform.streamlit.app/



