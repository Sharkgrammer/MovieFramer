# Yoinked from chatgpt and modified
counter = 1


# Convert the image to a byte array suitable for the open source Watchy framework
def to_byte_arr(image, image_dimen, output_text_file):
    global counter

    image = image.convert('1')

    pixels = list(image.getdata())

    hex_data = []

    print(image_dimen)

    for y in range(0, image_dimen[1]):
        for x in range(0, image_dimen[0], 8):
            byte = 0
            for i in range(8):
                if x + i < image_dimen[0] and pixels[y * image_dimen[0] + (x + i)] == 0:
                    byte |= (1 << (7 - i))
            hex_data.append(f"0x{byte:02x}")

    # Print out the array in the format you provided
    formatted_output = ", ".join(hex_data)
    append_to_file(f"const unsigned char f{counter} [] PROGMEM = {{\n\t{formatted_output}\n}};", output_text_file)
    counter += 1


def append_to_file(byte_data, output_text_file):
    with open(output_text_file, 'a') as file:
        file.write(f"{byte_data}\n\n")
