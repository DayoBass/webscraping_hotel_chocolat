"""
Extract data from 2,310 pages
"""
# import relevant libraries
import pandas as pd
import os
import time
from single_page_check import scrape_single_page
from constant import number_of_pages_to_extract, output_data, wait_time_seconds

# start timing the extraction
start_time = time.time()
print(start_time)

# scraping from 2310 pages
# create list and loop through the number of pages to extract
chocolat_data = []
for i in range(1, number_of_pages_to_extract):
    choco_url = 'https://uk.trustpilot.com/review/hotelchocolat.com?page={}'.format(i)
    chocolat_data += scrape_single_page(choco_url)
    # after every 5 pages, wait for 185 seconds (wait_time_seconds) before continuing
    if i % 20 == 0:
        time.sleep(wait_time_seconds)

# Convert data to DataFrame
df_chocolat = pd.DataFrame(chocolat_data)

# First check if output folder already exists, otherwise, create one
if not os.path.exists(output_data):
    os.makedirs(output_data)
    print(f'Output folder created at: {output_data}')

# Save to CSV file in the output folder
hotel_chocolat_csv_file = os.path.join(output_data, 'df_chocolat.csv')
df_chocolat.to_csv(hotel_chocolat_csv_file, index=False)
print(f'CSV file created at: {hotel_chocolat_csv_file}')

# Save to Excel file in the output folder
hotel_chocolat_excel_file = os.path.join(output_data, 'df_chocolat.xlsx')
df_chocolat.to_excel(hotel_chocolat_excel_file, index=False)
print(f'Excel file created at: {hotel_chocolat_excel_file}')

# calculate and print the time spent for the extraction
end_time = time.time()
time_spent = end_time - start_time
print(f'Time spent for extraction: {time_spent} seconds')
