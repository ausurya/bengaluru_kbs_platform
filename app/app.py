import streamlit as st
import pandas as pd

# Load the CSV file
csv_file = '../data/source.csv'  # Replace 'your_file.csv' with the actual CSV file path
df = pd.read_csv(csv_file)

# Function to get platform number based on bus route
def get_platform_number(bus_route):
    try:
        row = df[df['Bus Route'] == bus_route].iloc[0]
        platform_number = row['Platform']
        destination = row['Destination']
        via = row['VIA']
        return platform_number, destination, via
        
    except IndexError:
        return None

# Streamlit App
def main():
    st.title(':red[Kempegowda Bus Stand Platform Information]')

    # Section 1: User Input - Search Bar and Drop Down
    st.sidebar.header('Search Bus Route')
    bus_routes = df['Bus Route'].unique()
    user_input = st.sidebar.selectbox('Bus list:', bus_routes)


    # Section 2: Display Platform Number
    # st.header('Platform Number Information')
    if user_input:
        platform_number, destination, via = get_platform_number(user_input)
        if platform_number is not None:
            st.metric("Platform number", f"{platform_number}")
            st.metric("VIA", f"{via}")
            st.metric("To", destination)
            
        else:
            st.error(f'Bus Route {user_input} not found.')

    # Section 3: Display Map Image
    # st.header('Bus Route Map')
    # map_image_path = 'path/to/your/map_image.png'  # Replace with the actual path to your map image
    # map_image = mpimg.imread(map_image_path)
    # st.image(map_image, use_column_width=True, caption='Bus Route Map')

if __name__ == '__main__':
    main()
