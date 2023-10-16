import cv2
import glob

imgs_path = '/mnt/s3bucket/alector-immuno-neurology/DeAOT/Dataset/images/test/'

file_list = glob.glob(imgs_path + "/*.jpg")
img_list = [cv2.imread(im_file) for im_file in file_list]

for img_file in file_list:
  img = cv2.imread(img_file)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
  color_img = color_img[:, :, :]
  print(color_img.shape)
  cv2.imwrite(img_file, color_img)
