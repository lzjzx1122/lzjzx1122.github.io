from scholarly import scholarly, ProxyGenerator
from fp.fp import FreeProxy
import jsonpickle
import json
from datetime import datetime
import os

server = "zxtw02.mutdot.link"
port = 22749
cipher = "aes-256-gcm"
password = "7762614b-9bad-435d-86e5-aab66a4bec6e"

# 构建 ss 代理 URL
proxy_url = f"ss://{cipher}:{password}@{server}:{port}"

pg = ProxyGenerator()
pg.SingleProxy(proxy_url)
scholarly._ProxyGenerator__proxy = pg

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
