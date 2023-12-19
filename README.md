# Google Maps Distance Calculator

This Python script uses the Google Maps API to calculate the distance and duration of a journey between two locations based on user input.

## Prerequisites

Before you start, make sure you have the following:

- Python installed on your machine.
- Google Maps API key. You can obtain one [here](https://developers.google.com/maps/documentation/distance-matrix/get-api-key).

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yusufkaancelik/google-maps-distance-calculator.git
    ```

2. Change into the project directory:

    ```bash
    cd google-maps-distance-calculator
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the terminal and navigate to the project directory.

2. Run the script:

    ```bash
    python distance_calculator.py
    ```

3. Follow the prompts to enter your information:
   - Enter your name and surname.
   - Provide departure and arrival locations.
   - Specify the departure time in the format HH:MM:SS.
   - Choose the vehicle type (driving, walking, bicycle, two-wheeler).

4. The script will then calculate and display the distance and duration of the journey.

## Configuration

Before running the script, make sure to configure your Google Maps API key in the `distance_calculator.py` file:

```python
# Google Maps API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')
```

Replace `'YOUR_API_KEY'` with your actual API key.
