import streamlit as st
import yfinance as yf
import finnhub
from datetime import datetime, timedelta

# Initialize the finnhub client
finnhub_client = finnhub.Client(api_key="cnqu07hr01qs2jr528n0cnqu07hr01qs2jr528ng")

# Set the title of the Streamlit app
st.title('Finlang-Forecaster')

# Create input fields for user data
ticker_symbol = st.text_input('Ticker Symbol (e.g., AAPL, MSFT, NVDA)', '')
start_date = st.date_input('Prediction Start Date', value=datetime.today())
past_weeks = st.number_input('Number of Past Weeks for Market News', min_value=1, max_value=52, value=4)
add_financials = st.checkbox('Add Latest Basic Financials')

# Create submit and cancel buttons
submit_button = st.button('Submit')
cancel_button = st.button('Cancel')

if submit_button:
    if ticker_symbol and start_date:
        # Display the user inputs for confirmation
        st.write(f'Ticker Symbol: {ticker_symbol}')
        st.write(f'Prediction Start Date: {start_date.strftime("%Y-%m-%d")}')
        st.write(f'Number of Past Weeks: {past_weeks}')
        st.write(f'Add Latest Basic Financials: {add_financials}')

        # Convert start_date to string in the required format
        current_date_str = start_date.strftime('%Y-%m-%d')
        past_date = start_date - timedelta(weeks=past_weeks)
        past_date_str = past_date.strftime('%Y-%m-%d')

        # Analysis Summary
        st.subheader("Analysis Summary")
        st.write("### Company Information Summary")

        # Retrieve basic financials if the checkbox is selected
        if add_financials:
            try:
                stock = yf.Ticker(ticker_symbol)
                financials = stock.financials
                if not financials.empty:
                    st.write("Financials:")
                    st.write(financials)
                else:
                    st.write("No basic financials reported.")
            except Exception as e:
                st.write(f"An error occurred while retrieving financial data: {e}")
        
        # Retrieve and display market news headlines and summaries
        try:
            past_news = finnhub_client.company_news(ticker_symbol, _from=past_date_str, to=current_date_str)
            st.write("### Market News")
            if past_news:
                positive_developments = []
                potential_concerns = []
                for news in past_news:
                    st.write(f"**Headline**: {news['headline']}")
                    st.write(f"**Summary**: {news['summary']}")
                    st.write("---")
                    if "positive" in news['summary'].lower():  # simplistic check for positive news
                        positive_developments.append(news['summary'])
                    elif "concern" in news['summary'].lower() or "risk" in news['summary'].lower():  # simplistic check for concerns
                        potential_concerns.append(news['summary'])

                st.write("### Positive Developments")
                if positive_developments:
                    for development in positive_developments:
                        st.write(f"- {development}")
                else:
                    st.write("No positive developments found.")
                
                st.write("### Potential Concerns")
                if potential_concerns:
                    for concern in potential_concerns:
                        st.write(f"- {concern}")
                else:
                    st.write("No potential concerns found.")
            else:
                st.write("No market news available for this period.")
        except Exception as e:
            st.write(f"An error occurred while retrieving market news: {e}")
        
        # Placeholder for prediction and analysis
        st.subheader("Prediction & Analysis")
        prediction = "The stock price is predicted to increase by 3% over the coming week."
        st.write("### Prediction")
        st.write(prediction)
        st.write("### Analysis Summary")
        st.write("Based on recent market news and financial data, the FinGPT-Forecaster predicts a moderate increase in stock price due to strong earnings and new product launches, despite some regulatory and competitive pressures.")
        
    else:
        st.write("Please enter a valid ticker symbol and start date.")

if cancel_button:
    # Logic to reset the input fields
    st.experimental_rerun()
