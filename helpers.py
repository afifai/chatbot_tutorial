import requests
from datetime import date
def kasus_hari_ini():
    url = 'https://covid19.ngodingpython.com/api/hari-ini/'
    r = requests.get(url)
    data = r.json()
    message_template = \
'''KASUS COVID-19 HARI INI\n
Tanggal {}\n
Kasus Positif : {} (+{})\n
Dalam Perawatan : {} (+{})\n
Sembuh : {} (+{})\n
Meninggal : {} (+{})\n\n
API dari : https://covid19.ngodingpython.com\n
Sumber : https://covid19.go.id
'''.format(str(date.today()),
                        data['data']['total_kasus'],
                        data['data']['kasus_harian'],
                        data['data']['total_perawatan'],
                        data['data']['perawatan_harian'],
                        data['data']['total_sembuh'],
                        data['data']['sembuh_harian'],
                        data['data']['total_meninggal'],
                        data['data']['meninggal_harian'])
    return message_template
