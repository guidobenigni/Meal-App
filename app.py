from flask import Flask, render_template, request

app = Flask(__name__)

meal_data = {
    'Frühstück': {
        'Cut': ['3 Eier, 1 Scheibe Brot, 1 kleiner Apfel, 1 Scoop Whey mit Wasser'],
        'Maintain': ['5 Eier, 1 Scheibe Brot mit Butter, 1 Apfel, 1 Scoop Whey mit Milch'],
        'Bulk': ['5 Eier, 2 Scheiben Brot mit Butter, 1 Banane, 1 Scoop Whey mit Milch']
    },
    'Mittagessen': {
        'Cut': ['150 g Hähnchen, 80 g Reis, 1 TL Öl, 150 g Brokkoli'],
        'Maintain': ['200 g Hähnchen, 100 g Reis, 1 EL Öl, 150 g Brokkoli'],
        'Bulk': ['220 g Hähnchen, 120 g Reis, 1 EL Öl, 200 g Brokkoli']
    },
    'Abendessen': {
        'Cut': ['200 g Skyr, 20 g Whey, 20 g Nüsse, 30 g Haferflocken'],
        'Maintain': ['250 g Skyr, 30 g Whey, 30 g Nüsse, 50 g Haferflocken'],
        'Bulk': ['250 g Skyr, 30 g Whey, 40 g Nüsse, 60 g Haferflocken, 1 Dattel']
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    selection = {}
    if request.method == "POST":
        for meal in meal_data:
            selected_phase = request.form.get(meal)
            if selected_phase:
                selection[meal] = meal_data[meal][selected_phase][0]
    return render_template("index.html", meal_data=meal_data, selection=selection)

if __name__ == "__main__":
    app.run(debug=True)
