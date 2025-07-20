from nudenet import NudeDetector
detector = NudeDetector()

def check_nudity_image(image_path, threshold=0.5):
    detections = detector.detect(image_path)
    strong = 0
    classes = ['FEMALE_BREAST_EXPOSED','MALE_GENITALIA_EXPOSED','FEMALE_GENITALIA_EXPOSED',
               'BUTTOCKS_EXPOSED','UNDERWEAR_EXPOSED','BELLY_EXPOSED']
    for det in detections:
        if det['class'] in classes and det['score'] >= threshold:
            strong += 1
    return strong >= 2
