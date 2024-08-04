import csv
from time import sleep

import numpy as np
from PIL import Image


def display(buf_a, buf_b):
	BLACK = 1
	RED = 2

	color_mapping = {
		0: (255, 255, 255),
		1: (0, 0, 0),
		2: (255, 0, 0)
	}

	buf_a_unpacked = np.unpackbits(np.array(buf_a, dtype=np.uint8))
	buf_b_unpacked = np.unpackbits(np.array(buf_b, dtype=np.uint8))

	width = 136
	height = 250

	buf_a = buf_a_unpacked[:height * width].reshape((height, width))
	buf_b = buf_b_unpacked[:height * width].reshape((height, width))

	buf = np.zeros((height, width), dtype=np.uint8)

	for i in range(height):
		for j in range(width):
			if buf_a[i, j] == 0:
				buf[i, j] = BLACK
			elif buf_b[i, j] == 1:
				buf[i, j] = RED
			else:
				buf[i, j] = 0

	height, width = buf.shape
	image_array = np.zeros((height, width, 3), dtype=np.uint8)
	for y in range(height):
		for x in range(width):
			image_array[y, x] = color_mapping[buf[y,x]]
	image = Image.fromarray(image_array, 'RGB')
	image.show()


with open("./example.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    in_packet = False
    in_b_w = False
    in_y = False
    b_w = []
    y = []
    for row in reader:
        record = [int(row[2], 16), int(row[3], 16)]
        is_command = record[1] == 0x00
        is_data = not is_command
        if is_command:
            command = record[0]
            if command == 0x01:
                in_packet = True
            elif command == 0x20:
                in_packet = False
                display(b_w, y)
                b_w = []
                y = []
            elif command == 0x24:
                in_b_w = True
            elif command == 0x26:
                in_y = True
                in_b_w = False
        elif is_data:
            if in_packet:
                data = record[0]
                if in_b_w:
                    b_w.append(data)
                elif in_y:
                    y.append(data)
