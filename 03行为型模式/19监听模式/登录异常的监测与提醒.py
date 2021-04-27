import time
from 监听模式 import Observer, Observable


class Account(Observable):
    """用户账户"""

    def __init__(self):
        super().__init__()
        self.__latest_ip = {}
        self.__latest_region = {}

    def login(self, name, ip, time):
        region = self.__get_region(ip)
        if self.__is_long_distance(name, region):
            self.notify_observers({
                'name': name,
                'ip': ip,
                'region': region,
                'time': time,
            })
        self.__latest_ip[name] = ip
        self.__latest_region[name] = region

    def __get_region(self, ip):
        """根据IP地址获取地区信息"""
        ip_regions = {
            '101.47.18.9': '浙江省杭州市',
            '67.218.147.69': '美国洛杉矶',
        }
        region = ip_regions.get(ip, '')
        return region

    def __is_long_distance(self, name, region):
        """计算本次登录与最近几次登录的地区差距"""
        latest_region = self.__latest_region.get(name)
        return latest_region is not None and latest_region != region


class SmsSender(Observer):
    """短信发送器"""

    def update(self, observable, object):
        time_msg = time.strftime(
            '%Y-%m-%d %H-%M-%S', time.gmtime(object["time"]))
        print(f'[短信发送] {object["name"]}您好！检测到您的账户可能登录异常。最近一次登录信息：')
        print(f'登陆地区：{object["region"]}  登录ip：{object["ip"]}  登录时间：{time_msg}')


class MailSender(Observer):
    """邮件发送器"""

    def update(self, observable, object):
        time_msg = time.strftime(
            '%Y-%m-%d %H-%M-%S', time.gmtime(object["time"]))
        print(f'[邮件发送] {object["name"]}您好！检测到您的账户可能登录异常。最近一次登录信息：')
        print(f'登陆地区：{object["region"]}  登录ip：{object["ip"]}  登录时间：{time_msg}')


if __name__ == '__main__':
    account = Account()
    account.add_observer(SmsSender())
    account.add_observer(MailSender())
    account.login('Tony', '101.47.18.9', time.time())
    account.login('Tony', '67.218.147.69', time.time())
