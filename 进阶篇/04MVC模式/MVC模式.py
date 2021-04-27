import random


class Image:
    """图像"""

    def __init__(self, width, height, pixels):
        self.__width = width
        self.__height = height
        self.__pixels = pixels

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def pixels(self):
        return self.__pixels


class Lens:
    """镜头"""

    def __init__(self):
        self.__focus_mode = ''
        self.__scenes = {0: '风光', 1: '生态', 2: '人文', 3: '纪实', 4: '人像', 5: '建筑'}

    def set_focus(self, focus_mode):
        self.__focus_mode = focus_mode

    def collecting(self):
        """图像采集，采用随机的方式来模拟自然的拍摄过程"""
        print(f'采集光线，{self.__focus_mode}')
        index = random.randint(0, len(self.__scenes) - 1)
        scenes = self.__scenes[index]
        return f'美丽的 {scenes} 图像'


class Display:
    """显示器"""

    def show_image(self, image):
        print(f'图片大小: {image.width} × {image.height}, 图片内容: {image.pixels}')


class SDCard:
    """SD存储卡"""

    def __init__(self):
        self.__images = []

    def add_image(self, image):
        print('存储图片')
        self.__images.append(image)

    def get_image(self, index):
        if 0 <= index < len(self.__images):
            return self.__images[index]
        else:
            return None


class Camera:
    """相机机身"""

    # 对焦类型
    SingleFocus = '单点对焦'
    AreaFocus = '区域对焦'
    BigAreaFocus = '大区域对焦'
    Focus45 = '45点自动对焦'

    def __init__(self, name):
        self.__name = name
        self.__aperture = 0.0           # 光圈
        self.__shutter_speed = 0        # 快门速度
        self.__light_sensitivity = 0    # 感光度
        self.__lens = Lens()            # 镜头
        self.__sd_card = SDCard()       # SD卡
        self.__display = Display()      # 显示器

    def shooting(self):
        """拍照"""
        print('[开始拍摄中')
        image_lighting = self.__lens.collecting()
        image = self._transfer_image(image_lighting)
        self.__sd_card.add_image(image)
        print('拍摄完成]')

    def view_image(self, index):
        """查看图像"""
        print(f'查看第 {index + 1} 张图片')
        image = self.__sd_card.get_image(index)
        if image is not None:
            self.__display.show_image(image)

    def _transfer_image(self, image_lighting):
        """接收光线并处理成数字信号，简单模拟"""
        print('接收光线并处理成数字信号')
        return Image(6000, 4000, image_lighting)

    def setting(self, aperture, shutter_speed, light_sensitivity):
        """设置相机的拍摄属性：光圈、快门速度、感光度"""
        self.__aperture = aperture
        self.__shutter_speed = shutter_speed
        self.__light_sensitivity = light_sensitivity

    def focusing(self, focus_mode):
        """对焦，要通关镜头来调节焦点"""
        self.__lens.set_focus(focus_mode)

    def show_info(self):
        """显示相机的属性"""
        print(f'{self.__name} 的设置  光圈: F{self.__aperture}  快门: 1/{self.__shutter_speed}  感光度: ISO {self.__light_sensitivity}')


if __name__ == '__main__':
    camera = Camera('EOS 80D')
    camera.setting(3.5, 60, 200)
    camera.show_info()
    camera.focusing(Camera.BigAreaFocus)
    camera.shooting()
    print()
    camera.setting(5.6, 720, 100)
    camera.show_info()
    camera.focusing(Camera.Focus45)
    camera.shooting()
    print()
    camera.view_image(0)
    camera.view_image(1)
