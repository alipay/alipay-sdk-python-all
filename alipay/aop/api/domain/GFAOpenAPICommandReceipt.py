#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GFAOpenAPICommandReceipt(object):

    def __init__(self):
        self._ext_info = None
        self._receipt_status = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def receipt_status(self):
        return self._receipt_status

    @receipt_status.setter
    def receipt_status(self, value):
        self._receipt_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.receipt_status:
            if hasattr(self.receipt_status, 'to_alipay_dict'):
                params['receipt_status'] = self.receipt_status.to_alipay_dict()
            else:
                params['receipt_status'] = self.receipt_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPICommandReceipt()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'receipt_status' in d:
            o.receipt_status = d['receipt_status']
        return o


