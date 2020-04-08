为了兼容 Docker，默认的 sqlite 数据库生成在项目根目录的 database 目录下，因此在生成数据库之前需要确保项目根目录下 database 文件夹的存在。否则在生成数据库时会报错：

```
django.db.utils.OperationalError: unable to open database file
```

如果使用 MySQL、PostgreSQL 等数据库引擎，则 database 文件夹可有可无。