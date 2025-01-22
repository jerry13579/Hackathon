from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('search_query').lower()
    results_rmp = []  # Results from 'RMPSCRAPE.csv'
    results_phys = []  # Results from 'PHYS_F2023_data.csv'

    with open('Scraped/RMPSCRAPE.csv', mode='r') as rmp_csv_file:
        rmp_csv_reader = csv.DictReader(rmp_csv_file)
        for row in rmp_csv_reader:
            if (
                query in row['First Name'].lower()
                or query in row['Last Name'].lower()
                or query in row['Rating'].lower()
                or query in row['Difficulty'].lower()
            ):
                results_rmp.append(row)

    with open('Scraped/PHYS_F2023_data.csv', mode='r') as phys_csv_file:
        phys_csv_reader = csv.DictReader(phys_csv_file)
        for row in phys_csv_reader:
            if (
                query in row['FIRST NAME'].lower()
                or query in row['LAST NAME'].lower()
            ):
                results_phys.append(row)

    return render_template('search_results.html', results_rmp=results_rmp, results_phys=results_phys)

if __name__ == '__main__':
    app.run(debug=True)