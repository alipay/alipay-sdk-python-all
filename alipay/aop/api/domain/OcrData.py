#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OcrData(object):

    def __init__(self):
        self._ocr_data_key = None
        self._ocr_data_value = None

    @property
    def ocr_data_key(self):
        return self._ocr_data_key

    @ocr_data_key.setter
    def ocr_data_key(self, value):
        self._ocr_data_key = value
    @property
    def ocr_data_value(self):
        return self._ocr_data_value

    @ocr_data_value.setter
    def ocr_data_value(self, value):
        self._ocr_data_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.ocr_data_key:
            if hasattr(self.ocr_data_key, 'to_alipay_dict'):
                params['ocr_data_key'] = self.ocr_data_key.to_alipay_dict()
            else:
                params['ocr_data_key'] = self.ocr_data_key
        if self.ocr_data_value:
            if hasattr(self.ocr_data_value, 'to_alipay_dict'):
                params['ocr_data_value'] = self.ocr_data_value.to_alipay_dict()
            else:
                params['ocr_data_value'] = self.ocr_data_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OcrData()
        if 'ocr_data_key' in d:
            o.ocr_data_key = d['ocr_data_key']
        if 'ocr_data_value' in d:
            o.ocr_data_value = d['ocr_data_value']
        return o


