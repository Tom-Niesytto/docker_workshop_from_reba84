from flask import Flask, render_template
import random
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
app = Flask(__name__)


digits = load_digits()
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)
# loaded_model = pickle.load(open("model/logreg_model.pkl", 'rb'))
image = x_test[200]
image_res = np.array(image, dtype='float')
pixels = image_res.reshape((8, 8))

plt.imshow(pixels, cmap='gray')
plt.axis('off')
plt.savefig('static/number.png', bbox_inches='tight')

@app.route('/')
def index():
    # prediction = loaded_model.predict(image.reshape(1,-1))
    #, pred = prediction
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
