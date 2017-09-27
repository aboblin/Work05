from flask import Flask, render_template
import random, csv

jinjas_in_the_night = Flask(__name__)

@jinjas_in_the_night.route("/")
def root():
	return "Please go to the /occupations directory :)"

@jinjas_in_the_night.route("/occupations")
def occ_site():
		return render_template("template.html", datai = data, randomed = get_random_occupation())

data = {}

with open("occupations.csv", "r") as infile:
	reader = csv.reader(infile)
	for row in reader:
		k = row[0]
		if k != "Job Class" and k != "Total":
			v = float(row[1])
			data[k] = v

def get_random_occupation():
	occNum = random.random() * 99.8
	for key in data:
		if occNum - data[key] > 0:
			occNum = occNum - data[key]
		else:
			return key

if __name__ == "__main__":
	babys_app.debug = True
	babys_app.run()

