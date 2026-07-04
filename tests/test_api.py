import requests
def test_get_request(base_url):
    resp = requests.get(f"{base_url}/get")
    assert resp.status_code == 200

def test_post_request(base_url):
    resp = requests.post(f"{base_url}/post", json={"key": "value"})
    assert resp.status_code == 200

def test_will_fail():
    assert 1 == 1
    # 测试 pollSCM 自动触发
# 测试 webhook 实时触发
