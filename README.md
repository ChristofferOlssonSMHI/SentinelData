# SentinelData
A script that fetches satellite imaging data from the Copernicus Sentinel missions.

## Basic usage
You need an account on dataspace.copernicus.eu to access the API.
Check required Python packages in **Pipfile**.

1. Enter the username and password in the **.env** file.
2. Change variables in `request_url()` function in **api.py**
    - `name_contains_1`: Uncomment **S2A_MSIL1C** for Sentinel 2 and **OL_2_WFR** for OLCI
    - `start_date`: Enter date in YYYY-MM-DDTHH:MM:SS.000Z format
    - `end_date`: Enter date in YYYY-MM-DDTHH:MM:SS.000Z format
    - `bounding_box`: Uncomment relevant bounding box
3. Make sure only one of each variable is uncommented (otherwise the last one will be the defined)
4. Start by making a search to check if the wanted product results are returned
    - Uncomment `id_list(request_url())` at the bottom of **api.py**
5. Download by uncommenting the last row of **api.py**
    - `download_product(request_access_token(), id_list(request_url()))`