from polygon import RESTClient

class StockFinancials:
    def __init__(self, ticker, PTE, EBT, reportPeriod):
        self.ticker = ticker
        self.PTE = PTE
        self.EBT = EBT
        self.reportPeriod = reportPeriod

def getFinancials(client, ticker):
    response = client.reference_stock_financials(ticker)
    PTE = response.results[0]['priceToEarningsRatio']
    EBT = response.results[0]['earningsBeforeInterestTaxesDepreciationAmortizationUSD']
    reportPeriod = response.results[0]['reportPeriod']

    return StockFinancials(ticker, PTE, EBT, reportPeriod)

def main():
    key = "pbY1RM6pzUSJr4dxTJ0oo3SpZSw7ZxYq"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects

    # price to earnings ratio priceToEarningsRatio
    # Earnings before earningsBeforeInterestTaxesDepreciationAmortizationUSD
    # stock financials
    with RESTClient(key) as client:
        apple = getFinancials(client, "AAPL")
        print(apple.EBT)

        amd = getFinancials(client, "AMD")
        print(amd.PTE)
        print(amd.reportPeriod)


if __name__ == '__main__':
    main()
