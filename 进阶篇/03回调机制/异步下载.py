import requests
from threading import Thread


class DownloadThread(Thread):
    """下载文件的线程"""

    # 每次写文件的缓冲大小
    CHUNK_SIZE = 512 * 1024

    def __init__(self, file_name, url, save_path, callback_progress, callback_finished):
        super().__init__()
        self.__file_name = file_name
        self.__url = url
        self.__save_path = save_path
        self.__callback_progress = callback_progress
        self.__callback_finished = callback_finished

    def run(self):
        read_size = 0
        r = requests.get(self.__url)
        total_size = int(r.headers.get('Content-Length'))
        print(f'[下载{self.__file_name}] 文件大小: {total_size}')
        with open(f'{self.__save_path}', 'wb') as f:
            for chunk in r.iter_content(chunk_size=self.CHUNK_SIZE):
                read_size += f.write(chunk)
                self.__callback_progress(
                    self.__file_name, read_size, total_size)
        self.__callback_finished(self.__file_name)


def download_progress(file_name, read_size, total_size):
    """下载进度的回调函数"""
    percent = read_size / total_size * 100
    print(f'[下载{file_name}] 下载进度: {percent:.2f}%')


def download_finished(file_name):
    """下载完成的回调函数"""
    print(f'[下载{file_name}] 文件下载完成!')


if __name__ == '__main__':
    print('开始下载TestForDownload1.pdf......')
    download_url_1 = 'http://pe9hg91q8.bkt.clouddn.com/TestForDownload1.pdf'
    download_1 = DownloadThread('TestForDownload1.pdf', download_url_1,
                                './download/TestForDownload1.pdf', download_progress, download_finished)
    download_1.start()
    print('开始TestForDownload2.pdf......')
    download_url_2 = 'http://pe9hg91q8.bkt.clouddn.com/TestForDownload2.pdf'
    download_2 = DownloadThread('TestForDownload2.pdf', download_url_2,
                                './download/TestForDownload2.pdf', download_progress, download_finished)
    download_2.start()
    print('执行其他的任务......')
