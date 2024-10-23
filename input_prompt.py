import streamlit as st

# Set the title of the Streamlit app
st.title('Finlang-forecaster')

# Create input fields for user data
ticker_symbol = st.text_input('Ticker Symbol (e.g., AAPL, MSFT, NVDA)', '')
start_date = st.date_input('Prediction Start Date (yyyy-mm-dd)')
past_weeks = st.number_input('Number of Past Weeks for Market News', min_value=1, max_value=52, value=4)
add_financials = st.checkbox('Add Latest Basic Financials')

# Display the user inputs for confirmation
st.write(f'Ticker Symbol: {ticker_symbol}')
st.write(f'Prediction Start Date: {start_date}')
st.write(f'Number of Past Weeks: {past_weeks}')
st.write(f'Add Latest Basic Financials: {add_financials}')


