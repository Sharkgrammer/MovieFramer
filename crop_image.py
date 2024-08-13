def crop_image(image, image_dimen, crop_dimen):
    s = int((image_dimen[0] - crop_dimen[0]) / 2)

    return image.crop((s, image_dimen[1] - crop_dimen[1], image_dimen[0] - s, crop_dimen[1]))
