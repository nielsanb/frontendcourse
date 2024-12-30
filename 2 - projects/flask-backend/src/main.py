from website import create_app

app = create_app()

#This is what we call an "entrypoint"
if __name__ == '__main__':
    app.run(debug=True)
