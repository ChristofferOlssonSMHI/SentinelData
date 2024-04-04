from dotenv import dotenv_values, set_key
import requests
import os.path

def request_url():
    # search filters
    name_contains_1 = 'OL_2_WFR'
    # name_contains_1 = 'S2A_MSIL1C_20220627T100611_N0400_R022_T33VXD'
    name_contains_2 = '_NR_'
    mission = 'SENTINEL-3'
    start_date = '2024-02-28T00:00:00.000Z'
    end_date = '2024-03-31T00:00:00.000Z'
    # Västerhaven
    bounding_box = 'POLYGON ((7.256595 58.052452, 10.535889 59.956385, 10.83252 59.95501, 13.095703 56.619977, 13.183594 55.466399, 14.018555 55.541065, 14.194336 56.059769, 14.72168 56.267761, 15.79834 56.24335, 15.732422 54.059388, 14.633789 53.527248, 9.272461 53.813626, 7.256595 58.052452))'
    # bounding_box = 'POLYGON ((18.217292999999998 58.074616, 19.368973999999998 57.996821999999995, 19.080403 56.831705, 17.955171 56.910734, 18.217292999999998 58.074616))'
    # bounding_box = 'POLYGON ((17.43289 56.76217, 17.428176 58.121764, 19.704914 58.121213999999995, 19.713487999999998 56.761683999999995, 17.43289 56.76217))' # Gotland liten
    # bounding_box = 'POLYGON ((17.387726 58.440129, 19.877487 58.278389, 19.44107 56.59735, 17.064892 56.761131, 17.387726 58.440129))' # Gotland stor
    # bounding_box = 'POLYGON((9.08 60.00,16.25 59.77,17.50 63.06,21.83 66.02,26.41 65.75,22.22 60.78,28.90 60.82,30.54 60.01,20.20 53.57,9.06 53.50,9.08 60.00))'
    # bounding_box = 'POLYGON((10.2189734 56.50772281, 10.03165871 56.67213139, 10.1820399 57.06664644, 10.20249456 57.39751026, 10.41071944 57.65087635, 10.38127096 57.636289, 10.30543239 57.60604373, 10.20618503 57.57650816, 10.06861607 57.55773213, 9.96752988 57.52072436, 9.8588782 57.38798308, 9.63730005 57.20106113, 8.93173542 56.97892744, 8.59533939 56.92930122, 7.18433627 57.96407688, 7.08268121 57.9913456, 7.25300076 58.10754509, 7.39376379 58.13139782, 7.95633454 58.29177664, 8.17311256 58.23834854, 8.71685032 58.53260663, 8.92806793 58.70069814, 9.02480569 58.84259646, 9.62198609 59.26292051, 9.99148808 59.25843464, 10.11171904 59.67180963, 10.33461353 59.95988803, 10.89363381 59.98373078, 10.90699464 59.86925977, 10.93091681 59.6572801, 11.08826417 59.54809098, 11.3525491 59.3149257, 11.66116236 59.059384, 11.96583439 58.60918516, 11.98229038 58.58454188, 12.05437111 58.4250959, 12.09174278 58.16766937, 11.98575632 57.92036282, 11.91629272 57.90747943, 11.8069627 57.89041605, 11.84936519 57.84807786, 11.95524266 57.73050707, 12.06723593 57.61955545, 12.15145091 57.5284425, 12.2484656 57.36894072, 12.4563314 57.01221529, 12.55123631 56.91996875, 12.69534534 56.85376453, 12.76892283 56.71937922, 12.98414456 56.66404532, 13.02910374 56.52057839, 13.01288363 56.42073558, 12.99747827 56.28182478, 12.93345003 56.24049572, 13.10370597 56.05201127, 13.67343252 55.69825397, 13.97759543 56.10226798, 14.82548514 56.45393739, 15.83450019 56.7769963, 16.246068 58.22378162, 16.22662479 58.40619282, 15.77034893 58.70317421, 16.4290818 58.80423796, 16.94532453 59.14260512, 18.15750534 59.6734719, 17.70536994 60.04549503, 16.78231868 60.42013771, 16.12233842 61.26635535, 17.89440417 63.41548383, 19.20517959 63.96027974, 20.42202268 64.88498884, 21.61353594 65.91691615, 23.35623948 66.03537027, 24.91569643 65.82411919, 26.00648129 65.46699965, 26.01773296 65.14410573, 25.50190706 64.70750106, 24.55213618 64.26237458, 23.20086188 63.54758885, 22.33399259 62.56093236, 22.43085899 61.43592589, 22.35944672 61.09644415, 23.03947256 60.55822339, 24.21394668 60.60357474, 27.87083557 60.94223309, 29.87417924 60.80196558, 30.59630593 60.42111339, 30.56064783 59.42840986, 25.51836451 59.17165951, 24.38648751 59.02280838, 24.28928082 58.71998392, 24.69190008 58.48636557, 24.760162 58.06903004, 24.64376175 57.68767938, 24.50605721 57.20475952, 24.07976879 56.81019688, 23.57157384 56.77440459, 22.90345221 56.98593784, 22.06861242 57.373487, 21.9069004 57.16437264, 21.29249786 56.56470965, 21.4409455 56.03266306, 21.69890805 55.44939994, 21.41946517 54.75445018, 20.25487778 54.32344532, 19.74336696 54.07875939, 18.42975639 54.17164587, 17.3189573 54.09948118, 15.55442183 53.89203902, 14.15164747 53.72121111, 12.37765612 53.77483867, 11.1031179 53.80003403, 10.21064683 54.12708914, 9.32351169 54.57378705, 9.06580569 55.17685152, 9.47021375 55.76996609, 9.90061592 56.27126409, 10.48715798 56.43723051, 10.2189734 56.50772281))'
    product_type = 'S3OLCI'
    max_returned_items = 1000
    
    # url = (
    #     f"https://catalogue.dataspace.copernicus.eu/odata/v1/Products?"
    #     f"$filter=contains(Name, '{name_contains_1}')"
    #     f" and contains(Name, '{name_contains_2}')"
    #     f" and Collection/Name eq '{mission}'"
    #     f" and ContentDate/Start gt {start_date}"
    #     f" and ContentDate/Start lt {end_date}"
    #     f" and OData.CSC.Intersects(area=geography'SRID=4326;{bounding_box}')"
    # )

    url = (
        f"https://catalogue.dataspace.copernicus.eu/odata/v1/Products?"
        f"$filter=contains(Name, '{name_contains_1}')"
        f" and contains(Name, '{name_contains_2}')"
        f" and Collection/Name eq '{mission}'"
        f" and ContentDate/Start gt {start_date}"
        f" and ContentDate/Start lt {end_date}"
        f" and OData.CSC.Intersects(area=geography'SRID=4326;{bounding_box}')"
        f"&$orderby=ContentDate/Start desc"
        f"&$top={max_returned_items}"
    )
    print('Complete url:', url)
    print()

    return url
        #  and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq '{product_type}')

    # return "https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' and att/OData.CSC.DoubleAttribute/Value lt 10.00) and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S3_OL') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-30T04:00:00.000Z&$top=10"

def id_list(request_url):
    # get list of product IDs
    response = requests.get(request_url)
    json_response = response.json()
    # print(json_response)
    products = [product['Name'] for product in json_response['value']]
    for product in products:
        print(product)
    print(len(products))
    return [product['Id'] for product in json_response['value']]

    # print([json_response['value'][0]['Id']])
    # return [json_response['value'][0]['Id']]

def get_new_access_token():
    url = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    config = dotenv_values(".env")
    
    data = {
        'grant_type': 'password',
        'username': config.get('USERNAME'),
        'password': config.get('PASSWORD'),
        'client_id': 'cdse-public'
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    json_response = response.json()
    
    set_key(".env", "REFRESH_TOKEN", json_response['refresh_token'])
    
    return json_response['access_token']

def request_access_token():
    # If refresh token is not in .env file, get new access token and add 
    # refresh token to .env file
    config = dotenv_values(".env")

    return (
        get_new_access_token() if 'REFRESH_TOKEN' not in config
        else refresh_access_token(config['REFRESH_TOKEN'])
    )

def refresh_access_token(refresh_token):
    url = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': 'cdse-public'
    }

    response = requests.post(url, headers=headers, data=data)
    
    json_response = response.json()
    
    print(response)
    return json_response['access_token']

def download_product(access_token, id_list):
    for product_id in id_list:
        if os.path.isfile(f'data/{product_id}.zip') == False:
            url = (
                f"https://zipper.dataspace.copernicus.eu/odata/v1/"
                f"Products({product_id})/$value"
            )

            headers = {"Authorization": f"Bearer {access_token}"}

            session = requests.Session()
            session.headers.update(headers)
            response = session.get(url, headers=headers, stream=True)

            with open(f"data/{product_id}.zip", "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
        else:
            continue

def download_product_test(access_token, id_list):
    for product_id in id_list:
        print(
            f"https://zipper.dataspace.copernicus.eu/odata/v1/"
            f"Products({product_id})/$value"
        )

# config = dotenv_values(".env")
# print(config['REFRESH_TOKEN'])

# request_access_token()
# id_list(request_url())
download_product(request_access_token(), id_list(request_url()))