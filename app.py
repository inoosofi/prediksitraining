from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
     return render_template('index.html', unique_viwers=0)
@app.route('/predict', methods=['POST'])
def predict():
    category = float(request.form['Category'])
    day = float(request.form['Day'])
    time = float(request.form['Time'])
    
    x=np.array([[category,day,time]])
    
    
    prediction = model.predict(x)
    output = round(prediction[0], 0)

    #return render_template('index.html', insurance_cost=output, age=age, sex=sex, smoker=smoker)
    return render_template('index.html', unique_viwers=output)

if __name__ == '__main__':
    app.run(debug=True)