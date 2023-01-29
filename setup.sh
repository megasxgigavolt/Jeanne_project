mkdir -p ~/.streamlit/
echo "
[general]n
email = "jeanne_cavil@yahoo.fr"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml