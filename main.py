import os
import time
import random
import requests
import pdftotext
import sys

###### Functions ######


def pdf_to_txt(input_pdf, output_txt):
    try:
        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            with open(input_pdf, "rb") as f:
                pdf = pdftotext.PDF(f)
                for page in pdf:
                    txt_file.write(page)
        print(f"Text extracted from {input_pdf} and saved to {output_txt}!")
        sys.stdout.flush()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        sys.stdout.flush()


def download_file(url, local_filename, type = "completo"):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded as {local_filename}!")
        if type == "completo":
            filename_txt = str(year) + "_" + str(month).zfill(2) + \
                "_" + str(day).zfill(2) + ".txt"
        elif type == "opinion":
            filename_txt = str(year) + "_" + str(month).zfill(2) + \
                "_" + str(day).zfill(2) + "_opinion.txt"
        else:
            raise Exception("Error, type is missing. Go check download_file() function.") 
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

    for year in range(2023, 2024):
        for month in range(7, 10):
            folder_path = os.path.join(
                working_directory, str(year), str(month).zfill(2))

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Folder {folder_path} created!")

            for day in range(1, 32):
                sys.stdout.flush()
                link = "https://www.juventudrebelde.cu/printed/" + str(year) + "/" + str(month).zfill(2) + "/" + str(
                    day).zfill(2) + "/icompleta.pdf"
                filename_pdf = str(year) + "_" + str(month).zfill(2) + \
                    "_" + str(day).zfill(2) + ".pdf"
                
                link_opinion = "https://www.juventudrebelde.cu/printed/" + str(year) + "/" + str(month).zfill(2) + "/" + str(
                    day).zfill(2) + "/iopinion.pdf"
                filename_pdf_opinion = str(year) + "_" + str(month).zfill(2) + \
                    "_" + str(day).zfill(2) + "_opinion.pdf"

                try:
                    download_file(link, os.path.join(
                        folder_path, filename_pdf))
                except Exception as e:
                    print("Error occurred:", str(e))

                random_sleep(15, 30)

                try:
                    download_file(link_opinion, os.path.join(
                        folder_path, filename_pdf_opinion), "opinion")
                except Exception as e:
                    print("Error occurred:", str(e))

                sys.stdout.flush()

                random_sleep(15, 30)
