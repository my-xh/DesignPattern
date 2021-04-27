class Register:
    """报到登记"""

    def register(self, name):
        print(f'活动中心: {name} 同学报到成功!')


class Payment:
    """缴费中心"""

    def pay(self, name, money):
        print(f'缴费中心: 收到 {name} 同学 {money} 元付款, 缴费成功!')


class DormitoryManagementCenter:
    """生活中心"""

    def provide_living_goods(self, name):
        print(f'生活中心: {name} 同学的生活用品已发放。')


class Dormitory:
    """宿舍"""

    def meet_roommate(self, name):
        print(f'宿舍: 大家好! 这是刚来的 {name} 同学, 是你们未来需要共度四年的室友! 相互认识一下……')


class Volunteer:
    """迎新志愿者"""

    def __init__(self, name):
        self.__name = name
        self.__register = Register()
        self.__payment = Payment()
        self.__life_center = DormitoryManagementCenter()
        self.__dormitory = Dormitory()

    @property
    def name(self):
        return self.__name

    def welcome_freshmen(self, name):
        print(f'你好, {name} 同学! 我是新生报到的志愿者 {self.name}, 我将带你完成整个报到流程。')
        self.__register.register(name)
        self.__payment.pay(name, 10000)
        self.__life_center.provide_living_goods(name)
        self.__dormitory.meet_roommate(name)


if __name__ == '__main__':
    volunteer = Volunteer('Frank')
    volunteer.welcome_freshmen('Tony')
