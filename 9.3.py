import greatest_common_measure
import time
import random
from concurrent.futures import ProcessPoolExecutor

# def generate_number_list():
#     NUMBERS = []
#     for x in range(10):
#         num1 = ""
#         num2 = ""
#         for i in range(7):
#             num1 += str(random.randint(0,9))
#             num2 += str(random.randint(0,9))
#         krotka = (int(num1),int(num2),)
#         NUMBERS.append(krotka)
#     print(NUMBERS)
#     return NUMBERS

NUMBERS = [(32674319, 96399392), (12804863, 31630753),
           (74948553, 16042901), (35048343, 90780100),
           (71198012, 5609607), (38715533, 89353895),
           (96623884, 37527846), (87868545, 81237107),
           (18157878, 3127113), (43166730, 57695989)]

def main():
    print("Calculation START")
    start = time.time()
    amount_of_process = ProcessPoolExecutor(max_workers=4)
    result = list(amount_of_process.map(greatest_common_measure.greatest_common_measure,NUMBERS))
    end = time.time()
    print("Calculation END")
    run_time = end - start
    print(f"Time: {run_time:.2f}s")

if __name__ == '__main__':
    main()

