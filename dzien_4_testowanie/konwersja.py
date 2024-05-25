import requests

[
    {
        "table": "A",
        "no": "101/A/NBP/2024",
        "effectiveDate": "2024-05-24",
        "rates": [
            {
                "currency": "bat (Tajlandia)",
                "code": "THB",
                "mid": 0.1073
            },
            {
                "currency": "dolar amerykański",
                "code": "USD",
                "mid": 3.9376
            },
            {
                "currency": "dolar australijski",
                "code": "AUD",
                "mid": 2.6033
            },
            {
                "currency": "dolar Hongkongu",
                "code": "HKD",
                "mid": 0.5040
            },
            {
                "currency": "dolar kanadyjski",
                "code": "CAD",
                "mid": 2.8695
            },
            {
                "currency": "dolar nowozelandzki",
                "code": "NZD",
                "mid": 2.4041
            },
            {
                "currency": "dolar singapurski",
                "code": "SGD",
                "mid": 2.9151
            },
            {
                "currency": "euro",
                "code": "EUR",
                "mid": 4.2624
            },
            {
                "currency": "forint (Węgry)",
                "code": "HUF",
                "mid": 0.011056
            },
            {
                "currency": "frank szwajcarski",
                "code": "CHF",
                "mid": 4.3039
            },
            {
                "currency": "funt szterling",
                "code": "GBP",
                "mid": 5.0022
            },
            {
                "currency": "hrywna (Ukraina)",
                "code": "UAH",
                "mid": 0.0981
            },
            {
                "currency": "jen (Japonia)",
                "code": "JPY",
                "mid": 0.025077
            },
            {
                "currency": "korona czeska",
                "code": "CZK",
                "mid": 0.1725
            },
            {
                "currency": "korona duńska",
                "code": "DKK",
                "mid": 0.5713
            },
            {
                "currency": "korona islandzka",
                "code": "ISK",
                "mid": 0.028359
            },
            {
                "currency": "korona norweska",
                "code": "NOK",
                "mid": 0.3701
            },
            {
                "currency": "korona szwedzka",
                "code": "SEK",
                "mid": 0.3671
            },
            {
                "currency": "lej rumuński",
                "code": "RON",
                "mid": 0.8569
            },
            {
                "currency": "lew (Bułgaria)",
                "code": "BGN",
                "mid": 2.1793
            },
            {
                "currency": "lira turecka",
                "code": "TRY",
                "mid": 0.1220
            },
            {
                "currency": "nowy izraelski szekel",
                "code": "ILS",
                "mid": 1.0722
            },
            {
                "currency": "peso chilijskie",
                "code": "CLP",
                "mid": 0.004328
            },
            {
                "currency": "peso filipińskie",
                "code": "PHP",
                "mid": 0.0677
            },
            {
                "currency": "peso meksykańskie",
                "code": "MXN",
                "mid": 0.2358
            },
            {
                "currency": "rand (Republika Południowej Afryki)",
                "code": "ZAR",
                "mid": 0.2141
            },
            {
                "currency": "real (Brazylia)",
                "code": "BRL",
                "mid": 0.7654
            },
            {
                "currency": "ringgit (Malezja)",
                "code": "MYR",
                "mid": 0.8354
            },
            {
                "currency": "rupia indonezyjska",
                "code": "IDR",
                "mid": 0.00024621
            },
            {
                "currency": "rupia indyjska",
                "code": "INR",
                "mid": 0.047388
            },
            {
                "currency": "won południowokoreański",
                "code": "KRW",
                "mid": 0.00288
            },
            {
                "currency": "yuan renminbi (Chiny)",
                "code": "CNY",
                "mid": 0.5435
            },
            {
                "currency": "SDR (MFW)",
                "code": "XDR",
                "mid": 5.1988
            }
        ]
    }
]


class Konwerter:
    def __init__(self):
        j = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/?format=json').json()
        self.kursy = {d['code'].lower(): d['mid'] for d in j[0]['rates']}

    def konwertuj(self, waluta, kwota):
        return round(self.kursy[waluta.lower()] * kwota, 2)

if __name__ == '__main__':
    k = Konwerter()
    print(k.konwertuj('usd', 1000))