import os
import time
import random
import requests
import pdftotext

###### Functions ######


def pdf_to_txt(input_pdf, output_txt):
    try:
        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            with open(input_pdf, "rb") as f:
                pdf = pdftotext.PDF(f)
                for page in pdf:
                    txt_file.write(page)
        print(f"Text extracted from {input_pdf} and saved to {output_txt}!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


def download_file(url, local_filename):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded as {local_filename}!")
        filename_txt = str(year) + "_" + str(month).zfill(2) + \
            "_" + str(day).zfill(2) + ".txt"
        pdf_to_txt(local_filename, os.path.join(folder_path, filename_txt))
    else:
        print(
            f"Failed to download file from {url}. Status code: {response.status_code}")


def random_sleep(x, y):
    sleep_time = random.uniform(int(x), int(y))
    time.sleep(int(sleep_time))


###### Code ######


if __name__ == "__main__":
    working_directory = os.path.join(os.getcwd(), 'Data')

    for year in range(2021, 2023):
        for month in range(1, 13):
            folder_path = os.path.join(
                working_directory, str(year), str(month).zfill(2))

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Folder {folder_path} created!")

            for day in range(1, 32):
                link = "https://www.granma.cu/file/pdf/" + str(year) + "/" + str(month).zfill(2) + "/" + str(
                    day).zfill(2) + "/" + "G_" + str(year) + str(month).zfill(2) + str(day).zfill(2) + "09.pdf"

                filename_pdf = str(year) + "_" + str(month).zfill(2) + \
                    "_" + str(day).zfill(2) + ".pdf"

                try:
                    download_file(link, os.path.join(
                        folder_path, filename_pdf))
                except Exception as e:
                    print("Error occurred:", str(e))

                random_sleep(10, 30)