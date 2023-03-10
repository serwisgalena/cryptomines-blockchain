from __future__ import annotations

from typing import Dict, Tuple

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUWzGLmUq3RgS/u2oYomRSyKsXWwcwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDczMTAyMDgyM1oXDTMyMDcy
ODAyMDgyM1owRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAzB+IyNSmoJt99NpPQ2agYv/3Bxa70ZKHmCRHT6h2eNFg
87Mw6Dntpq8uS4zAa2pUohWNRPFrWLkHMxngQuuCJqfu7sqTJwwSNodYK6ajoidI
qKyZGZd4kj8AYhKe/2O0cefjWbc1leOzXwqtQSdlr65pXaJMWG7jckNGf8hj+Dfe
ZqJdonS9w6LYJPFH7l8njHaECLm6fWusJjq8nhVlAbbjetnl5wYsWjdJZCWfcSG2
PRrHncuPLSJVPn9Gdo/bqC+zQ3VJhXLELM/Fz10+cxWpaUvjEJEnhaRjAYsD6wk0
yBoaNXzVo3e/gsPcppG14dgFC+bdfFytDHMFqw2kHwIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBNwno+FoJnwcJpltsDfPnTYAMD
+9gm/dMBrwVtYZyB6OJKrOUYY49KA5p5/O06n0S7DOYKXVGZmXPownj9Hc1/0kUE
KKg3GTzekBIso91wUL9isR5eEUnLfnHwa1OAsu2ycv1pQWwsyFvcl8ttBdmYWN5z
3EgF3kDtIc0erz91hpkixev4ZpWQzf22UKhp58EehwODI5CRRJKeVUP/pMPkrfUm
58aU31u+rCSX+uJWH/wnWeE6WZDBS5/4abcY8KLnW+ArEXrZPpEqWWsuj0lWrM24
yyfyhCmRMmeS6XSgpitKZk6kWG0VUUF6NKSilGCYUD1tEKq89oUCdDoMqJIC
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAzB+IyNSmoJt99NpPQ2agYv/3Bxa70ZKHmCRHT6h2eNFg87Mw
6Dntpq8uS4zAa2pUohWNRPFrWLkHMxngQuuCJqfu7sqTJwwSNodYK6ajoidIqKyZ
GZd4kj8AYhKe/2O0cefjWbc1leOzXwqtQSdlr65pXaJMWG7jckNGf8hj+DfeZqJd
onS9w6LYJPFH7l8njHaECLm6fWusJjq8nhVlAbbjetnl5wYsWjdJZCWfcSG2PRrH
ncuPLSJVPn9Gdo/bqC+zQ3VJhXLELM/Fz10+cxWpaUvjEJEnhaRjAYsD6wk0yBoa
NXzVo3e/gsPcppG14dgFC+bdfFytDHMFqw2kHwIDAQABAoIBAQCP/GqLZ92GC0kF
L/2biMf4LaB+Ip4oDdmSC302BppTTTa7kRodpccqvgXFCyssWhwLHXLCQB29vv8C
H+2epuvvAqS7UrAMaipqxnv+hpSErHtHaECy2bMWTlSh2YrIkfdWJgGsZlzpN25u
y2Q9QmIrU7dFcleyRb4w+p2/Q4apLtUgx+IoJfwKq501LmdTT7/sUyRrg3wi+Dz4
pxrv/RdFbllPDww85vl5e6amwhcNHZ76KpV1aK7qqvhQ2OLkBvRe4eKAH5O/hHWM
tzDC/x5Bnn9O4n3mOh7aVAun+98x23KakPvqQBStkGAqUGQeWKI2tSRr8p+441xj
U+fLTy5RAoGBAOnI6XrnAVP2MaeeokiDNSCUGY5YhjLVX+FJZsvPLdoVKU+p59cm
CnSvjTQjfOSivkE+GvWQlPu2KQo/AchdP/NFZ/3VFzx8OE1EQgRhQ5frTTlWkB0V
2XGtvxhJvXRs9n8mwkMVGSmsIWqRkUteodfXne11uOJg3nmbL2jaH+f3AoGBAN+F
EYs1ofve+euarDRjRzQscFZd0XXHQ+ff/U26veGpsvgUIFb0ONLFWuvsPp5KrWUr
sMih0h2gjRTzmYlj/9CE/YQUXRDg7287dZYuFIEvmlCqw+X1+i8PXIA9PDlSloDE
jFnoa5uLIC+orc41KmzFXqxSZgYTG8ddqMHOcqsZAoGBAN4dzwbAF9jn3gF9jH4M
ext62lUN8mK1q6TmEk6thsjetiNEMEuPjvuSFzxkQzMPFGf0U7TgK0yDo7ZiapUt
U6cUWFsobC1BcFSo93gl2QyruPEzNzULH08MXrT6yo+lPwVLk+IcV43qRs1zhHHx
dR8Xcqq74G7kzjsHoCGkrA+9AoGAORteaBrDz/4gDDnwVVIoFwRjjy1ZHqZSiyOH
LBzR9p3Mw+UgfhbXjcIugKhTN04NDxQijqAJdthWM0wpphiOe0//FYe+X1mY0up2
GHCdfIQVARcgBdjamrtp/rmmcV7QZQXSdgYTuCHLj2GhRlX/CNtEXPKQbmzjZARh
4WJFmcECgYAe8b7w2RFkm4VvMYLOYOGuABJT9mpfEZpIuJ7/qtdM93IKh+ZdRKE9
ZyoWerb1TmY+Ug8ChwPrIadj2J1e6Ml/TqcufsMGKm6cMfg9Y+AuuGyd9ZOzYid5
IdfCNbUvD3PrrwClHqY2XEb4GkSbDwxLsguIq5IP92TCD8WJiOmS2A==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUSj1pdOwRwJrEORU+fqWLTHMZr3cwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC76QDovPz74lN1tpHAA/sXtUXVu3UiikJjnFpgUQIK44wX
+QSbiY3W4fvvmrDv2c283ZiH2td080R/sACUVW3o87hqYJI3aSsuoE0AtOkBjPbg
xvn4T9C0DpJQIiqhBWXBZ7JnLVcgihCblRd/LsjWQOB/G42VC7ikLe5zW5fto0DS
sTwFLmY6wKMmuSN0HoHvk/fv7YSTFKPNW6ofwwQ7gaeqwBRUsRqCXoREUe0wLvUP
7HRfJ6+mDn3Yd+upymCuUOhXQNTjD5mfiijxawq8MYIO3niObValyqNU6mHUyaOj
4abGws3Y8Mju+5dlHmQmBBL/HXme1Irw/Ta4G7TnAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAWfUyskkstyDNjFG9EseOZ
YPvtjkjbrlk+IKPfACfpiwAGsEMYS3P/GVQXkA/VYAUiaqhZqJvGvb7zceXKDqcD
3/UiId3YtlcZYzaAcAbf7xmPkmb/kMjtsmao17lm//YldbM9zp9kh6JJS+8Gh1cp
Q4c4pR1NPS5/m/dPHNe5K/BrAQZUEV4TBlfEUSkQ9vYJeOIekHGWVTFOgJ9mfML5
aP01qLcDOvTwV9BewpjHL0RXPqn7w9v4nUQa9Tqla5ce/OBgAOfB9xO2+9IpWI8a
NCigB+qkSal87TL2/jGgry1aPpT5SHP2iGaLYbG5//Z75rTZzGHQJQxgJeR5zm+7
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAu+kA6Lz8++JTdbaRwAP7F7VF1bt1IopCY5xaYFECCuOMF/kE
m4mN1uH775qw79nNvN2Yh9rXdPNEf7AAlFVt6PO4amCSN2krLqBNALTpAYz24Mb5
+E/QtA6SUCIqoQVlwWeyZy1XIIoQm5UXfy7I1kDgfxuNlQu4pC3uc1uX7aNA0rE8
BS5mOsCjJrkjdB6B75P37+2EkxSjzVuqH8MEO4GnqsAUVLEagl6ERFHtMC71D+x0
Xyevpg592HfrqcpgrlDoV0DU4w+Zn4oo8WsKvDGCDt54jm1WpcqjVOph1Mmjo+Gm
xsLN2PDI7vuXZR5kJgQS/x15ntSK8P02uBu05wIDAQABAoIBAFN0LfUvSePMJmjX
BnAS1Ic4+KTtth367XUz0WeJUrDnUiarb4JsWtQeVTeaqg472wWQHNfpN1s3Vyqm
TfuS3VdiNnr4HLgDOyxgARLZRcpsgpBdjlLbj8MH3a89HVWaAhEdLrxoBJPs/Wc7
lc3kR0nwUkPhRsX1CLHRvF77RMRCwuUgcftPypGtPCBLsk446d+7VRzdQwmLp1jf
D75Azy3JsNI47e/KVqSMpTU3LXBTBq4S89AhQACRhABdPNsWXcEotgRZUN0Urn2W
A8oBxr0L0VSLy/4yyAbSHvoD470r1lsakgs0vwJLdDuubpwnm5I2gULgb6pfJWHw
YRg7v6ECgYEA9IN4w4fWt0rhqDL1zY4zZZX+7lqxkgPYFnDGwJP4uRNWjAK4zfkZ
jr9LRvAxLOqkSntGQsVZRglXzIw84TYfrrzx+DKoQlPbhAaJSzwKz5a+NbWsnNQF
qQS2ut5ly3kvpt/Jo4zJyRJleDqBRqabOnnW78PaakkW2470Yzs4mb8CgYEAxLzR
SlnUGsqUgJOc5OmjDsOb/vlSrP+DVHxY4wafV3cbzHIG0OouYkZhNFdF97Ryst+2
ct77WydwhH6wHW304tCByvbQFCFaOaOWsWobvkLthC28QjHtnPlh9ea0dErk1zgC
b6QXbm9Olj/TrKs/mUDIij/Ek6V5JzhUH6IjHtkCgYBJ306lBG1Cg0UZ5AuPRt8Q
WfjjWlM7oh2u6fOiSxJiGA2Vz1y2HgQytGixze+NenaYahYYJjeKiVgVXGkoQYng
6QTRz7w2Dc/MW40vRbyeaxScdX7pAsWTAvGSE479omdbK1FoMCjmrsApSsOz7LIJ
QLZHSgy6/8oAG3iKYmH/UQKBgDz79rhgbgI8B5pvp3PCBJyAACwiZwFfVvtqbDc7
h0sajdBrDDfYT7aA8ILEBtlI40EVXb3v5uSTrio0By2oNv/T+FfM+CU1TX2OexjV
tnHc1zlg3/l49pnxJ++MqyVdTeB06TRoHidKc4bZlCjzEIzV6xQHvkyyP4Lr0A/a
N57JAoGBAKHqP0V/qOsdB5vjFaI+mgRZWnYz9V8w3iJ1y0tYOOgZ4LvuCZcQG9P1
8PrZ5KKcUCxlpBXljEWery2Q8c8FZWft9hEcklYCNRz7q+TarnDYOvzLOSmQkYCG
e7iszMYB+s4lVAYr+vd8bGY+e9i/C6S1hM4ApT1F/g3/VU0rBvyR
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUU6xhWBWAz/LanKKEiMOFsRIw0mAwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDC7U3QVRjBkgeNtXO74IHz9vlkL0MA1DWGglxzPDTUArgx
qaOySonFeh5kjMhYqRNulUsdCoRyNIUz02cvg0UAE323BkJUPJBaz/F+jS9rX/f3
KLqbbsxDc2l+R3uz+MqD6DAiuBJuqD/273oIdGmhp3j0be2/DGCPpfTeh8h9lM8u
eIvBClLWPsVaZAD93ahflId1XIji+D3xsRao6ss2zWkYtQC33giSTC30+DVmVbJG
wsTGkEki6SZa04m8nrCcMAMyujspmrO3Z9ybDMq77HzF334QSkG7M5Jl0Z4lA0R5
g25Poi3Ej0GBU4nPfJoChSnelV4emG6G2FxZfXZHAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB80O3SW7hciWlkcRKrl6tL
iBVLFxobmIVUVjSeXfSx1fiVzdSoPKy5S1NLzisGqPkFQnngz85CWb+frFUSiCQw
jKepxTKluiWzW2IUTgu6lwPFcupd2EfTv3RLiN6NY/ivjYKtMvOGP7c7WFf21r3B
39SmTfwJoEfJAkRmi4bTOwTjVC1fV8j3idyjWudvEtH/QdOIMp7+CdDJAa+loPCT
V5jXF2gVyaLZJkilr2ZGj9+uy2w6LGyrxU2LKvuaMzFWRC4X8EmnFuO2o0Dbss7Y
zSofQc72b5XtaaTkfHaGWzLBeebu8ICo5zJwCzMkK2fWp4tAegetnlUKlEWpvT2Z
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAwu1N0FUYwZIHjbVzu+CB8/b5ZC9DANQ1hoJcczw01AK4Mamj
skqJxXoeZIzIWKkTbpVLHQqEcjSFM9NnL4NFABN9twZCVDyQWs/xfo0va1/39yi6
m27MQ3Npfkd7s/jKg+gwIrgSbqg/9u96CHRpoad49G3tvwxgj6X03ofIfZTPLniL
wQpS1j7FWmQA/d2oX5SHdVyI4vg98bEWqOrLNs1pGLUAt94Ikkwt9Pg1ZlWyRsLE
xpBJIukmWtOJvJ6wnDADMro7KZqzt2fcmwzKu+x8xd9+EEpBuzOSZdGeJQNEeYNu
T6ItxI9BgVOJz3yaAoUp3pVeHphuhthcWX12RwIDAQABAoIBAQCrGAfY+RiFr1uZ
8s7m9aSbMwir+x/gtmNU8U+chhgIj2qFjNT2RZ6wCwRqVXf0+lLoGXqYvwaKB7dz
SfekKKCD9Je/8mp97br3OtZJsjsREGdiNgm1LId2HPNXt/7IdXOsXD0D/HWRU3Tx
ljmS+jtNfOYaBfNMYdzPuWc5fA1qy472ANA9x/iENhce/ubi9AYbo26G4IoIt/W9
x9A1Ogsd00w3rV7rFnH1/UBk9B5exsaCG6GdUvUpfp3dffDuBnIJ50XHZzO1hm6w
KgKB7ByXZUDXRDaQeZyzfsXhq6wleMMnABqCrGywYbTf1IIC00LJR22jNywOrqkY
YM7lEgLBAoGBAOCxtWafc+YBay8pZE6bcZ48gwf6oeja5U0SLiFeuCa6746s3BiL
Phv1pawYg48eXfA8nsySmuedFBKXNBJuuv4a0n8NSGa85lXQQvfxu8tCVTYx3mPC
K7HE1bPWB2/ZSOFcouiB+PEeKSN8W6WiwqTe+ytR5KpEocX4v5dlvzSJAoGBAN4V
3zm3OV4gb0eO8eR4Di/FNpYPFsKqzeWLMqXWkY6tigkndy8p6bAjmvYhE8cuyq3w
JCGIgxFls7hxdACbBm1hp8jUVnSUUhXHRticOIcfb+XzV9ukQkjFKpPrQ3h39c4U
58djf8NHAlFZ9pVoNmq2ulRgIUx9MGOPx4cRCkBPAoGALAyqs2OvJPhCOwyyTXbL
32mdhoLsGupO6b0WrhQTpgQf0qiwvV8O3gxaXlKv9+7MG7zGpPRYye9RcBOUccij
gA1iFuZTu1BtF4Wsm08YsdBfRDCimIwIZOFhw8/BxXujfgrbJRnV4+81wW8vyFkQ
L6JHO0bivT6XOGh7pwKbaYECgYAFCD/XofQ10sxStcV7ZNEFehWDjvH4FUC3G9FY
+qSvs/T1wiQsOGnoKNZhD1zQXZoQGOnorJwzr7dDzaZQQTMDFXxky5Lt71Jw1eQg
EmIhha/WaQ4rluw9k+IkGeecejNiqQybcwC5HwnJaB1zQzpAbsWIFemLPybyipZ9
1AAEdwKBgFRuWL0QE+80c9oDMdGryjFoOdnEb8ZyNuJ4zfE4sO9zG9ijiuuDm6Zb
qKSF5Sp76PEG0wpESnDraGbCBkD8icqOnmCICdZ/rl/o5dzqR1FdakY/Tst/Lcxm
hcKNbEQjbJ5C+epayOgkdZkE+Dx3TMJvO9awRjXP3rGzzV5ri71B
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUE3WYHLRte9HfED08IQ/HsX/LM78wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCtro19tmukTk4ClxM7EsqL4nEG8deswAwgpxvHAqwruOLO
fn8VrWOruj+WCLwPiFulAFA79eX6qoUNj+KskOqhseLPQgw/PPXNVmFr4pCIhUJR
m1RsSnN8/rbQwGwqaZTNv9ziwPY9N+sRAO+dNK9JWaRQYnUYM7aVO7ze0T5TAGZx
Xc1RnRH4z66mvyK2o+RxGrm9bRRJckXHewcpmGKzWlJWBeUpgTMb7i32y83sfR4K
hKCee7YQqb4NBO+Xi3+NWxks62qjrInupxE3x7bm/uBRFGxxQEko4Nuy9gIs9as3
nJKwxxb0t1k0DPfZVBMOa6rmsXw2XAT7Gy2Mu+tfAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAy6Rn3XCcZIwdoTlqcXGTq
SxOJ2YD8vluqyGdk7oF8sv7hprQy4fiuIKgVM6H0j6o/ITZeAqZfYOJ7XwmbrhBn
XBCjWqa5GLIqjG/SH9qjxnqI7zPkVwyGXfUEUu2q934fq5hZ3/KC+9mAqOXyYpgI
pEuJlgqP8F1mc/QoSgbEldCJonGFnJo5tXx5p9a7lTz9y9EUFBR74hPfpUKWilGG
9YZ0UFnsV3NsAyngQ5/SeY1/leBWCXy6YPpVZZD8l5vOvRYeRKzZbPhJnbL22ba+
rUZ/b1sBH0+aW7wOGfR/dQgIoGgHjgpztLm4dmdwmJNRI5J94yQSJLswgTbvl8ka
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAra6NfbZrpE5OApcTOxLKi+JxBvHXrMAMIKcbxwKsK7jizn5/
Fa1jq7o/lgi8D4hbpQBQO/Xl+qqFDY/irJDqobHiz0IMPzz1zVZha+KQiIVCUZtU
bEpzfP620MBsKmmUzb/c4sD2PTfrEQDvnTSvSVmkUGJ1GDO2lTu83tE+UwBmcV3N
UZ0R+M+upr8itqPkcRq5vW0USXJFx3sHKZhis1pSVgXlKYEzG+4t9svN7H0eCoSg
nnu2EKm+DQTvl4t/jVsZLOtqo6yJ7qcRN8e25v7gURRscUBJKODbsvYCLPWrN5yS
sMcW9LdZNAz32VQTDmuq5rF8NlwE+xstjLvrXwIDAQABAoIBAQCGdblilsSU6m5o
gO9Jb43RaBha6QYw3mlFKjpOAtqp6rPka3gVnyunukQZ8l8to0JX5ns3QHKwci0Z
x8gUEwki72WJUTfMCXS+aF55uGhu2MP0C837HFR2c3ey+xWCbETgWOY3wm2gDVd1
zYSz7yK5JaYY+XBvsTFsLVhWJCYc+M7Vmt5BNMlvWJcPiKaI3TGqTrnV171WsZ5o
ovZalkyUTrVOFl8q6Aqt/3ocTXbLx8m6cLpweW2GLjJgwumU3x3RA/3KcBro6SVF
AeKin7PXPjkajrVkKa3ZAZAaycBOAUL3zau3FujKGYrhXWtQZDLJcZx2eAgZcjBW
WkupOC/RAoGBANSpcjOj3QNSIUVW5yCt2HwubxStUyHVB1rC67SvO4G5abNLHvfp
Pb7rO28tNxBuj7VWJOYxnMt2WM5zMZnsdmICr39bKsiANw5Mt4cAFQrBsZi+a5w4
gHekXZQUpj9n7P6ajrYwW/3h/Ced5kJqj9aGZgeyKkFip4aGuljhKAVXAoGBANET
hTw+T/H4mNBkuBBQ4LUNZt360OVEskH1LczjHeiWTW63cvJZyxZkTdozkQqQCH8U
rr0B8xVzxiXph6Nuvkv/ANZuKEivO4xSnh7UM5X8T5VsSIhwLNbY7yZQxBuDbYLi
xXqsVRRV1NNZjTzMOBVJytN/GaF/f0OA+Vb9uz05AoGAaACyhETISt54vQOCJ349
2IWQ96jIdkxLu3yGb6gfTxMReYjsjUu5UcyTFY0kV9nqWEHX6+gpiWvIhLbbdC6r
usUbdQpuAv6Jbmnge5pzr/4IT+4YjJ8pXNm6ljf/EhVOVznZP4qpAqHpgqp7ONIK
pFy4O11LwwxvZ6AuNFdxDiMCgYEAtVPvvvLwFRUdO8fOl1/9syjfaXApkl5FF81T
npnvi5QnrfluuN/FsjLmDnOgvH90zvqaHhS9xYI2fRUP7V+TrYeJK3A4gelwhN/2
gRhbcR51y0sxkRtw2BknOJzdqFsRNG4HBcDGvS8/uNm3E96uWVA5l7po+VcBggMu
vRKsPIkCgYAkA1YumgHT6vHTfwHSKSncYl8QM9Qh9EyZ4qFrTkEs+S7j3Hcqu7Ln
0Dj/FX3oFpPJj/qjNJeqsosi39vRMeEMvgfSOw4F7hoihT1Po7gBRgTiEFhtbyBS
xztRjI+2dhPGEcnCNUUZOKsXDo0VATSVeECOLHKqlNKANIx5c6g4nA==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUceygR6j1lNbh5j15q1GRBLaqODwwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDXxvUiBZjy1HMvZuOEeXSx6ByH7NrLbdQargaCuhpNP1M8
B4Be5t+5UJK40oDpMrVNg5hdqIRGn6kH9j6sA/mNDdHt1d7alAIAAljSe1RXnk/o
r2znyAjnA3UpkQl1JT4pyPXfsE8ucIq4XcC66MWtKj5mVH2CWbPqbJbVqtvwO2eV
MC3G4x7gj3LCPxiTmGyt2v730lsMeShYN/H2ocZ1ZvFKDBInK7iLwycaM7GGaRkf
oXYodbVwZydd0DLMuumqml+6U52tWtB2mFYJeKEAauJr2h0n/QdBFRzVpDjRXU7/
AIGzHl6tpQys2fhFa+wAY4n4oSu4CHTsIiZLKWSrAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBZWLumeHQXOK9mju8KhC05
FvTz0X6osRIIu+B85ZBh4xh52xpaIe52xeNAzZ1CH7IKuLoQdSROWhLOEQu4YUGX
KvN+2/8D60M1WXtAXmQwX27ZNEVfCsveLVqV+KD3Eb6y7YsXzS+GneQInlP+b3+H
3YYPfhKwqUjYcSsj9A3u0iSu6NM8Iefwl89NYN0Rk4//dM0blK17gcT2TiGNJB5z
uEXtvL3+78oWgY/nNbqcf0yHa7mjMwebnU5RQRs0gYIWnlGmqfctwSFgEw/V8Kq0
Pgau9uqub3bfFJ+bV4wScRnOkjq1h4KkQkHSqLOVPRK86fa57pQw4FOQyykvzD25
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEA18b1IgWY8tRzL2bjhHl0segch+zay23UGq4GgroaTT9TPAeA
XubfuVCSuNKA6TK1TYOYXaiERp+pB/Y+rAP5jQ3R7dXe2pQCAAJY0ntUV55P6K9s
58gI5wN1KZEJdSU+Kcj137BPLnCKuF3AuujFrSo+ZlR9glmz6myW1arb8DtnlTAt
xuMe4I9ywj8Yk5hsrdr+99JbDHkoWDfx9qHGdWbxSgwSJyu4i8MnGjOxhmkZH6F2
KHW1cGcnXdAyzLrpqppfulOdrVrQdphWCXihAGria9odJ/0HQRUc1aQ40V1O/wCB
sx5eraUMrNn4RWvsAGOJ+KEruAh07CImSylkqwIDAQABAoIBAQDOxAgCIfr+NjZq
Jd2/A+Oe1xz/4yeF6ChnqHr0qgCqJRRNYaLRTcr0eREfqhd9Xun87S0EEocuZbBD
wOMtUmG/mI6hqV9zdIC2IYmbqDKaA0nvXqqtMDHXrKiIvEKjzpxSzg9N2lUF2zIS
mUQl1wgVd3Vz+WKLlgmhiYzAEonPGFm24kDAckP/2TFKjQA8CqZhd+QQfq/EcTuP
khKVAOvp/7e50PCq1TegjEGmTEgr3T82AJPKOzM+9flicYC3KTFkDv4XbyR+7A6h
ZRRIpjcj6zSzS6pgkkKBdqD8gPw2cjztb/1aV/eBa+vnqgUpNUib+DCcNImuGFhR
0yp8s/UBAoGBAP6q0rXe4vMNCfaMeQMJd2medfH6+zobCiRD1nAJHHTqNSJLsH9Y
TgBNp6Tg+OpginccSj4NYryYz5TXw+xfOjgm4Y8IXK/mNc5B3hrQwVZynk63hP75
tyv5OHDsjHx0zgRndFAkFbAOswenneMULKHbOB/7PjhQ3lo+nBx2MWfJAoGBANjo
CJUMxit91HcsMWWpZD82JOn+da8/LOE/TqY6Z4IGayHrFOTw43MEf/FrEX9//FRR
vVF/puhuBhdZMga8HwUTiXRg51ts8GI5eT8DhDj3tiudX14Moa2LVJtEEhdRN541
h7blwjvbAHHc5xw5KW666w2NDTlPrQuzSBd2ywrTAoGBAI50l/HMgD9dZ9lWssqU
HQwj6+40axwRzBaFLAr3zcdIy/gnRs+1Ycyho8mDXzocTthaJt2XN0gwYs3r9Fjg
2/xVI4+TKeXrbOW3yrpNVBk7fHqkBe1rWp9qhbwFVoC4BhZImLPLu6YEUvlRNey0
eFMCAd9B94ghFIB+zWzOYMyhAoGBAJv1aoZRIwQOe4AcpH/mZhAVTEF7Fv8ku45R
yKk5AUe6eblvoBxlIAWJTL03MOOuEK5H/4nj8QzaX0LWfWPeS6eIvqKRMojIMadO
j+FBFAcqBTAi/XlQN8fikLj7Hs7pNMZq0uQtG5WSCCXWoc3nQ+U8PNoHe2Sj51as
V7+XSLLFAoGBAITi2BRO8OjXXxaOUMK8AATVR6WAH7kC6GXtqUDZFskoqYYwK/bG
/orTfIG0f9YFAid4XZMIyW8VA4d3kaZ/v5OOKMV0GVKcNZpH1NT8h9QyftYUH3TZ
7tFetndT0C5nUIM21lXZoyPFLPS0nUcgCnkIrbY4lf9iVWw84p+dGi/z
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUD/plueTF8nkLakTDG0grFBs+OUIwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDcF8mA8F+FreurCbiCrW0e9t6QrME4w37dwoXxN1YamOO/
15IVMCd4HJRiCp9FN6Z/MrZeBgVqzzZW4XwdH4EcIAr3yFkRo21mxvlRKPe70NJw
ZByFhtkzTo+Sb8drAbl4LsBb7obxWAIhZvMT/1Od0QH+7mhkSi11gxR1AI9EF7cd
bK85MnAuH4UXDM4w4fg/n4gFlNiHhH2gaF5xFwEn+Bksy/lxFA9lEXnOI4QSTeCO
UtTPN7q2Ns5i1tx1zLmQDFfxkaC9BNq0GFDCRvgvEdFW3VGN44C8TTBbXDucdAFK
O8Lmhvj59Re4ulJuEeHS2Z6BTwEWdRXFPQ2j1kiLAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAhakbfc0tiTSdyXNqxXMzZ
EdQJOupcHLuBC4rIN5qlV416r8H+sBKMJoKNUjI/pUHdGiIiM5bsfVqBYeVF26WS
B4VWaj6KG5t+kmp+DTjur1MmgKt2mgMtbeziCe0N34mX7EdO6JBYriGQcq5B8+S+
WVcM3JBsTi7ou+6+V0AIs80e2BpGiqpkTOi8Weu8f3x1WjSbGjFCck/Om1M67v+O
SJo2TXv1boz1yFcjD7Ha8qTzDSDRQQJ9Td4LheooCd3TSQ6bTG7mNDaYh7WT5Ra6
TOlbXp/CnnSsF67XY7w4LjPXhOKpGNriDiyq0/DeKx+3Ie0kSCSoQZe04Zm40+OO
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA3BfJgPBfha3rqwm4gq1tHvbekKzBOMN+3cKF8TdWGpjjv9eS
FTAneByUYgqfRTemfzK2XgYFas82VuF8HR+BHCAK98hZEaNtZsb5USj3u9DScGQc
hYbZM06Pkm/HawG5eC7AW+6G8VgCIWbzE/9TndEB/u5oZEotdYMUdQCPRBe3HWyv
OTJwLh+FFwzOMOH4P5+IBZTYh4R9oGhecRcBJ/gZLMv5cRQPZRF5ziOEEk3gjlLU
zze6tjbOYtbcdcy5kAxX8ZGgvQTatBhQwkb4LxHRVt1RjeOAvE0wW1w7nHQBSjvC
5ob4+fUXuLpSbhHh0tmegU8BFnUVxT0No9ZIiwIDAQABAoIBAQClM5WkmsiYZruG
Xn2IWPSXUWYt4f4GxXbsrZ4sOQUAYdJRpVWZYdO+bHVUQfTa17K5ty771Dksuuxm
ukmW8pbOrZ6N7mwsuSbdBm0NZlrNNyk+A2cFMvrFcCqEGDLvNxQoCa+JUbkoXo76
03ORhw0UYFXHLNxequ8ETaeFSy4+RMplCEYoYFW7/kL3iZcvdvq4zR55gKI5JbuR
co8aBBEW0ddkU7A6RGLq3RAAR+u/wAtYIp74lDka0CdxBTQG7dnB0RIT9PTJS07z
oJhz+26Pvgnypkma8Zr9XxVK0un5KGeYys5XrM1yC14YORuYSV/35+Uk2VjBtP/P
ngY+BkzBAoGBAPDDAgEqtPFJlhxOYJSPwZdqXU0MaFCE/P0BM6vKKlQuz2KXdmzS
Slm9LWp+O2ZuDKHdB8GpD7HWZiXqvJOIE3xF21U4wpFycuGsbbEO34+6vyc/gs96
Noq/7H7G+Ut8yvIlnbFRiUYWhkTTXqBZgtTtBijWFJ6eSfv8u7OmYGDFAoGBAOoF
42X8ozmNNkYoJ5b28PJ3NgklZIIMED3Y4IN1Usjk07VYCOEv5VOn+WcL1magJ7U4
XFC/uR28wPNm7QD3NMKkL9McBlgduzAdm/1PIcjmqgr3liVQBsYHu5BuFU87wAlZ
j9WzfdFenr4Pk/aZwgHxEUy4GbcidUhN/cLs3fkPAoGAY2FbdnfWcLLbT5vaqfgd
BQ9Wq/MvK+15MEZKueKdTlp0KFI1A/5ZymkYUhkBE+rhM/80sG/ElrfVOlmGta85
u9ZqDud7COahHR47uRZWmdGQDfddW58q3GMUj9A6HzrH2uRED2mErHWnvskxCido
pdOg80JLCJ52E5njMOjAZ7ECgYEAzL30EhEy2LIj7sNIx7oqWWdUnjHZujFFsGZj
Hn/xupMAaeKoeiNGNqd5+t6PaF/r/Y9erMLf+RVfllPRPIwK29N7h+432rXARDtT
cw3dV//+evPbp69ZDb5MKfM1r4lt3IA/585OYHOw3EWSxSgGZV58LSvQS7nY9DZP
sk87cJ8CgYEA4d+XJN+cME3366wqPJV3Qxsaox9rKcbnrEj39mMUxUoW1egSw6EP
oVQ/kDoAckED+/EL/gExxK9kzrVf903U5+fj88ZlfkwdegbyJmxxadCOYzpXxjvr
ZCPSBjX54e87l23A+bnedRP2kUVwLNfulmWlvZAvVvgWmiIE75GtZXo=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUGEsNvk3tP0A/OO8kzGApLrkPgqAwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDfU/KtYwJBDRNT1ohOQiZyWS21uU249ykMPIUmryL6/2wf
V8QGoXSPapX1nDi5scC6/m9WBGeQkvytkqkfDCKXeQkcwDWslstYJrYQUL/aDnLE
Kd/EWkoFiQM2ALcPRk/v4W1s7e1UfZCn/LWRZok1mTvLhO7/ReanpQ9p7AcKgE7b
I2HCEpe6YT8X1eFWBQnsep3FqipKRTfOL3lAv3vd3ufahcU0rFY+REae5DKSyKzK
rlWb1CHUxEIHTHvUdmCRVkEBUfudbsS/9SDi6N4KHyW3k05FZ11E0iM0ugimlVAe
h8A968IFxcZj9iMU/WYuuOQz/xsrkie2VC0Un3P9AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB3bfnPsdtBRoQhCzF+TbF2
tJjl5Aa22Hdgkp+ew6X1l+BsOtSyKnWhfDE3Vc5ImWbwXCRXqh8R2GrlG1qACRFr
EoMr7XwYSMxF9BE/dsBNiVszs+cLoSmVKEzLdHMcdgptaJLbKRP+p3/M9qUgs6cS
7Iuwl8mqH0ebCgSMYrteVYu/XPanmTRfHIWNIVa0S8Wfrcu1FY+UiVSRVmSCPlGS
HOsYKko8JKlLG3ZpKOJ9wDLGIbOEelqCB/ysYXbzLTl/qzbrfdun3pk4rL3UPQir
FmXo/0MLHgnl1qJpHCXsrTIpxzCR2+7KpkA31JrM01T+6FBGEFQBVPo6zIHlPLDD
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA31PyrWMCQQ0TU9aITkImclkttblNuPcpDDyFJq8i+v9sH1fE
BqF0j2qV9Zw4ubHAuv5vVgRnkJL8rZKpHwwil3kJHMA1rJbLWCa2EFC/2g5yxCnf
xFpKBYkDNgC3D0ZP7+FtbO3tVH2Qp/y1kWaJNZk7y4Tu/0Xmp6UPaewHCoBO2yNh
whKXumE/F9XhVgUJ7HqdxaoqSkU3zi95QL973d7n2oXFNKxWPkRGnuQyksisyq5V
m9Qh1MRCB0x71HZgkVZBAVH7nW7Ev/Ug4ujeCh8lt5NORWddRNIjNLoIppVQHofA
PevCBcXGY/YjFP1mLrjkM/8bK5IntlQtFJ9z/QIDAQABAoIBACtJm01OVp6DSU7D
05HPsqIRdRG3REBo7/TmOizgX5hlL/D3UxCx9OTjlQORb1FXCfN04+G5YtWcGAwQ
1GUnNgFEPabr/rtgUzPX9Qw+iqFakZZCQ5RMp/Jgt1WdV95HE7F8cXheudTZrdNR
4WO4iznvZK6zKpwiUW4HSXCPhmHbVjEHWJveXNycMLr8NXj7RKmkNkiqBcBk/pNK
kR3qP8GiMKNgTSRJ8qnQFB+QeqGuNh8B5CJXQubJle94cbiJYIlJlAH8uzMtGDXn
9ymQMPAWWvTO/bmBT5Of5/9nEYxHWyaPZoSonLxObj0Da0JcK1tVSl7ujTpQPaVt
2g8rLWECgYEA9ogwLxiZlWV+VaOYciiuwaDkxBG4xoLgeB8g6zttBr9mxRyOF1yc
s+sVKMu60yX1y1sTIF3LeiuLnIAIbOkK3xDzIrz0B9rwwjk7DUQmFLu1b3p1LaZr
6R8u6VFZwdqGNOLpf6avxHaR5uu3jgTmpBflm3QcHQSB25BLqaSkyQkCgYEA5+eg
PIhScTZfxXUwOZt6FK+bF3QNeWocmkZM1q6JgE5flY+TwF9igMaF9LNJu+xAqA6H
xySxoW7PEnPkNUVHaS8Wu8TyVThcC3Qz9XsvKFdGM6+liv9Kl38GfGLM5pS94dwa
c7Jlx33EZbKxuruUdNVqrWhs6i8YW/7JLwmUFFUCgYB9z5BvaGlwcWQghiVVFOfi
Dp7QZI7cV4wAITqmcSQ5jlH/A4yL5Ype0vhwYk/MU5H1HlxLZzJg/Xn4+unR0rfm
kHrT3oPWwmedZqF5Kq8YY5a69k54ZnapeG1zSj25DTDyKl6o80K9yxi4NNDunBer
5DobtAxozpUKnL/QKiKiKQKBgEomYrLYN9whMbA2T0wsLXXNzH5MSj6nMiwWDF2c
gzS2WpO8y9Z36UwZrh1W8l2XJflWZA3F6tIeVzGkQrTRyQqV1uQFDiM3mR7EchSs
5aA1f6npILp39IbKQ+2jvbaAmtJMCV0zDp4h1Zla8L8vWUGeN7ToreKXWmeX6QYU
PvfdAoGAHXi3zRmkl5reHsfloNgP598rx6S7kk1hxAC0RGPW9wkv/DzCsaRwUoW6
3z7gUoopzsC/T8fGbhMoD5skvm4wPvn40dc6az1PvLowLfErM8W9tgwWuL6uKqIM
mFgOD7eTsIslvrikO+sN/SHWW8dOlPxzF9c2A5vKtqztYTr8kP8=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUYuDSVIYA8huPudIdi0WG2abkweswDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCpomQtc8V53Akl8GGEiAmySQBqEdpHzezrfzmZULGkPHIi
brx5QAUpzLTaRQL8vTKls0wN2qjf3k3oQXB8NDuveUTuosms14KeNhSj2AK/3baH
aUCe+F/UnPb3ns/YLZltuGUzsf9mp8P9yluTMhUqLweaRG4rfWkzu8aug6uuKt5o
5FBV8AHLLNe89WHBRDqR29BiQV7rrdfjVEPrlW0ZuVJ2obcp/OvXt6c7XEq/FgOG
r7qVxK9VELEZM2auH+wDHFghIdLgsbj3dUNOqxqhE3Mg3bKiTqxmrLsV15ZLQCcE
erJPLQsqjQla6+yGPOKou26C3n0ukdyWvPuipjqPAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCtDYfrHPXlP8OR62xr/Eve
dD+2Sl8KLDX+ekaV2p6GLO6+nTeD//8NFG7gh22LGBAyGYSKDcFSVy7fIl4iV98t
qXpYfC8PA+pXIhCI0bEHz0Jd/g0oCgtbvGs/1SGWYzVvvfrDunGM2d/IRLFtIwde
xNz661oFWR4UzbF16wPlxZ4S2BolgBAq9V3vr8G6r58/wfKLaR+kM11u3MupI/iz
z/b67IsYicnYf+r8tLs0NMxI3nt6bkMth4552GGOx0490faxSH2wvS8r9OhvHfh1
yzpmzqgcGJ5vVyzPcj0ADCe7USBsTF5ocL5wLpj5i1OWtGeuevkyJ4CUHOUn2l3T
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAqaJkLXPFedwJJfBhhIgJskkAahHaR83s6385mVCxpDxyIm68
eUAFKcy02kUC/L0ypbNMDdqo395N6EFwfDQ7r3lE7qLJrNeCnjYUo9gCv922h2lA
nvhf1Jz2957P2C2ZbbhlM7H/ZqfD/cpbkzIVKi8HmkRuK31pM7vGroOrrireaORQ
VfAByyzXvPVhwUQ6kdvQYkFe663X41RD65VtGblSdqG3Kfzr17enO1xKvxYDhq+6
lcSvVRCxGTNmrh/sAxxYISHS4LG493VDTqsaoRNzIN2yok6sZqy7FdeWS0AnBHqy
Ty0LKo0JWuvshjziqLtugt59LpHclrz7oqY6jwIDAQABAoIBAGWXVKmH6R9m8K+g
+7YUhsIYSEA9+tz/7cDHy+YO1qSGctA+Q2/WMIFtEG6b4AMfCAMGkyjE6FhSWZQc
BNLNsWUQmoDUSzXRR2+a8deCGXtwu8zy8vmBxFqfuqRnnxBXlsiII0vHcS64kH8g
vqEz4EsIKWRxUQ2IqQWLkpyXTK0cEyqwSoz43n+DQ3/xdsVA2cYtQSQyc46IPt6/
euHHRvYaJi3tlL0dUCn12Z18VcKYI2fsdiP7RBpVSf631ssHXSGGq+fP7t8Sr8kW
DJVfzpZg0HzrbsUaj7HDVolCRfdRPAY4yGTPhm+J3X37xqPf5PdlsLIUCNg9S2Gl
F+OFjykCgYEA32xi6dD3PlV1D7e/+XF9H7sD1h5WKFSETF7Q0+BuWjVGJupMLpC9
h3YkLcvus3+eXT9VhJ2a92xpVtc5lTYxPoJ/IlnFrDaOc4WeyNXz4xGUeNYXe0Ua
E0z0X4MueaQmtycbqfIeYK837k+lQaBIL2zD2jTeoUCnAlYnvHNbAPMCgYEAwl4/
gKPhAXJhRHEBazdJ0+nw9N/zpFFi5PQhRu5KKpRYypxjL/DZtjDJuXN1lEfZcoDG
6D0EleI9VZnDQSjxv7APTFE06E9SaqF1mJA7rpFv5GKHk5uT3CEx1iibTWrUncRO
gdwpNfN7D0P2A2de+mYeEwLw1PR/ZcL1E+x85vUCgYEAvi86J8ScojAGfMGypfiI
RTlhs6ORPbVsBMJ1StZxuVI+DCRHgx/sZeIYO++rmppYyRF/j2rFnjZnmOeOechu
tMJKzIfUb5rlOcsVdepCOBkf5JiB1onk/2bzYlZ9ekhUOHYO42RZnX2pw6+CgdGZ
gN05/oYguO0a/S8vlggwACcCgYB3FbmAfmeINGUFwtrkrq4sCQQZc/DZtweJUU3m
IG8OYW95S5G1uLIa3w9o8SWT4OWIMwArH99kWYXMoXWwwX5EPIFS99objyXmsN/U
xmHalb7hRcDdHg/cafYXyS9FonN76d9Tzujs5i16b+AVu8rETbaVXVLilp5LYcQ4
Hcd01QKBgE1MUbsJQI+LELrVTOJyZUZ/hI6IWI/uXkG4il+j7azwat+TfhwYlvzZ
ZdwzUMnEKH1j4jX3jLeS9Ds08IzpSXvy1gkISg5cPrr6nMybVkfHPmCCdUPP3O+Q
fRVO2Q2QWfFKF9U4+FfTfa3GOU3LUP12sxQGLTVXniYsOpyl6zGL
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUN/JXfTKKgYd8tAmAAwPecG1x5qswDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDRq9bspUpXBycLMb0rLXGVMD4xnT9+VfLF9GD5EFVOCG9N
t2VmZ8Tvlq76G/5MI7nI/wf2E+Z5e46DFdsCwH3uZRja//eQQ3jhiNN92qPaHpZo
15CXLRm0HUEX+YHTBCQ4A2evFhH3CkxVmTwJYEIfQUf1N8XRMTV+LUGdjeYJSMR7
GuDrRft1AJDmGEeECp9o/DxBc/Na6a3hSM6EKfVacXh3XZBuRtfXvArOiZw18U80
qzi905hw0UnsCd34hHc30gYMI1ZGnhafFQRzLQuIAzCQgKGZJ6S6mwY1Ovu8qi6T
vjGGzWc58yRv4SgiI+wMEJGcfDGEjedXnH5Sb14VAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCY5SoXBJC1OtM3oDPvrbD0
ziondPDLGfS3zOXZ224c9s3vV8VOfUtdamrjn3OJnip5U8jlTg16gpSOqNK62CTl
kgRtmR3tBLZmSfQIDB3SVN9OLWS+bpb2BtAdrUu/3vdP9EClbPMCO6lCDnjt2LBV
qGmfBl57J9p9j/2z2ln+C9AboGmJGlNWiu56kOYUCM3+WYSSAq56FCGpqMSzBvX8
0q7lAy/dG07fVtnE6FSQ44nEmqY9zq2goy0F/w3h9EPXaIuixz/PnJuFhPHVZLZm
GmpR9Aqxnu1EURt0I/reYetoXB4oYP8b+3LtQ00o64fQV7byKNSrji6Nw6VVaCUI
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0avW7KVKVwcnCzG9Ky1xlTA+MZ0/flXyxfRg+RBVTghvTbdl
ZmfE75au+hv+TCO5yP8H9hPmeXuOgxXbAsB97mUY2v/3kEN44YjTfdqj2h6WaNeQ
ly0ZtB1BF/mB0wQkOANnrxYR9wpMVZk8CWBCH0FH9TfF0TE1fi1BnY3mCUjEexrg
60X7dQCQ5hhHhAqfaPw8QXPzWumt4UjOhCn1WnF4d12QbkbX17wKzomcNfFPNKs4
vdOYcNFJ7And+IR3N9IGDCNWRp4WnxUEcy0LiAMwkIChmSekupsGNTr7vKouk74x
hs1nOfMkb+EoIiPsDBCRnHwxhI3nV5x+Um9eFQIDAQABAoIBAFOh5He+MpnmG3fG
njsDxGOKu7QUkgf1hoHZSXjvP+eBS8xHE+Y2DAK5KxBObC+4rFl1CJrqMytP0neN
Fy/Q0ipuHuzz3q6niycC6cEwndzaCIrHOUBj1/XVGWrTtioSY9QH36qh9gaBEBOw
rJbc02MeKfKxDXG03C55JMwQlqoqqDTychssqj+4g+Z9IFr/qI3lx9NJLYIaKf6D
5XcCGmqxJBCo1EZ2YYmAyrNV7T2T/MjcdblwnL6V06ZYu/vrUTjpaJKqKh+GYl+z
kKOBi8Ff3FuSQXlc/P4IOKHN5J59UxOIe65JsjC8CnqImBssdPW78Uh3ieIU7YxI
hQNggv0CgYEA9fAO+G+hPVEJ3QR4BLiO8bn8pbAm2XrruqdR3GzT24WJyI4erJJ7
LpdRaJjzi7fplmF3n5XSABEZuJw1aDukwBIpZ6M4+XlDejsZe0YvxwSTAGIYwygZ
VMMKeLRoiQIy4e3XaZIbENjJkLr7AKdshIcQa63foDcm0s3slKBJ/WsCgYEA2j/t
boEoxLe2svNy+Dg3FSHCgvsYbSH4kB+66hxaxx8hf3UDVtX7WnA2kmHsRtk7BjEJ
P1XfoZFQMJ+XK/re5rWtxmTkorpApokKQF+gmnA6YMepMCYTaTufzcZT9QBjj5W8
y9OLIZS9eC67zYXQ8/+32xHtU9DHOOC1Hq/jcn8CgYB7FkpnzHbGWWi2VSY8NqJU
GOF5i0/mSL7yDAvMZisiExOCbJ6tgCJmjxUPZH1/z+v4d4+HL1SK9AQLgSK5qCAs
gOp4FBjPwwEii7GVIOuIj6GC75W1FryWz4bOInyvFYqhyIenLpidNeKrrOkyyphl
O7PcMIlbhj7IAogFWrOtQQKBgQCVqi0aEHxymkExan029uXfGe2XgLV5cUhRHVFC
ZftifVitXQLTM55QoI7rxzcORr2RO2NKCYt38nx5O5ehU0I0F/Z5DIs1hF/9VBCx
oGI0Ri3iXEkLebDqAzdNF2pPotqjhl2XsRPCDYv4tKOZBuEJ0hy0oBCN36geuwm5
Z4ij5QKBgQC4ZICjQCBa4sHrSVIRhOxQ//WLUFBNqBnOCKXst8x4I827fgcQqzRp
QjbcXqkSlvcstWplFCTBabR5ZOnHCGHsXBcDKrQOv387OC279fG0RNeMlaZmSC3a
1pOgGDzhft0Yjog+whVg1ldrDMU8q9vukm8ZLrYigJgHfhkNkHCC5A==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUH0ogquGB4mndRRHavQuBPNDRMc0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCfuudKm7y0TVi6OOD54Ir9f0LaXBWRy+Xdq+0Jtmbc5TPk
9XMgt4DP+U6KukAwSb7jEudyiHjWIeB8EXkQ6bVRPWUxo9CZtzPjYVi8yZhJnOqE
r5oSgiS0L45mEuhrVeero+K6QtMlU07UaZk2OPq+AppeYLexMDvexxx1yVf36mby
VG+o1s/Eu1RPLaViaF8Owjl/A3YgccKUSx+/KKYGRnSIaEpoXdnLbD6HfgLWZbw2
qBg+eiy6GGYVFTJ0CcnfxgTJQ5wN9je+VFEPvdJQpuU/aBZ/CLxI/BCqF91xRg/A
kND8+WqZI2X5ET+gnRuDA0SzNARyUx6ng93vyCAZAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBWOG1W4dxscVyJPt2hczoN
OOuS9uA6cHeqtRyXxwBfCxFMTBJn3nEnNFNt1CgLhyPQY1CFyf+8ZycaIfeeCqE2
+qHdIpwoFOF0usRUi1oH2Pb4F/62x1EERDdl+tDdVE1vgm5Mh/teDBmHZwPnAhyZ
rX3FAN/he6JXmZpQCuMazJ0PhcMPbrwtv2RBkFGneQamHYbTcsofQlecgRIcGRbO
N5nr1d6LGoBlGRNFJRcH+9VZtw09dOixh9+uzKHIhzkUpJWrfpZXGq/Zxjjhj+7G
z1LWzIV/uatBy6TyHsnHicPyc3dYW01OPE3TjsiFMaGFB2A38IcyqP+3PmzD5vwG
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAn7rnSpu8tE1Yujjg+eCK/X9C2lwVkcvl3avtCbZm3OUz5PVz
ILeAz/lOirpAMEm+4xLncoh41iHgfBF5EOm1UT1lMaPQmbcz42FYvMmYSZzqhK+a
EoIktC+OZhLoa1Xnq6PiukLTJVNO1GmZNjj6vgKaXmC3sTA73sccdclX9+pm8lRv
qNbPxLtUTy2lYmhfDsI5fwN2IHHClEsfvyimBkZ0iGhKaF3Zy2w+h34C1mW8NqgY
PnosuhhmFRUydAnJ38YEyUOcDfY3vlRRD73SUKblP2gWfwi8SPwQqhfdcUYPwJDQ
/PlqmSNl+RE/oJ0bgwNEszQEclMep4Pd78ggGQIDAQABAoIBADMImVtqFMmaqM2e
3KqZhm7l2StBHpcdiUzg4HQo9gZ/qKvvjCAY4SwRoHmMdnO3LCkK4i3i0pC/9CRP
xNmVghv5vLo2d7CVKxvr/1kaI/DpFLjeDiD5udZkF2AfjGi24rUhQJB4R1P2oQoW
zx/W5q4M0Nt0lVwkaAyOm1Y6xUNs/KKm/greKPRlZCwcHUg3RYE3D03Mgiy6v7KH
/QelfUhEzTvbJ38mjd6djs9FYHeiG7XH56HQB2SF0MNaKN2s9Ej+i9ZUf2WoOtWN
qM9i5eymaV0LqAyCtU+4RTAhRMpH++nHwxm90Hhb7DbSL5zOd/mR3TDKshS8V8fr
KK9uX40CgYEA1M8zuKTqbtT7l9rEJ4S0nnfVDKrqWyAvOcMNvV2s42W/Z1NpBwFE
ovxWGnQrTkja7adDHGA9UGzif09yGzpDnOKc8sJNAmPxDyYrkBrgTAcnwLP2L+Fs
9okDNb2fBAI+OHOcNKX8JUZ0SHx4q0sUD+Xl5x1J9gpOx53D1U7acQsCgYEAwCXl
OhqmJHwDdhBHGFygKE8UY8YaArFd1HGi6g6b/STDSGvyvVQsCrhN4uBZw0wdKPXg
nshrIid3ZICGRXqGcS+kw0f2+4skUQ2FzSIOYDVq3zSdnq0HRxucamQMhA2LGMxR
T0LRR3K8XHQkmTAcT2HFj7qFMYObF6SkVZ7l8esCgYBR6oxjOAARt6Q9GPXGrHuG
QGRfIu9hMmtbVazVRtjFE6Zw1JeqHZ/ZCT7voeYFlV/IeUkJBDa13aP2E5O9zVi3
bDez7n0MPYJOLYg5SU8rlNmFgQBz/9ccszLsHdi3B1ICEuZ/EaGUi6E5QciFTzoi
wIEVzJ1qux8GEcGPO3I0bwKBgGoTgZy2IYp6vB5tlhIo8HHQVl1OfAWIjVg+88Vr
E0qJBRXyIivLUBUK8lSRrnxWhLKcKsj9s8dDKnJdUcMBhT7vInJ8RClSA1aLtJYu
euk6FCntDicPNrlW0N8bJJ2yLFwgT7MGHCrpeHtB0wKOwNJCE6LpQaa4FOLUjbSG
6ELJAoGANbe5Q6c48hLJcdZe4AmNX4VcPrhRN2PyE8Qbwqq04lBpbHqbijosX9oQ
AqMkYLavW85YDru5i+trpuq80msX+Y9EWjXmTkjwg6yxhVwkZHLAVrZMq9F7e3vK
zTScXyJGjj0OJkUhbNTH2O3S2E5Pqrfd/m+idRo9sL+gZeaJXHo=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUchZN2ld769tiYoK60GmFQF/Q1z8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCmD4gtULYn91b8jZo0/I0JUA6j3lbV40/ivqH9AqEoHiKY
qQMbT1IywATq0/oaawM0sz3JfPPWpRVMVHHXWZdNtSinnXheqraWJX8ZDLmMKhMP
srRgX1eDjY+brHB1+E/0BGhFmajopdv2RDlfjljh+J+/nFMqvR5m2Eap0m6peINV
m6gYloHwCfa/ieYsF+zpHJNX5t4Z3q6BiTZPwcmxF19gfS35ea4SEqW9Skvm2+o8
VbOiC0y9VtSl925phEn7ptefu2vT+QtgNVllMZ1r51s8T76bs/pVBUTE0ZSycQsU
LAgNP7luy+PepQf5JsGPM9M71idQudkjiNKRe1EjAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBAwLNxGGdf9VqeqG3RO5lS
a4B7k276NjG9Fl1Ys5BbbUzpSPwLunNGGNI0rhlY+uUZDCg8kAdwfnrMwtoTwH8d
ez0cYCW210Gdtg0z4X2L0oHkGMxJwsRvl7cp3v1k5R1iupFzdE4lUsxapfRrQeOt
JJGVVDdQKKZ86DuDMpanrBGUWl8e4b4/8bQS/8PgCQEJqkJjVB4qS9km/CV83D83
aeJVOvBlf1TfJgmxKvUksgnKUoN1L1sN6JIcWtVqe4qj39wmCZLIUaupFE0fmUYt
JPrsEwbkgm1PN+n0+gyV9uNwW3WFGoildZ/hCN0f9KuH2uz/LmnMpEmBMnnk/DAS
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEApg+ILVC2J/dW/I2aNPyNCVAOo95W1eNP4r6h/QKhKB4imKkD
G09SMsAE6tP6GmsDNLM9yXzz1qUVTFRx11mXTbUop514Xqq2liV/GQy5jCoTD7K0
YF9Xg42Pm6xwdfhP9ARoRZmo6KXb9kQ5X45Y4fifv5xTKr0eZthGqdJuqXiDVZuo
GJaB8An2v4nmLBfs6RyTV+beGd6ugYk2T8HJsRdfYH0t+XmuEhKlvUpL5tvqPFWz
ogtMvVbUpfduaYRJ+6bXn7tr0/kLYDVZZTGda+dbPE++m7P6VQVExNGUsnELFCwI
DT+5bsvj3qUH+SbBjzPTO9YnULnZI4jSkXtRIwIDAQABAoIBAC9jU0sLM1AoZyxf
BFiGkYDM1cCxnDohShS8reFTtMWMA/dok7hhZGWTIlQY9dBAJYQOel1bSQJBzdgg
aPQ5XtIQFm/uogDx2nTyclilpvV2tEXQi2TNEF48MXUNOnKPz9EkyNTDys3JNwIJ
6g14w6iImJ3HcHxLx7c1lMS1hlrZ0VmU44/YlW0rXIEYAHpY7Zg5adEXGhlEaFnq
+t022nDlOYUY91H9IwftRNT/jj1Upxgu6lmQAqVtdgjTi3PcG2dVr88EQ28t7oF6
qOxKDiGkFBkCZV/V22eqdnEq75NVUrBGxkWlS44KDi7qQHoCOk1AtftXqFe1ImqO
YwGYcaECgYEA2VjI7ugWHdNuzB8hAAdqEbV17mgWctisGFGpLBrFWu9F64jqlZ+A
APR8U+V1oir54A6PukNhndP6L/bocYtV5Vlngg7BzeVHdByrbTnNwZ8jrd2JiAlA
alvGC1EjGGDWAhJv2UAF7DxbwI4lDlqfHoeXyvruP7dSKP7VLYa67DkCgYEAw5fT
uH63BIP4ToLkBKLd4Dkq0ZTUIDzBcZtyk7C7m/WlndxpYyw49RMSBlyaR2JuT/pj
FPyDIkjuwqhNYCTmwhsLy6j0w9tY1vpDOvJg12V4EPOycSC2Jy6UJUfAGyet88SV
MNljEbrqnlUQ3HWejANTKnJFZo3N8EOSXE1d4DsCgYEArg0di8QrweLJfYkIIj/N
vzSzpiGQqJO+7RKoCPu/Q50NPxs70GoUVa9zyLOeSilkRPskOiMvjvZsCfEOH69X
L/0ymMI8jSeo2uECnsuFbCKGrfsU4e2WuhWYOQPWuPUDLFGbZDyTAaUsTL0IC8Ci
YA5xjkj4denWT6ITEQwtsHECgYAovbBRJrvSifany+XY/V+/+8hqfViuGlmk4187
Wj3J36IOvsGI8cYvbjh78MAGDH+z0xDeZzadZpmtHEd5tlYGqoGLe3b4cPERXnGw
jpoTY8Rdq5VIsSqgALjFBywBvAMk2pbE5RMYt1l1f3ySn0FWIr8pAUJpeTIjUL/k
0Ay0zwKBgFTW+RKHanBZy6BUgfTdOw99599h9l1Crzvk0FOWOEOsRc9ksHEALTlA
LaUf9r4cTDC+Oz8Yab3nnj3+o8FWYYxRBjBkTCGpasscvbAzRa9EBw2RMWaKb8um
scpS5ptQ4CzueaT+tT+Apw+NPBeLEn/jSn6+af0DZ6t0Qf0teidJ
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUa42MrlXu0Vb3u6bdR8DwCfMsPV8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC7oQMwbqJoeS3oiLCgTaa5ruJkb9tPKzPKwHSrRcyXsFim
wNp6dtw3rxT4i7Fa5gAe7Y4iH72pQYOVMfTLH+5gEciUjnhTZwilMi/PzcEbsjVV
UUr23RoZ5iLVZNAcUP8lcf1eSWJk6ohmA738artmaXdcjXO3gL/FVi5E8BG3n5Dj
ZcQ5e+eTm0CbsF0cBa42TjTyjr27/o1J79kmoHVVlZIxZXVJNMcnXHcMF68UQi/i
czEZdpby/T4bnU8e/fnXe94v5Tsr1wWtaqQp1xh4r+Ngtn6ovu+JGHdX5FGsnOGM
Wjnzu3gXm4BvSVq6R5OZptP8NPZELRq4S5RbZoCbAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCcYWvDW8WbK0OkXEDGR2DZ
yv8g9+Wtg77krCngqMnLcd33IBEqm5Tc02WfZCd786yj7Qfz1v9Y0qHQodibgfYK
FtN7zUMaovGltm8M0sP5XdQKh/UAjmvCtOn/qB4mYImkx5vkbTF38kH+wWac7kWg
3ehxJ8Xsv6SLLNb0KQgrFt0HblVC5Xr0JfHLKDm9j4QmIjeE+DkS/xW2ERr+E8MR
iXgoWjbeXfSwvstAj3IRSN6Wh4gsi38unpC7sxsrCalRvASgkvaAykV20HcaueVq
BzQ1jKOQ2zKpAr0n4mXtrtvw/t2VNVRu+QEir8Kwm4TtTHsgaIuU/sVchYqDsKgy
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAu6EDMG6iaHkt6IiwoE2mua7iZG/bTyszysB0q0XMl7BYpsDa
enbcN68U+IuxWuYAHu2OIh+9qUGDlTH0yx/uYBHIlI54U2cIpTIvz83BG7I1VVFK
9t0aGeYi1WTQHFD/JXH9XkliZOqIZgO9/Gq7Zml3XI1zt4C/xVYuRPARt5+Q42XE
OXvnk5tAm7BdHAWuNk408o69u/6NSe/ZJqB1VZWSMWV1STTHJ1x3DBevFEIv4nMx
GXaW8v0+G51PHv3513veL+U7K9cFrWqkKdcYeK/jYLZ+qL7viRh3V+RRrJzhjFo5
87t4F5uAb0laukeTmabT/DT2RC0auEuUW2aAmwIDAQABAoIBAHUCNmDvvax1VaHc
DHoLstu9KkYEU7oNcSER4DAnOS2ntcFYJ2eT1EWNlABj7ViIcq7W6npxXO++gXZ7
TvOVmCylKncqWfN5H7UVlSd8Yt8IxaXNKnjE7dAU6sg1NGtUP6l0atNv5EKW2DT2
RHazgOafAube97kKO42u7u/i3smpUWic+VWOOkCAjdQN3aj4c7OwxW2WJL+MFyGU
2+1Mrl7vgDiQzif+LG01kBhwTL2Hm3XFNhbJHO3XzDKYb4ttqBKYUuRM+hxZGIjs
nj7R9zEpWoLP08iiuFxdlNGLWWx2QE2Hpvmtw0IfXI8Cjxz2sxne70w6JX4HbHIU
tu/5EmECgYEA3qkHI4u5AKiIx1BXpRP3v881FWjj0PxwFjDHKmol+mseNkVCElfu
Df+qhFk23VablKRfuwjhxyFb72Y3b7ZjZnYVQ/gxU01ozvSq+i8YRwvOZ3ks1faz
dQ3e+uSV1qWBm4uqDdb86OYI0WGP8h4vqAcP0o/KmgmSMrYUrS8dTIMCgYEA17kr
vb1CuLmFT8MC62053G/29CCtWmDrFun69c3M2cbWuVCQonCEKwvyWz2uQ2qqkkoJ
HUUJ/v3Vz2BYN4DGP/IQ8UFDF8DYcQ/u3EGGSzX7VJElUoDSLw8P7/wX9Gh8K0ho
ljy1wlgg+s4j2rA58c7IzsR2YDyUJqY+HMyM8AkCgYB5eghOCU2+oTQ2YYvfoTw6
ZmbUrmwUOZVBVg1jA5SCwewyuahpb5WOB51VJYM8UKMC/obH+PmM9ZM90iuOhBhI
70V81qy6gPIcbvnVEtqQ8E0EwOSIO1b/Frk/cnSZLaS/Yvw9HrzOp6nJ6gtpkbR4
XJnyS8bCMVSU3Cf9sEWw1wKBgGCHvakD3a1nZt4QN2g90hxwBaOsU6YTpF72iJQh
aT8yGLeH85CcpKfWiraFXUtRmc4oTvfIAvcVgu1vAUqk1xGaMjaiq3EfnDrLlGj+
8ScKmtJ2uKq4dlUUel87AUUe1CFSH2rK89JpOSjBwY2EOgmYLIdJpmbd9LVuwnCE
n7RxAoGAGr8DVsRf148dQOCdKSjpT8M+shkrOgsp6+iGzGYeucwSnCS1QebkGCZS
UB+HF5IRHcH9q3gvQaCes/a9oZXagpUVru4Hm9uTe7gaP3vV5x6+8CMVtolrKCE0
lwarmXSO6kpyVxyQkRbRWBSlvh2mNJw6ywgN9KBANNvq7YSKdy0=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUICyWEmsr4MlpJdYd26hP/SeDpY0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCo9A1mRiRjlRDVdiu0aQjkJKzorb9LTNnlkWGIjTjoFOhS
w8+lxt4Ul/MQf4xx3KetsUT32OUOGy8RGOWhCnDI1v4V9QzvUWUniDLu7DKFmmHq
uvoW9LGVy/2rA19OeTu+rg5XbygTHnhfMlHwd1jlg7fc6eQlouwA+HtJ6yPNAgRK
3i4IyqHsM/UQQpoE0hb0cMTSR9S+LlGsmL2TciPV00YYzGLWVYXGIT4OAtZg6rsx
FzxjzEDGIxqKZwh6O82L/nM+/bZz9cemdKKnJhEByxeErBotD81y7lrlG5PRNjzY
/1h0QhovQ1Qq0St8/JuJERWln+lB4hh3MtmChTW5AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQACE2BlPeJVC1dMaotYniTu
G7WsfsRbNaozT55kXwMQ8/SYGLutUZr7pqO7VwGFlEiIKD2nbypZx69Q7/GjMtTd
5bFFtrkZcuTViaLARZFbSTAYeakp3CGrUanlJT2xLTFvu4HFxFCBzpIYGjhLcm82
spMaHzr7Ch9jZIlFqB8bHJcedEtOSnIbeetVNDnkES1JZCN8GBDpUmbKxWm5qfPs
WDG546VZbigBvsWDke+z/mcB7NkbasyXzzHqAdlvBMjo9ZHQZfvqB+6Ira0Hir+R
KA9hMtCL1MTX9Hg5+V8MZpoOi66B4q71svDoL/I/VjO3w2QFyt+2+Y2gQp6YfGdf
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAqPQNZkYkY5UQ1XYrtGkI5CSs6K2/S0zZ5ZFhiI046BToUsPP
pcbeFJfzEH+McdynrbFE99jlDhsvERjloQpwyNb+FfUM71FlJ4gy7uwyhZph6rr6
FvSxlcv9qwNfTnk7vq4OV28oEx54XzJR8HdY5YO33OnkJaLsAPh7SesjzQIESt4u
CMqh7DP1EEKaBNIW9HDE0kfUvi5RrJi9k3Ij1dNGGMxi1lWFxiE+DgLWYOq7MRc8
Y8xAxiMaimcIejvNi/5zPv22c/XHpnSipyYRAcsXhKwaLQ/Ncu5a5RuT0TY82P9Y
dEIaL0NUKtErfPybiREVpZ/pQeIYdzLZgoU1uQIDAQABAoIBAQCQd7cpd9rPx/wP
+y7d4l527qFniIIlOj6r3UdgAxng4VfSxZq97zGgvFlcBySpi/tZO1Z08+LQ0A/L
99UKgin0olm7nsGDtb7gMccTo6aDtYH6vAzzKiLbqwVqgMSzDlk28BBVVTgYORrG
k/mavAKoppvGa7zpLcnN/qs1hrojJiz3FU5Td0j1oYgRcAIdJkWJGFMCzlxTQ2cw
5itxtzjXZSLsr0XbxmUHOG3dM+m7CVKK104wdveDLBDvRL+vgRLUQqQp5u/qwe2Q
ZlGh+LQxg5juO4p61nlPbkOq6Ch72ciD1OwzvD+f2KIV4iSlwbcB2XGE36a6BSTk
PckI4XAxAoGBAN1fKUpBXVHzYpnH2PsGhu5u/pGavBrdbhWeGVmju88bIM7KRDZt
CJOMX91N8hbIjZQjuHtB1sTSIKQ3+ZHcttGi9yJWu/Krrl+HcWTjcnIcwmpSCUu7
DHOuZA+3NWa1RyU07+McE4cJcOuVtlk/hOo3mdME3nHxeDSUOacq2pHdAoGBAMNh
y2efzcYHj9XokNrv6TZBng4EY41k4StpwqpWkV3iw+ym8w8Qj6vAxbxTt31fxILV
BqyFksq5CkAlRseWGgteIP4CZVyDkZIcaMeQdm/5I8OkcnZEb5cL8HUenVRDdjcA
7kwc7yzOC+LzIJyCQ4GN++N0ykaFrOgiIYPF4euNAoGAA3LhFMwR5R3ykky/v6Fp
ZruJ8cDEX3LFrUaKRJA9c8uLZk1WZLasJIhSUgNN2zcCpaUs0ZbD/sr7QTOyCqiy
nG96hClvwicUj15v0M+OT+LM0JU4mdpvJjo4Stpi1ZfLZPP/LL2aPEdUYAc0EQ3h
RzjYh6YSxRmq8r7Aay9Kum0CgYBHmP7A6n6tovfCm4b5tBDyIPmaiWEx31XkYs1D
PpXmocLKZiOL0bXUasALU2JaP03z47yeXBR+1XA8MWzOluLUZ5oPezFJxa0CrgZ3
myjLv7CrcQfA7zM1Vtq3EJD24AHiBiVNHw1GjfstH4tDzziNsUotAA9f6HyEVH2T
nGA9wQKBgCe1d4qXM5YNI+TkP10/KE4iVc8gcEMtEtwECPc3qPbZVXwnfgcJ0nUl
pW+QMSziVgWDv6bTr1uiOMLZGDUi04+oEmFX0S6gGwVVsnQkLklQB4TOBaJ6nIrO
Uu2HdVNORi7L6RuU+7qhuTe6YEuEgxDLtI5Mr5xZg1huuVkc2w+X
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_10: Tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_10: Dict[str, Dict[str, Dict[str, bytes]]] = {
    "full_node": {
        "private": {"crt": SSL_TEST_FULLNODE_PRIVATE_CRT, "key": SSL_TEST_FULLNODE_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FULLNODE_PUBLIC_CRT, "key": SSL_TEST_FULLNODE_PUBLIC_KEY},
    },
    "wallet": {
        "private": {"crt": SSL_TEST_WALLET_PRIVATE_CRT, "key": SSL_TEST_WALLET_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_WALLET_PUBLIC_CRT, "key": SSL_TEST_WALLET_PUBLIC_KEY},
    },
    "farmer": {
        "private": {"crt": SSL_TEST_FARMER_PRIVATE_CRT, "key": SSL_TEST_FARMER_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FARMER_PUBLIC_CRT, "key": SSL_TEST_FARMER_PUBLIC_KEY},
    },
    "harvester": {
        "private": {"crt": SSL_TEST_HARVESTER_PRIVATE_CRT, "key": SSL_TEST_HARVESTER_PRIVATE_KEY},
    },
    "timelord": {
        "private": {"crt": SSL_TEST_TIMELORD_PRIVATE_CRT, "key": SSL_TEST_TIMELORD_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_TIMELORD_PUBLIC_CRT, "key": SSL_TEST_TIMELORD_PUBLIC_KEY},
    },
    "crawler": {
        "private": {"crt": SSL_TEST_CRAWLER_PRIVATE_CRT, "key": SSL_TEST_CRAWLER_PRIVATE_KEY},
    },
    "daemon": {
        "private": {"crt": SSL_TEST_DAEMON_PRIVATE_CRT, "key": SSL_TEST_DAEMON_PRIVATE_KEY},
    },
    "introducer": {
        "public": {"crt": SSL_TEST_INTRODUCER_PUBLIC_CRT, "key": SSL_TEST_INTRODUCER_PUBLIC_KEY},
    },
}
