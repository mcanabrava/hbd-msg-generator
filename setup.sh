mkdir -p ~/.streamlit/

echo "\
[generaç]\n\
email = \"mcanabrava.andrade@gmail.com"\"n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless= true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml