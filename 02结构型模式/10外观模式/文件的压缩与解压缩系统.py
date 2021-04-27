import os
import logging


class ZIPModel:
    """ZIP模块, 负责ZIP文件的压缩与解压缩"""

    def compress(self, src_file_path, dst_file_path):
        print(f'ZIP模块正在进行 {src_file_path} 文件的压缩......')
        print(f'文件压缩成功, 已保存至 {dst_file_path}')

    def decompress(self, src_file_path, dst_file_path):
        print(f'ZIP模块正在进行 {src_file_path} 文件的解压缩......')
        print(f'文件解压缩成功, 已保存至 {dst_file_path}')


class RARModel:
    """RAR模块, 负责RAR文件的压缩与解压缩"""

    def compress(self, src_file_path, dst_file_path):
        print(f'RAR模块正在进行 {src_file_path} 文件的压缩......')
        print(f'文件压缩成功, 已保存至 {dst_file_path}')

    def decompress(self, src_file_path, dst_file_path):
        print(f'RAR模块正在进行 {src_file_path} 文件的解压缩......')
        print(f'文件解压缩成功, 已保存至 {dst_file_path}')


class ZModel:
    """7Z模块, 负责7Z文件的压缩与解压缩"""

    def compress(self, src_file_path, dst_file_path):
        print(f'7Z模块正在进行 {src_file_path} 文件的压缩......')
        print(f'文件压缩成功, 已保存至 {dst_file_path}')

    def decompress(self, src_file_path, dst_file_path):
        print(f'7Z模块正在进行 {src_file_path} 文件的解压缩......')
        print(f'文件解压缩成功, 已保存至 {dst_file_path}')


class CompressionFacade:
    """压缩系统的外观类"""

    def __init__(self):
        self.__zip_model = ZIPModel()
        self.__rar_model = RARModel()
        self.__7z_model = ZModel()

    def compress(self, src_file_path, dst_file_path, _type):
        """根据不同的压缩类型，压缩成不同的格式"""
        ext = '.' + _type
        full_name = dst_file_path + ext
        if _type.lower() == 'zip':
            self.__zip_model.compress(src_file_path, full_name)
        elif _type.lower() == 'rar':
            self.__rar_model.compress(src_file_path, full_name)
        elif _type.lower() == '7z':
            self.__7z_model.compress(src_file_path, full_name)
        else:
            logging.error(f'Not support this format: {_type}')
            return False
        return True

    def decompress(self, src_file_path, dst_file_path):
        """从 src_file_path 中获取后缀, 根据不用的后缀名, 进行不同格式的解压缩"""
        base_name = os.path.basename(src_file_path)
        ext = base_name.split('.')[1]
        if ext.lower() == 'zip':
            self.__zip_model.decompress(src_file_path, dst_file_path)
        elif ext.lower() == 'rar':
            self.__rar_model.decompress(src_file_path, dst_file_path)
        elif ext.lower() == '7z':
            self.__7z_model.decompress(src_file_path, dst_file_path)
        else:
            logging.error(f'Not support this format: {ext}')
            return False
        return True


if __name__ == '__main__':
    facade = CompressionFacade()
    facade.compress(r'E:\标准文件\生活中的外观模式.md', r'E:\压缩文件\生活中的外观模式', 'zip')
    facade.decompress(r'E:\压缩文件\生活中的外观模式.zip', r'E:\标准文件\生活中的外观模式.md')
    print()

    facade.compress(r'E:\标准文件\Python编程——从入门到实践.pdf',
                    r'E:\压缩文件\Python编程——从入门到实践', 'rar')
    facade.decompress(r'E:\压缩文件\Python编程——从入门到实践.rar',
                      r'E:\标准文件\Python编程——从入门到实践.pdf')
    print()

    facade.compress(r'E:\标准文件\谈谈我对项目重构的看法.doc', r'E:\压缩文件\谈谈我对项目重构的看法', '7z')
    facade.decompress(r'E:\压缩文件\谈谈我对项目重构的看法.7z', r'E:\标准文件\谈谈我对项目重构的看法.doc')
