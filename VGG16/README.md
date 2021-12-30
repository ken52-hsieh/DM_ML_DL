---
title: VGG-16 study note
date: Dec 09, 2021
tags:
  - VGG16
  - Deep Learning
  - image regression
---
#### 前言

VGG是由Simonyan 和Zisserman在文獻《Very Deep Convolutional Networks for Large Scale Image Recognition》中提出卷積神經網絡模型，其名稱來源於作者所在的牛津大學視覺幾何組(Visual Geometry Group)的縮寫。

該模型參加2014年的 ImageNet圖像分類與定位挑戰賽，取得了優異成績：在分類任務上排名第二，在定位任務上排名第一。

#### Keras vs Pytroch

目前對使用者比較友善且具備靈活性的Deep Learning框架主要為**Keras**與**Pytroch**, 並且各自有背後(底層)的支持, 因此分別以兩種框架進行簡單的image regression task測試

1. **Keras**

參考[VGG16学习笔记](http://deanhan.com/2018/07/26/vgg16/), 辨識結果並不理想
- [x] 虎斑貓
- [ ] 仙人掌 (辨識成綠色的房子)
- [ ] 大腦 (辨識成羊毛)

2. **Pytroch**



#### Appendix - Reference
1. [Accelerating Very Deep Convolutional Networks for Classification and Detection](https://arxiv.org/abs/1505.06798)
2. [GitHub example](https://gist.github.com/baraldilorenzo/07d7802847aaad0a35d3)
