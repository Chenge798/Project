工具是kali自带，多用于网站的后台扫描

工具路径：/usr/share/dirbuster

cd /usr/share/dirbuster进入路径后ls查看，会看到目录下的jar文件:

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128105941938.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)


2. java -jar DirBuster-1.0-RC1.jar 打开jar文件
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128110205418.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

  

3. 出现可视化窗口，配置很多，现在我们先填写空白的输入框部分，这里我们在第一个输入框填写扫描网站的url地址

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128110611807.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

4. 第二个输入框是使用字典，我们点击browse按钮查找
  

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128110715996.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

5. 出现字典的查找路径，进入第二个

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128110838839.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

6. 默认自带的字典如下，这里为了快速演示选择了一个轻量级的字典

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128110953772.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

7. 配置好后会显示如下

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128111123839.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

8. 我们点击url fuzz

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128111226709.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

9. 最下方的输入框追加上{dir}

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128111322843.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

10. 开始扫描

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128111347343.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

11. 进入扫描窗口，我们点击第二个查看

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128111641429.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128111813128.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

12. 从response响应上来看，返回值200的路径应该是可以访问的，第一个是/本目录可以忽略，第二个/wp-content/可以直接追加上试一试

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128112014925.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

13. 发现是空白页面，排除，继续往下看，发现返回302的几个字典名称为/login和/admin，这几个是常用的网站后台路径，所以也输入尝试一下

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128112248253.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

14. 这里我的确输入了login，但url自动跳转到后台的登录页面了，接下来用admin试试，发现也可以

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128112406213.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)

15. 经过测试发现，返回值为302的这几个路径都是可以直接访问到后台登录界面的

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128112631607.png)

16. 当然这样扫描速度是比较慢的，届时记得把线程调大一些
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200128112847622.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlZWVlbGV0ZQ==,size_16,color_FFFFFF,t_70)
