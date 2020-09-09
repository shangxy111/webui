import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.image import MIMEImage
from pom.common.logger import Logger

class StmpMail() :

    def send(self):
        html = """
        <p>python自动化测试用例报告，请下载附件查看</p>
        """
        message = MIMEMultipart('related')  # MIME邮件中除了可以携带各种附件外，还可以将其它内容以内嵌资源的方式存储在邮件中
        msgAlternative = MIMEMultipart('alternative')  # ，MIME邮件中同时存在纯文本和超文本考虑兼容性
        message.attach(msgAlternative)
        msgAlternative.attach(MIMEText(_text=html, _subtype='html', _charset='utf-8'))
        # 失败图片附件发送
        img_dir = '../case_unit/img/'
        if os.path.exists(img_dir) :
            #遍历目录下的文件名
            for fileName in os.listdir(img_dir):
                #拼接图片路径
                img_path = os.path.join(img_dir, fileName)
                #读取图片信息
                with open(img_path, 'rb') as imgfile:
                    imgObj = MIMEImage(imgfile.read())
                    #附件形式添加
                    imgObj["Content-Type"] = 'application/octet-stream'
                    imgObj["Content-Disposition"] = 'attachment;filename="error.png"'
                    message.attach(imgObj)

        #报告存放路径
        report_path = '../case_unit/beatifulReport/report.html'
        # 读取报告，并以附件的形式在邮件中追加
        with open(report_path, 'rb+') as file1:
            att1 = MIMEText(file1.read(), "base64", "utf-8")
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment;filename="report.html"'
            message.attach(att1)

        #进行发送邮件操作
        try:
            my_sender = "xxx@qq.com"  # 发件人
            recevier = "xxx@qq.com"  # 收件人
            to_acc = 'shangxiaoyu736@163.com'  # 抄送人
            message["From"] = formataddr(['xxx', my_sender])
            message["To"] = formataddr(['xxx', recevier])
            message["Cc"] = to_acc
            message["Subject"] = Header('邮件主题', 'utf-8')
            #创建邮件发送服务器SMTP对象
            smtpObj = smtplib.SMTP()
            #建立连接，进行通信
            smtpObj.connect(host="smtp.qq.com", port="587")
            #邮箱授权码认证
            smtpObj.login(user='xxx@qq.com', password='xxx')
            #发送邮件
            smtpObj.sendmail(my_sender, [recevier, to_acc], message.as_string())
        except smtplib.SMTPException as error:
            Logger().get_logger().info("邮件发送失败：%s"% error)