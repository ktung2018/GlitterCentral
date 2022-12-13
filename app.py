###########################################################################################
# Final Project -  Glitter Central
# Data Visualization
# Prepared by: Kim Tung (ktung@jh.edu)
# Date: Dec. 12, 2022
#
# For the final project, the user is an audience searching for a Netflix movie to
# watch and reviewing Netflex Movie/TV Shows data via Netflix Analytics in the portal. 
# The audience will perform the following:
#
# Search for movie details by clicking "View Netflix Anlaytics" button on top of the side bar.
# * From "Netflix Analytics" (Tableau), audience is able to find historical data on Netflix 
#   Movies and TV Shows: Movie and TV shows by Year, by Country, by Rating, and top 10 Genre.
# * Generate a new Ethereum account instance by using his/her mnemonic seed phrase.
# * Fetch and display the account balance associated with his/her Ethereum account address.
# * Look up available movie, select the movie and enter the number of tickets to purchase.
# * Calculate the total value of an Ethereum transaction, including the gas estimate,
#   that pays Glitter Central for the tickets.
# * Digitally sign a transaction that pays Glitter Central for ticket purchased, and send
#   this transaction to the Ganache blockchain.
# * Review the transaction hash code associated with the validated blockchain transaction.
#
###########################################################################################
# Imports
import streamlit as st
import webbrowser
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

#################################################################################

# Step 1 - Part 3:
# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# Movie Information
# Database of movies including their title, digital address, ticket price per Ether.

candidate_database = {
    'Bullet Proof 2': ['Bullet Proof 2', '0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0', '4.3', .20, "Images/jo.jpeg"],
    'Live Twice Love Once': ['Live Twice Love Once', '0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396', '5.0', .33, 'Images/ash.jpeg'],
    'All the Freckles in the World': ['All the Freckles in the World', '0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45', '4.7', .19, 'Images/kendall.jpeg'],
    'A Fall From From Grace': ['A Fall From From Grace', '0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45', '4.1', .16, 'Images/lane.jpeg']
}

# A list of the Movie Title
movie = ['Bullet Proof 2', 'Live Twice Love Once', 'All the Freckles in the World', 'A Fall From From Grace']


def get_movie():
    """Display the database of Movie Title information."""
    db_list = list(candidate_database.values())

    for number in range(len(movie)):
        st.image(db_list[number][4], width=200)
        st.write('Movie: ', db_list[number][0])
        st.write('Ethereum Account Address: ', db_list[number][1])
        #st.wrtie('Directed by: ', db_list[number][2])
        st.write('Movie Rating: ', db_list[number][2])
        st.write('View Rate per Ether: ', db_list[number][3], 'eth')
        st.text(' \n')

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown('# Glitter Central!')
st.markdown('### Find your movie!')
st.text(' \n')

################################################################################
# Streamlit Sidebar Code - Start
url = 'https://public.tableau.com/app/profile/kim7343/viz/Netflix_16707780336720/Dashboard1?publish=yes'
url2 = 'https://public.tableau.com/app/profile/kim7343/viz/Netflix2_16708761198580/Dashboard2?publish=yes'

if st.sidebar.button('View Netflex Analytics'):
    webbrowser.open_new_tab(url)
if st.sidebar.button('View Netflex Analytics 2'):
    webbrowser.open_new_tab(url2)

st.sidebar.markdown('## Movie Address and Ethernet Balance in Ether')

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function creates the Movie Finder
# customer’s (in this case, your) HD wallet and Ethereum account.

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# A new `st.sidebar.write` function displays the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
# pass it your Ethereum `account.address`.

# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
st.sidebar.write(get_balance(w3,account.address))

##########################################

# Create a select box to chose a Movie 
film = st.sidebar.selectbox('Select a Movie', movie)

# Create a input field to record the number of viewers
viewers = st.sidebar.number_input('Number of Viewers')

st.sidebar.markdown('## Movie, Ticket Price, and Ethereum Address')

# Identify the Movie
candidate = candidate_database[film][0]

# Write the Movie Title to the sidebar
st.sidebar.write(candidate)

# Identify the Movie ticket price
ticket_price = candidate_database[film][3]

# Write the Movie Ticket price to the sidebar
st.sidebar.write(ticket_price)

# Identify the Movie's Ethereum Address
movie_address = candidate_database[film][1]

# Write the Movie's Ethereum Address to the sidebar
st.sidebar.write(movie_address)

# Write the Movie's ticket total price to the sidebar
st.sidebar.markdown('## Total Amount in Ether')

################################################################################
# Step 2 - Part 1
# Sign and Execute a Payment Transaction
# 1. Movie Finder customers will select a Movie from the movie showing
# interface’s drop-down menu, and then input the number of tickets for
# which they’ll purchase.

# 2. Now that the application can calculate a movie's ticket_total, write the code
# that will allow a customer (you, in this case) to send an Ethereum blockchain
# transaction that pays the Glitter Central.

ticket_total = candidate_database[film][3] * viewers
st.sidebar.write(ticket_total)

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function and pass it three parameters:
    # - Your Ethereum `account` information. (Remember that this `account`
    # instance was created when the `generate_account` function was called.)
    #  From the `account` instance, the application will be able to access the
    #  `account.address` information that is needed to populate the `from` data
    # attribute in the raw transaction.
    #- The `movie_address` (which will be created and identified in the
    # sidebar when a customer selects a movie). This will populate the `to`
    # data attribute in the raw transaction.
    # - The `ticket_total` value. This will be passed to the `toWei` function to
    # determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.

if st.sidebar.button('Send Transaction'):
    transaction_hash = send_transaction(w3, account, movie_address, ticket_total)

    # Markdown for the transaction hash
    st.sidebar.markdown('#### Validated Transaction Hash')

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes Movie Titles to the Streamlit page
get_movie()