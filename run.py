from shareideas import create_app

app = create_app()
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

if __name__ == '__main__':
    app.run(debug=True)
