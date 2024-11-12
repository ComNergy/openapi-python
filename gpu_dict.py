'''
GPU 型号与 ID 对应参考：https://fizuclq6u3i.feishu.cn/wiki/FCQ3w0ZLei8Y7NkGOpxcCoEsnBc?from=from_copylink
'''

gpu_dict = { 'NVIDIA GeForce RTX 4090D': 162,
 'NVIDIA GeForce RTX 4090 Laptop GPU': 4,
 'NVIDIA GeForce RTX 4090 D': 12,
 'NVIDIA GeForce RTX 4090': 16,
 'NVIDIA GeForce RTX 4080 SUPER': 73,
 'NVIDIA GeForce RTX 4080 Laptop GPU': 112,
 'NVIDIA GeForce RTX 4080': 14,
 'NVIDIA GeForce RTX 4070 Ti SUPER': 43,
 'NVIDIA GeForce RTX 4070 Ti': 137,
 'NVIDIA GeForce RTX 4070 SUPER': 62,
 'NVIDIA GeForce RTX 4070 Laptop GPU': 63,
 'NVIDIA GeForce RTX 4070': 8,
 'NVIDIA GeForce RTX 4060 Ti': 100,
 'NVIDIA GeForce RTX 4060 Laptop GPU': 92,
 'NVIDIA GeForce RTX 4060': 35,
 'NVIDIA GeForce RTX 4050 Laptop GPU': 5,
 'NVIDIA GeForce RTX 3090 Ti': 25,
 'NVIDIA GeForce RTX 3090': 32,
 'NVIDIA GeForce RTX 3080 Ti Laptop GPU': 68,
 'NVIDIA GeForce RTX 3080 Ti': 34,
 'NVIDIA GeForce RTX 3080 Laptop GPU': 134,
 'NVIDIA GeForce RTX 3080': 133,
 'NVIDIA GeForce RTX 3070Ti': 337,
 'NVIDIA GeForce RTX 3070 Ti Laptop GPU': 15,
 'NVIDIA GeForce RTX 3070 Ti': 136,
 'NVIDIA GeForce RTX 3070 Laptop GPU': 2,
 'NVIDIA GeForce RTX 3070': 90,
 'NVIDIA GeForce RTX 3060 Ti': 45,
 'NVIDIA GeForce RTX 3060 Laptop GPU': 7,
 'NVIDIA GeForce RTX 3060': 19,
 'NVIDIA GeForce RTX 3050 Ti Laptop GPU': 44,
 'NVIDIA GeForce RTX 3050 OEM': 275,
 'NVIDIA GeForce RTX 3050 Laptop GPU': 13,
 'NVIDIA GeForce RTX 3050 6GB Laptop GPU': 280,
 'NVIDIA GeForce RTX 3050 4GB Laptop GPU': 38,
 'NVIDIA GeForce RTX 3050': 187,
 'NVIDIA GeForce RTX 2080 with Max-Q Design': 151,
 'NVIDIA GeForce RTX 2080 Ti': 121,
 'NVIDIA GeForce RTX 2080 SUPER': 97,
 'NVIDIA GeForce RTX 2080': 129,
 'NVIDIA GeForce RTX 2070 with Max-Q Design': 241,
 'NVIDIA GeForce RTX 2070 Super with Max-Q Design': 354,
 'NVIDIA GeForce RTX 2070 SUPER': 81,
 'NVIDIA GeForce RTX 2070': 135,
 'NVIDIA GeForce RTX 2060 with Max-Q Design': 103,
 'NVIDIA GeForce RTX 2060 SUPER': 53,
 'NVIDIA GeForce RTX 2060': 132,
 'NVIDIA GeForce RTX 2050': 29,
 'NVIDIA GeForce MX570': 350,
 'NVIDIA GeForce MX350': 10,
 'NVIDIA GeForce MX330': 324,
 'NVIDIA GeForce MX250': 79,
 'NVIDIA GeForce MX230': 195,
 'NVIDIA GeForce MX150': 164,
 'NVIDIA GeForce MX130': 152,
 'NVIDIA GeForce MX110': 260,
 'NVIDIA GeForce GTX 980M': 64,
 'NVIDIA GeForce GTX 980 Ti': 347,
 'NVIDIA GeForce GTX 980': 247,
 'NVIDIA GeForce GTX 970M': 215,
 'NVIDIA GeForce GTX 970': 122,
 'NVIDIA GeForce GTX 965M': 273,
 'NVIDIA GeForce GTX 960M': 39,
 'NVIDIA GeForce GTX 960': 37,
 'NVIDIA GeForce GTX 950M': 305,
 'NVIDIA GeForce GTX 950A': 31,
 'NVIDIA GeForce GTX 950': 142,
 'NVIDIA GeForce GTX 850M': 261,
 'NVIDIA GeForce GTX 780M': 348,
 'NVIDIA GeForce GTX 770': 239,
 'NVIDIA GeForce GTX 760': 286,
 'NVIDIA GeForce GTX 750 Ti': 117,
 'NVIDIA GeForce GTX 750': 127,
 'NVIDIA GeForce GTX 660': 113,
 'NVIDIA GeForce GTX 650 Ti': 278,
 'NVIDIA GeForce GTX 650': 203,
 'NVIDIA GeForce GTX 550 Ti': 320,
 'NVIDIA GeForce GTX 4090': 349,
 'NVIDIA GeForce GTX 1660 Ti with Max-Q Design': 155,
 'NVIDIA GeForce GTX 1660 Ti': 22,
 'NVIDIA GeForce GTX 1660 SUPER': 76,
 'NVIDIA GeForce GTX 1660': 61,
 'NVIDIA GeForce GTX 1650 Ti': 11,
 'NVIDIA GeForce GTX 1650 SUPER': 178,
 'NVIDIA GeForce GTX 1650': 23,
 'NVIDIA GeForce GTX 1080 Ti': 55,
 'NVIDIA GeForce GTX 1080': 101,
 'NVIDIA GeForce GTX 1070 Ti': 60,
 'NVIDIA GeForce GTX 1070': 82,
 'NVIDIA GeForce GTX 1060 with Max-Q Design': 259,
 'NVIDIA GeForce GTX 1060 6GB': 109,
 'NVIDIA GeForce GTX 1060 5GB': 167,
 'NVIDIA GeForce GTX 1060 3GB': 148,
 'NVIDIA GeForce GTX 1060': 95,
 'NVIDIA GeForce GTX 1050 with Max-Q Design': 344,
 'NVIDIA GeForce GTX 1050 Ti with Max-Q Design': 358,
 'NVIDIA GeForce GTX 1050 Ti': 111,
 'NVIDIA GeForce GTX 1050': 106}