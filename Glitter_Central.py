# Fintech Finder

################################################################################
# For this Challenge, you will assume the perspective of a Fintech Finder
# customer in order to do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase
# (which you created earlier in the module).

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total value of an Ethereum transaction, including the gas
# estimate, that pays a Fintech Finder candidate for their work.

# * Digitally sign a transaction that pays a Fintech Finder candidate, and send
# this transaction to the Ganache blockchain.

# * Review the transaction hash code associated with the validated blockchain transaction.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
#################################################################################

# Step 1 - Part 3:
# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
# YOUR CODE HERE
from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# Fintech Finder Candidate Information
# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.

candidate_database = {
    'Grinch': ['Grinch', '0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0', '4.3', .20, "Images/jo.jpeg"],
    'Mickey': ['Michey', '0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396', '5.0', .33, 'Images/ash.jpeg'],
    'White Christmas': ['White Christmas', '0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45', '4.7', .19, 'Images/kendall.jpeg'],
    'Caspers': ['Caspers', '0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45', '4.1', .16, 'Images/lane.jpeg']
}

# A list of the FinTech Finder candidates first names
people = ['Grinch', 'Mickey', 'White Christmas', 'Caspers']


def get_people():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write('Movie: ', db_list[number][0])
        st.write('Ethereum Account Address: ', db_list[number][1])
        st.write('Movie Rating: ', db_list[number][2])
        st.write('View Rate per Ether: ', db_list[number][3], 'eth')
        st.text(' \n')

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown('# Glitter Central!')
st.markdown('## Find your movie!')
st.text(' \n')

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown('## Movie Address and Ethernet Balance in Ether')

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function creates the Fintech Finder
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

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Movie', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input('Number of Viewers')

st.sidebar.markdown('## Movie, Ticket Price, and Ethereum Address')

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.markdown('## Total Amount in Ether')

################################################################################
# Step 2 - Part 1
# Sign and Execute a Payment Transaction
# 1. Fintech Finder customers will select a fintech professional from the
# application interface’s drop-down menu, and then input the amount of time for
# which they’ll hire the worker.

# 2. Now that the application can calculate a candidate’s wage, write the code
# that will allow a customer (you, in this case) to send an Ethereum blockchain
# transaction that pays the hired candidate.

wage = candidate_database[person][3] * hours
st.sidebar.write(wage)

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function and pass it three parameters:
    # - Your Ethereum `account` information. (Remember that this `account`
    # instance was created when the `generate_account` function was called.)
    #  From the `account` instance, the application will be able to access the
    #  `account.address` information that is needed to populate the `from` data
    # attribute in the raw transaction.
    #- The `candidate_address` (which will be created and identified in the
    # sidebar when a customer selects a candidate). This will populate the `to`
    # data attribute in the raw transaction.
    # - The `wage` value. This will be passed to the `toWei` function to
    # determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.

if st.sidebar.button('Send Transaction'):
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown('#### Validated Transaction Hash')

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people()