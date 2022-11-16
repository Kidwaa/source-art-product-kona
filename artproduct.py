payload={
    "InventoryProductId": "07096bc8-a168-4bd3-9dbb-9d66727f5d81",
    "Name": "Structure Combination 2019",
    "Description": "The painting focuses on discarded objects in a waste disposal plants.Through this, they contemplate their own anxious present, which focuses only on the present situation and does not look around, and the absurdity of the times that encourage the omission of relationships.",
    "ModelName": "1970",
    "ModelNumber": "MW2699",
    "Vendor": "Artmining",
    "Price": 5000.00,
    "Tax": 25.00,
    "Vat": 10.00,
    "SupplementaryDuty": 10.50,
    "AdvanceIncomeTax": 12.50,
    "RetailPrice":9000.00,
    "Currency": "USD",
    "PackagingSymbols": [
        "Pack-1",
        "Pack-2"
    ],
    "SerialNo": "SN:1234567890",
    "BatchNo": "Batch-1234567",
    "ManufacturingDate": "2022-09-09T06:32:04.362Z",
    "ExpiryDate": "2022-09-09T06:32:04.362Z",
    "RestockDate": "2022-09-09T06:32:04.362Z",
    "Quantity": 2,
    "ProductSize": 1,
    "MeasurementUnit": "Piece",
    "ReturnPolicy": "No return after sales",
    "Warehouse": {
        "Name": "Arthouse",
        "Code": "12321",
        "Address": "Address",
        "Latitude": 50.233232,
        "Longitude": 50.233232,
        "InventoryId": "IVIVD308D283",
        "Description": "",
        "ZipCode": "1675",
        "MetropolitanCity": "Seoul",
        "SpecialCity": "Seoul",
        "SpecialSelfGoverningCity": "Suwon",
        "Providance": "Providence",
        "City": "Hwaseong",
        "Country": "South Korea",
        "District": "Jeju",
        "Town": "Yangju",
        "Township": "",
        "Neighborhood": "",
        "Villages": ""
    },
    "Brand": "Kim Hye-Ryeong",
    "SubBrand": "",
    "Colour": "",
    "ColourFamily": "",
    "Sku": "SKU-1234",
    "Specification": "",
    "ComplianceInfo": "Complient",
    "Miscellaneous": "",
    "Contents": {
        "A": "0",
        "B": "about:blank"
    },
    "MaturingDate": "2022-09-09T06:32:04.362Z",
    "MeasurementValue": "1",
    "SizeUnit": "Piece",
    "CostPrice": 4000.00,
    "CountryOfOrigin": "South Korea",
    "Language": "en-US"
}

import requests
import json
import random
import uuid
import names

def get_image_data(n):
    p=1
    arts=[]
    images=[]
    while p<n+1:
        try:
            url: str = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{random.randint(1,482652)}"
            print(url)
            request_result = requests.get(url)
            request_dict: dict = json.loads(request_result.text)
            if request_dict["primaryImage"]=="" and request_dict["additionalImages"]=="":
                continue
            else:
                artist_name=request_dict["artistDisplayName"]
                link_to_page=str(request_dict["objectURL"])
                dimensions=str(request_dict["dimensions"])
                art_date=str(request_dict["objectDate"])
                title=request_dict["title"]
                medium=str(request_dict["medium"])
                description= f"Painted by {artist_name}, {title} is currently displayed in Metropolitan Museum of Art, New York, NY. The dimensions of this painting  are {dimensions}. It was painted in {art_date}. The medium is {medium}. Visit {link_to_page} for more more details"
                new_payload=payload.copy()
                new_payload["InventoryProductId"]=str(uuid.uuid1())
                new_payload["Name"]=request_dict["title"]
                new_payload["Description"]=description
                new_payload["ModelNumber"]=str(request_dict['objectID'])
                new_payload["RetailPrice"]=float(random.randint(1000,10000))
                new_payload["CostPrice"]=float(random.randint(1000,10000))
                new_payload["Brand"]=str(names.get_full_name())
                arts.append(new_payload)

                image=request_dict["primaryImage"].rstrip()
                images.append(image)

                img_data = requests.get(image).content
                image_name=f"{title}.jpg"
                with open(image_name, 'wb') as handler:
                    handler.write(img_data)

                p=p+1
                additional_images=request_dict["additionalImages"]
                n1=1
                for i in additional_images: 
                    image_additional=i.rstrip()
                    img_data_additional=requests.get(image_additional).content
                    img_name=f"{title}{n}.jpg"
                    with open(img_name,'wb') as handler:
                        handler.write(img_data_additional)
                    n1=n1+1


        except:
            continue

        jsonimages=json.dumps(images,indent=3)
        jsonarts=json.dumps(arts,indent=3)
        with open("images.json","w") as outfile:
            outfile.write(jsonimages)
        with open("arts.json","w") as outfile:
            outfile.write(jsonarts)



get_image_data(5)