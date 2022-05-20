from nb_log import LogManager,get_logger
from multiprocessing import Process
# logger = get_logger('日志器')
#
# logger.debug("绿色")
# logger.info('蓝色')
# logger.warn('黄色')
# logger.error('紫红色')
# logger.critical('血红色')
# print('print样式被自动发生变化')

logger = get_logger(name='日志器',is_add_stream_handler=True, log_filename='ha.log')

def f():
    for i in range(10):
        logger.warning('测试文件写入性能，在满足 1.多进程运行 2.按大小自动切割备份 3切割备份瞬间不出错'
                     '这3个条件的前提下，验证这是不是python史上文件写入速度遥遥领先 性能最强的python logging handler')

#
# if __name__ == '__main__':
#     [Process(target=f).start() for _ in range(10)]