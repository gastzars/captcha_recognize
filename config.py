# about captcha image
IMAGE_HEIGHT = 88
IMAGE_WIDTH = 280
CHAR_SETS = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CLASSES_NUM = len(CHAR_SETS)
CHARS_NUM = 6
# for train
RECORD_DIR = './data'
TRAIN_FILE = 'train.tfrecords'
VALID_FILE = 'valid.tfrecords'
