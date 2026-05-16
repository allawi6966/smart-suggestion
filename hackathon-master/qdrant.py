from qdrant_client import QdrantClient

from pathlib import Path  
from qdrant_client.models import PointStruct
import importingData as i

#!!!!!!!!!!!!!!!!!!!!!!!the data to insert should contain "id" "vector" and finally the "infos or payload" !!!!!!!!!!!!!!!

#connect to qdrant ***************
client = QdrantClient(
    url="https://4797bc27-a78a-4d46-bb0d-9d87dc8ca35e.us-east4-0.gcp.cloud.qdrant.io",
    api_key="kkkk"
)
#prepare product**************** (example of a product)
products =i.read_products("laptops_cleaned_v1.csv")
print(products)

#insertion*******************
points=[]
for p in products:
    v=i.prepareVectore(p)

    points.append(
        PointStruct(
            id=int(p[0]),
            vector=v,
            payload={
                "title":p[2],
                "price": p[3],
                "processor": p[5],
                "graphic card": p[14],
                "ram": p[8],
                "os": p[16],
                "storage": p[13],
            }
        )
    )
client.upsert(
    collection_name="finmatch",
    points=points
)
count = client.count(collection_name="finmatch")
print(count)
