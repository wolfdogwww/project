#https://zx7978123.medium.com/python-logging-日誌管理教學-60be0a1a6005
import logging

def logsetup():
    FORMAT = '%(asctime)s %(levelname)s: %(message)s' #設定log檔案格式 tim ,日誌等級數值,訊息
    logging.basicConfig(level=logging.DEBUG, filename='LOG.log',filemode='a',format=FORMAT)

''' 
    logging.debug('Hello Debug')
    logging.info('Hello info')
    logging.warning('Hello WARNING') 
    logging.error('Hello ERROR')
    logging.critical('Hello CRITICAL')
'''