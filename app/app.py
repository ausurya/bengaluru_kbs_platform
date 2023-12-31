from bs4 import BeautifulSoup
import folium
import pandas as pd
from pathlib import Path
import streamlit as st
from streamlit_folium import folium_static

csv_file = Path(__file__).parents[1] / "app/data_source.csv"
# Load the CSV file
df = pd.read_csv(csv_file)


def get_platform_number(bus_route):
    """Function to get platform number based on bus route

    Args:
        bus_route (int): bus route number

    Returns:
        string: platform number, destination, via details
    """
    try:
        row = df[df["Bus Route"] == bus_route].iloc[0]
        platform_number = row["Platform"]
        destination = row["Destination"]
        via = row["VIA"]
        return platform_number, destination, via

    except IndexError:
        return None


def create_folium_map(mapfile):
    """Create folium map to be displayed in app

    Args:
        mapfile (.kml): base map kml file to extract placemarks from

    Returns:
        folium map object: folium map object containing labels of bus platform number
    """
    # Read KML file
    kml_file = (
        Path(__file__).parents[1] / "app/map.kml"
    )  # Replace with the actual path to your KML file

    # Parse KML file
    with open(kml_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "xml")

    # Extract placemark information
    placemarks = soup.find_all("Placemark")

    # Create a Folium Map
    m = folium.Map(location=[12.9776273, 77.5728988], zoom_start=40)

    # Add names of placemarks as text on the map
    for placemark in placemarks:
        name = placemark.find("name").text
        coords = placemark.find("coordinates").text.strip().split(",")
        lat, lon = float(coords[1]), float(coords[0])

        # Create a text marker with the placemark name
        folium.Marker(
            location=[lat, lon],
            icon=folium.DivIcon(
                html=f'<div style="font-size: 10pt; color: blue;">{name.replace("-", "").replace("Platform","")}</div>'
            ),
        ).add_to(m)

    return m


def main():
    st.subheader(":red[Kempegowda Bus Stand Platform Information]", divider="rainbow")

    # Section 1: User Input - Search Bar and Drop Down
    st.subheader("Search Bus Route")
    bus_routes = df["Bus Route"].unique()
    user_input = st.selectbox("", bus_routes)

    # Section 2: Display Platform Number
    if user_input:
        platform_number, destination, via = get_platform_number(user_input)
        if platform_number is not None:
            with st.chat_message("assistant"):
                st.write("Your vahana will arrive at Platform 🚌")
                st.metric("", f"{platform_number}")
                st.markdown(f"Via: {via}")
                st.markdown(f"To: {destination}")

        else:
            st.error(f"Bus Route {user_input} not found.")

    # Section 3: Display the platform map
    st.divider()
    folium_map = create_folium_map("map.kml")
    folium_static(folium_map)


if __name__ == "__main__":
    main()
