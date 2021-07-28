#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BarcodeInfoVO(object):

    def __init__(self):
        self._barcode = None
        self._barcode_type = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def barcode_type(self):
        return self._barcode_type

    @barcode_type.setter
    def barcode_type(self, value):
        self._barcode_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.barcode_type:
            if hasattr(self.barcode_type, 'to_alipay_dict'):
                params['barcode_type'] = self.barcode_type.to_alipay_dict()
            else:
                params['barcode_type'] = self.barcode_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BarcodeInfoVO()
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'barcode_type' in d:
            o.barcode_type = d['barcode_type']
        return o


