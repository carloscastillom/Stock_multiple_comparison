# Stock_multiple_comparison
Compare multiples over a set of stocks

# Ticker Comparison Tool

This is a Python script that allows you to compare the fundamental data of multiple stocks in a given industry. The script retrieves the fundamental data from Yahoo Finance API and outputs the data to the console or to a CSV file.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Introduction

The Ticker Comparison Tool is a Python script that allows you to compare the fundamental data of multiple stocks in a given industry. The script retrieves the following fundamental data for each stock:

- Market Cap
- Trailing P/E
- Forward P/E
- Price/Book
- Enterprise Value/Revenue
- Enterprise Value/EBITDA

You can choose to output the data to the console or to a CSV file.

## Installation

1. Clone the repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt` in your terminal.
3. Create a virtual environment and activate it.

## Usage

To use the Ticker Comparison Tool, you need to provide a list of tickers that you want to compare. You can modify the list of tickers in the `tickers` variable in the script. By default, the script compares the fundamental data of Microsoft, Apple, and Airbnb.

To run the script and output the data to the console, navigate to the directory where the script is located in your terminal and run the following command:

python pull_data.py

To output the data to a CSV file, run the following command instead:

python pull_data.py --output-file data.csv
