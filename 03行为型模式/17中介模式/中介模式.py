class HouseInfo:
    """房源信息"""

    def __init__(self, area, price, has_window, has_bashroom, has_kitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__has_window = has_window
        self.__has_bashroom = has_bashroom
        self.__has_kitchen = has_kitchen
        self.__address = address
        self.__owner = owner

    @property
    def owner(self):
        return self.__owner.name

    @property
    def address(self):
        return self.__address

    def show_info(self):
        print(f'面积：{self.__area} 平方米，',
              f'价格：{self.__price} 元，',
              f'窗户：{"有" if self.__has_window else "无"}，',
              f'卫生间：{self.__has_bashroom}，',
              f'厨房：{"有" if self.__has_kitchen else "无"}，',
              f'地址：{self.__address}，',
              f'房东：{self.owner if self.owner else ""}')


class HousingAgency:
    """房屋中介"""

    def __init__(self, name):
        self.__houseinfos = []
        self.__name = name

    @property
    def name(self):
        return self.__name

    def add_houseinfo(self, houseinfo):
        self.__houseinfos.append(houseinfo)

    def remove_houseinfo(self, houseinfo):
        for info in self.__houseinfos[::-1]:
            if info == houseinfo:
                self.__houseinfos.remove(info)

    def get_search_condition(self, description):
        """将用户描述信息转换成搜索条件"""
        return description

    def get_match_infos(self, search_condition):
        """根据房源信息的各个属性查找最匹配的信息"""
        print(f'{self.name} 为您找到以下最适合的房源：')
        for info in self.__houseinfos:
            info.show_info()
        return self.__houseinfos

    def sign_contract(self, houseinfo, period):
        """与房东签订合同"""
        print(f'{self.name} 与房东 {houseinfo.owner} 签订 {houseinfo.address} 的房子的租赁合同，',
              f'租期 {period} 年。合同期间，{self.name} 有权对其进行使用和转租！')

    def sign_contracts(self, period):
        for info in self.__houseinfos:
            self.sign_contract(info, period)


class HouseOwner:
    """房东"""

    def __init__(self, name):
        self.__name = name
        self.__houseinfo = None

    @property
    def name(self):
        return self.__name

    def set_houseinfo(self, area, price, has_window, has_bashroom, has_kitchen, address):
        self.__houseinfo = HouseInfo(
            area, price, has_window, has_bashroom, has_kitchen, address, self)

    def publish_houseinfo(self, agency):
        agency.add_houseinfo(self.__houseinfo)
        print(f'{self.name} 在 {agency.name} 发布房源出租信息：')
        self.__houseinfo.show_info()


class Customer:
    """租房用户"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def find_house(self, description, agency):
        print(f'我是 {self.name}，我想要找一个"{description}"的房子')
        return agency.get_match_infos(agency.get_search_condition(description))

    def see_house(self, houseinfos):
        n = len(houseinfos)
        return houseinfos[n - 1]

    def sign_contract(self, houseinfo, agency, period):
        """与中介签订合同"""
        print(f'{self.name} 与中介 {agency.name} 签订 {houseinfo.address} 的房子的租赁合同，',
              f'租期 {period} 年。合同期间，{self.name} 有权对其进行使用！')


if __name__ == '__main__':
    my_home = HousingAgency('我爱我家')
    zhangsan = HouseOwner('张三')
    zhangsan.set_houseinfo(20, 2500, 1, '独立卫生间', 0, '上地西里')
    zhangsan.publish_houseinfo(my_home)
    lisi = HouseOwner('李四')
    lisi.set_houseinfo(16, 1800, 1, '公用卫生间', 0, '当代城市家园')
    lisi.publish_houseinfo(my_home)
    wangwu = HouseOwner('王五')
    wangwu.set_houseinfo(18, 2600, 1, '独立卫生间', 1, '金隅美和园')
    wangwu.publish_houseinfo(my_home)
    print()
    my_home.sign_contracts(3)
    print()
    tony = Customer('Tony')
    houseinfos = tony.find_house(
        '18 平方米左右，要有独立卫生间，要有窗户，最好朝南，有厨房更好！价位在2000元左右', my_home)
    print()
    appropriate_house = tony.see_house(houseinfos)
    tony.sign_contract(appropriate_house, my_home, 1)
