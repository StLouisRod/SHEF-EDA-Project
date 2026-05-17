from exception import USVisaException
import sys
try :
    a=10/0
except Exception as e:
    raise USVisaException(e,sys)
