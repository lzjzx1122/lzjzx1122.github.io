from scholarly import scholarly, ProxyGenerator
from fp.fp import FreeProxy
import json
from datetime import datetime
import os
import sys
import time

# --- 修补 free-proxy：代理网站表格改版后会拼出 "ip:port:HTTP"，这里去掉多余的协议后缀 ---
_orig_get_proxy_list = FreeProxy.get_proxy_list
def _fixed_get_proxy_list(self, repeat=False):
    return [p.rsplit(':', 1)[0] if p.count(':') >= 2 else p
            for p in _orig_get_proxy_list(self, repeat)]
FreeProxy.get_proxy_list = _fixed_get_proxy_list
# ---------------------------------------------------------------------------

scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
if not scholar_id:
    print("GOOGLE_SCHOLAR_ID secret is not set.")
    sys.exit(1)

max_attempts = 5
wait_seconds = 60
author = None

for attempt in range(1, max_attempts + 1):
    try:
        print(f"Attempt {attempt}:", flush=True)
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        author = scholarly.search_author_id(scholar_id)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        print(f"Attempt {attempt} success", flush=True)
        break
    except Exception as e:
        print(f"Attempt {attempt} failed with error: {e!r}", flush=True)
        time.sleep(wait_seconds)

if author is None:
    print("All attempts failed; skipping update this run.")
    sys.exit(0)  # 不生成 results，workflow 会跳过 push，保留上次的数据

author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}
os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as f:
    json.dump(author, f, ensure_ascii=False)
with open('results/gs_data_shieldsio.json', 'w') as f:
    json.dump({"schemaVersion": 1, "label": "citations",
               "message": f"{author['citedby']}"}, f, ensure_ascii=False)
