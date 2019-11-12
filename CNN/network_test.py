from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import argparse

classes =['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

model = load_model('model.h5')
print('Loaded trained Model\n')
 
# load and prepare the image
def load_image(filename):
	img = load_img(filename, target_size=(32, 32))
	img = img_to_array(img)
	img = img.reshape(1, 32, 32, 3)
	img = img.astype('float32')
	img = img / 255.0
	return img

parser = argparse.ArgumentParser(description='Classify Input Images')
parser.add_argument('--input',type=str,required=True,help='Input Image eg:img.jpg')
args = parser.parse_args()
    
img = load_image(args.input)
result = model.predict_classes(img)
print('The image represents:', classes[result[0]])
