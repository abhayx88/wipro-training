import requests
import threading
import time

urls = [
    "https://example.com/data1",
    "https://example.com/data2",
    "https://example.com/data3",
    "https://example.com/data4"
]


def download_file(url):
    try:
        response = requests.get(url)
        filename = url.split("/")[-1] + ".txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")


start_seq = time.time()

for url in urls:
    download_file(url)

end_seq = time.time()
print("\nSequential Time:", end_seq - start_seq)

threads = []
start_thread = time.time()

for url in urls:
    t = threading.Thread(target=download_file, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_thread = time.time()
print("\nThreading Time:", end_thread - start_thread)
