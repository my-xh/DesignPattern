from 克隆模式 import Clone


class AppConfig(Clone):
    """应用程序功能配置"""

    def __init__(self, config_name):
        self.__config_name = config_name
        self.parse_from_file('./config/default.xml')

    def parse_from_file(self, file_path):
        """从配置文件中解析配置项"""
        self.__font_type = '宋体'
        self.__font_size = 14
        self.__language = '中文'
        self.__log_path = './logs/app_exception.log'

    def save_to_file(self, file_path):
        """降配置保存到配置文件中"""
        pass

    def copy_config(self, config_name):
        """创建一个配置的副本"""
        config = self.deep_clone()
        config.__config_name = config_name
        return config

    def show_info(self):
        print(f'{self.__config_name} 的配置信息如下:')
        print(f'字体: {self.__font_type}')
        print(f'字号: {self.__font_size}')
        print(f'语言: {self.__language}')
        print(f'异常文件的路径: {self.__log_path}')

    def set_font_type(self, font_type):
        self.__font_type = font_type

    def set_font_size(self, font_size):
        self.__font_size = font_size

    def set_language(self, language):
        self.__language = language

    def set_log_path(self, log_path):
        self.__log_path = log_path


if __name__ == '__main__':
    default = AppConfig('default')
    default.show_info()
    print()

    new_config = default.copy_config('tony_config')
    new_config.set_font_type('雅黑')
    new_config.set_font_size(18)
    new_config.set_language('English')
    new_config.set_log_path('./logs/app_exception2.log')
    new_config.show_info()
