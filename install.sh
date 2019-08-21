echo "[!] Installing Package"
sleep 1
apt-get install python -y
pip2 install requests urllib3 bs4 pyquery
python run.py
