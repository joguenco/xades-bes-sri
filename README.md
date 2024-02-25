### 🧾⚡️ XADES BES SRI

An implementation of xades bes sri python to sign XML documents for e-invoicing.

### ⚙️ Technologies

- lxml
- cryptography
- xml

### 📦 Installation

```
pip install git+https://github.com/jsonfm/xades-bes-sri@0.1.0.1
```

### ✨ Read .p12 file

```python
from xadessri import get_private_key


with open("/signature.p12", mode="rb") as file:
    p12 = file.read() # bytes


p12 = get_private_key(p12, "password")
print(p12.key)
print(p12.cert)
```

### ✨ Sign a XML

```python
from xadessri import get_private_key, sign_xml


with open("/signature.p12", mode="rb") as file:
    p12 = file.read() # bytes


p12 = get_private_key(p12, "password")

xml = """<xml><data>some important data</data></xml>"""

signed = sign_xml(p12, "password", xml)

print("signed: ", signed)
```

### 🔆 Credits

Project Inspired by [`xades-bes-sri-ec`](https://github.com/alfredo138923/xades-bes-sri-ec.git) created by [@alfredo138923](https://github.com/alfredo138923). Thanks.
