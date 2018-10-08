sudo apt-get update
sudo apt install postgresql postgresql-contrib
sudo apt-get -y upgrade
sudo apt-get install python3-pip
pip3 install Babel decorator docutils ebaysdk feedparser gevent greenlet html2text Jinja2 lxml Mako MarkupSafe mock num2words ofxparse passlib Pillow psutil psycogreen psycopg2 pydot pyparsing PyPDF2 pyserial python-dateutil python-openid pytz pyusb PyYAML qrcode reportlab requests six suds-jurko vatnumber vobject Werkzeug XlsxWriter xlwt xlrd
sudo apt-get install -y npm
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo npm install -g less less-plugin-clean-css
sudo apt-get install node-less
sudo apt-get install python-software-properties

sudo -u postgres psql
ALTER USER postgres PASSWORD 'felino'

sudo su postgres
createuser -s odoo
createuser -s nuansa
sudo adduser --system --home=/opt/odoo --group odoo
cd /opt/odoo
sudo wget https://pypi.python.org/packages/a8/70/bd554151443fe9e89d9a934a7891aaffc63b9cb5c7d608972919a002c03c/gdata-2.0.18.tar.gz
sudo tar zxvf gdata-2.0.18.tar.gz
sudo chown -R odoo: gdata-2.0.18
sudo -s
cd gdata-2.0.18/
python setup.py install


cd /opt/odoo

sudo apt-get install git
sudo su - odoo -s /bin/bash
git clone https://www.github.com/odoo/odoo --depth 1 --branch 11.0 --single-branch
sudo mkdir /var/log/odoo
