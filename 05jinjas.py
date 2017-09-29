from flask import Flask, render_template
from utils import occupations

jinjas_in_the_night = Flask(__name__)

@jinjas_in_the_night.route("/")
def root():
	return "Please go to the /occupations directory :)"

@jinjas_in_the_night.route("/occupations")
def occ_site():
		return render_template("template.html", data = occupations.open_da_occupations(), randomed = occupations.get_random_occupation())
	
if __name__ == "__main__":
	jinjas_in_the_night.debug = True
	jinjas_in_the_night.run()

