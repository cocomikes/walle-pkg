# App & walle

> 解决使用walle快速打出渠道包，再加固后，渠道信息丢失的问题

===


## 使用方法

- ProtectedApkResignerForWalle(https://github.com/Jay-Goo/ProtectedApkResignerForWalle/blob/master/README.md)
- 拷贝加固后未签名的 APK 到本项目根目录下
- 修改 `config.py`，按照注释改成自己项目配置
- 根据项目情况修改 `channel` 文件，以后扩展渠道时，我们只需要修改这个文件就好了
- 运行命令 `python ApkResigner.py`， 即可自动生成所有渠道包，之后我们可以在channles文件夹下看到生成的各种渠道包了。 

