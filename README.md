# github-action快速接入 只需网页端fork仓库&设置仓库secret对
1. 获取form信息
- 使用方法和以前一样，https://app.buaa.edu.cn/site/buaaStudentNcov/index
- 填好之后打开控制台Internet选项，提交后查看save-负载-查看源  将xxx=xxx&...所有内容复制起来作为FORM添加到secret
2. fork仓库&设置secrets.YOUR_NAME 和 secrets.YOUR_PWD
3. 参考Actions页，若提示enable则点击，github自动执行 也可手动触发测试

（如果不是打卡时间可能提交不了form，form可以参考使用这个-信息是我在大运村的，共用也能打上卡）
```
sfzs=1&bzxyy=&bzxyy_other=&brsfzc=1&tw=&sfcxzz=&zdjg=&zdjg_other=&sfgl=&gldd=&gldd_other=&glyy=&glyy_other=&gl_start=&gl_end=&sfmqjc=&sfzc_14=1&sfqw_14=0&sfqw_14_remark=&sfzgfx=0&sfzgfx_remark=&sfjc_14=0&sfjc_14_remark=&sfjcqz_14=0&sfjcqz_14_remark=&sfgtjz_14=0&sfgtjz_14_remark=&szsqqz=0&sfyqk=&szdd=1&area=%E5%8C%97%E4%BA%AC%E5%B8%82%20%E6%B5%B7%E6%B7%80%E5%8C%BA&city=%E5%8C%97%E4%BA%AC%E5%B8%82&province=%E5%8C%97%E4%BA%AC%E5%B8%82&address=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E8%8A%B1%E5%9B%AD%E8%B7%AF%E8%A1%97%E9%81%93%E8%80%81%E9%BA%BB%E6%8A%84%E6%89%8B%28%E7%9F%A5%E6%98%A5%E8%B7%AF%E5%BA%97%29%E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%A4%A7%E8%BF%90%E6%9D%91%E5%AD%A6%E7%94%9F%E5%85%AC%E5%AF%93&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22Q%22%3A39.977510579428%2C%22R%22%3A116.34294786241401%2C%22lng%22%3A116.342948%2C%22lat%22%3A39.977511%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get%20ipLocation%20failed.Get%20geolocation%20success.Convert%20Success.Get%20address%20success.%22%2C%22accuracy%22%3A90%2C%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22010%22%2C%22adcode%22%3A%22110108%22%2C%22businessAreas%22%3A%5B%7B%22name%22%3A%22%E5%A4%A7%E9%92%9F%E5%AF%BA%E6%9D%91%22%2C%22id%22%3A%22110108%22%2C%22location%22%3A%7B%22Q%22%3A39.965569%2C%22R%22%3A116.339877%2C%22lng%22%3A116.339877%2C%22lat%22%3A39.965569%7D%7D%2C%7B%22name%22%3A%22%E4%BA%94%E9%81%93%E5%8F%A3%22%2C%22id%22%3A%22110108%22%2C%22location%22%3A%7B%22Q%22%3A39.99118%2C%22R%22%3A116.34157800000003%2C%22lng%22%3A116.341578%2C%22lat%22%3A39.99118%7D%7D%2C%7B%22name%22%3A%22%E5%8F%8C%E6%A6%86%E6%A0%91%22%2C%22id%22%3A%22110108%22%2C%22location%22%3A%7B%22Q%22%3A39.971882%2C%22R%22%3A116.32657599999999%2C%22lng%22%3A116.326576%2C%22lat%22%3A39.971882%7D%7D%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E7%9F%A5%E6%98%A5%E8%B7%AF%22%2C%22streetNumber%22%3A%2229%E5%8F%B7%E9%99%A2%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%22%2C%22city%22%3A%22%22%2C%22district%22%3A%22%E6%B5%B7%E6%B7%80%E5%8C%BA%22%2C%22towncode%22%3A%22110108018000%22%2C%22township%22%3A%22%E8%8A%B1%E5%9B%AD%E8%B7%AF%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E8%8A%B1%E5%9B%AD%E8%B7%AF%E8%A1%97%E9%81%93%E8%80%81%E9%BA%BB%E6%8A%84%E6%89%8B%28%E7%9F%A5%E6%98%A5%E8%B7%AF%E5%BA%97%29%E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%A4%A7%E8%BF%90%E6%9D%91%E5%AD%A6%E7%94%9F%E5%85%AC%E5%AF%93%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&gwdz=&is_move=0&move_reason=&move_remark=&realname=%E6%9D%A8%E6%96%87%E5%93%B2&number=SY2002220&uid=401394&created=1653737805&date=20220528&id=13260932&gwszdd=
```

# + 自动提交出校申请
原理： 依赖于web版提交抓包https://app.buaa.edu.cn/site/applicationSquare/index?sid=16，也可通过手机+fiddler+端口代理抓包解析
- 见check_v2.py中新增函数，其中日期默认是第二天凌晨的核酸+打第三天的假，截图随便传了一张，由于自动审批不会校验，所以无所谓，原因为出校就医，需要修改名字及学号为自己的


# 补充
通过github的action自动执行，但时间有10-40min延迟，调试时可以手动执行测试，之后每天github会自动执行。

## 版权

使用 MIT 协议发布，著作权由代码的贡献者所有。
