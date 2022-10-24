import requests

def numverifyRequest(number : str):
    params = {"number" : number}
    apiKey2 ="YkPacMHSbgX11IetFkpIuvzPUhpcSsRt"
    apikey = "cpJWvQjOx2mz3DDvGKPkz1gFIisHTDlx"
    headers = {"apikey" : apikey}
    url = 'https://api.apilayer.com/number_verification/validate'
    response = requests.get(url , headers = headers, params = params )
    return response
