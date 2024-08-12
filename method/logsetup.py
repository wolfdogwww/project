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