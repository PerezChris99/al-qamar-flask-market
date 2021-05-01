from market import app

#checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)