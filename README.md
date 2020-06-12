# walle-pkg

> 使用 walle 快速打出千奇百怪的渠道包！

- 已升级walle-cli-all-android-Q.jar ，解决 Android P 系统无法安装经 walle 打包后的 APK 问题。

===


## 使用方法

- ProtectedApkResignerForWalle(https://github.com/Jay-Goo/ProtectedApkResignerForWalle/blob/master/README.md)
- 拷贝加固后未签名的 APK 到本项目根目录下
- 修改 `config.py`，按照注释改成自己项目配置
- 根据项目情况修改 `channel` 文件，以后扩展渠道时，我们只需要修改这个文件就好了
- 运行命令 `python ApkResigner.py`， 即可自动生成所有渠道包，之后我们可以在channles文件夹下看到生成的各种渠道包了。 

=======
