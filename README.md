# Graphic CAPTCHA Strength Testing Demo



Base on BruteForce Testing & Tesserocr  & Tencent ocr open API

图形验证码强度测试Demo -- 基于暴力攻击 & Tesserocr & 腾讯ocr开放平台



```
├── auto					自动化测试demo
│   ├── auto.py				识别+验证流程自动化（需要有验证接口）
│   ├── pic							存放下载下来图片的目录
│   ├── processed			存放处理后的图片目录
│   ├── qq_recon.py			使用Tencent OCR开放接口进行识别测试
│   ├── random_brute_force_test.py		暴力攻击测试
│   ├── result.txt				结果输出
│   └── tesserocr_recon.py
├── manual				手动测试demo
│   ├── qq_recon.py		使用Tencent OCR开放接口进行识别测试
│   ├── pic						存放下载下来图片的目录
│   ├── processed		存放处理后的图片目录
│   └── real.txt			人工标记的正确值
└── readmd.md
```



## Declaration:



​	For study purpose only.



## 声明：



​	仅供学习使用。



