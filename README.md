用 Python 实现的 Pixiv 爬虫，支持批量下载和上传。

随机图片 API: <https://loliapi.ml/>

## Deploy

**Github Action 集成部署**

建议使用本方法部署，相较于本地部署，无需搭建环境，全程在线上完成。并且使用国外服务器下载、上传，网络更加通畅。

1. Fork 本项目，并给这个 repo 一颗小星星。
2. 点击 Actions 选项卡，开启 Github Action。
3. 新建一个 Token，需要 `repo` 权限。
4. 在仓库的 Settings --> Secrets 中新建秘钥 `personal_token`，填写你的 Github Token。
5. 若要立即看到效果，请随意修改 `main` 分支，触发 Github Action。

**本地部署**

1. 下载本项目，并给这个 repo 一颗小星星。
2. 安装好 `wget`， `pip` 库 `requests`。
3. 用 Python 3 运行 `main.py`，默认上传到图床 SM.MS。

## Customize

**R-18**

修改 `main.py` 中的 `url`，如下

```python3
url = 'http://api.lolicon.app/setu/v2?r18=1'
```

P.S. 这并不是严格意义上的 R-18，详见 [API 文档](https://api.lolicon.app/#/setu)。

**图床**

默认使用 [SM.MS](https://sm.ms/) 图床。因为 Github Action 单次运行是新建一个完全不同的虚拟化环境，所以可以绕过图床的每日上传限制。

理论上可以自己根据图床提供的 API 来修改，但是经过作者的尝试，只有 SM.MS 支持 pixiv 大多数尺度的照片。国内的部分图床（例如[去不图床](https://7bu.top)）不允许上传此类图片。

**图片类型**

请阅读 API 文档，修改 `main.py` 中的 `url`。

## To Do

- repo 主想要实现的功能好像都在了呢~ 提个 issue 吧

## Thanks

API: <https://api.lolicon.app/#/setu>

## Warning

所有图片均来自 Pixiv，版权也归作品的作者所有。本项目只是出于兴趣爱好和研究用途搭建，严禁将本项目爬取的照片用于商业用途！

若您是未成年人，请自觉抵制 R-18 和露骨内容，遵守您所处国家的法律法规，谢谢配合！
