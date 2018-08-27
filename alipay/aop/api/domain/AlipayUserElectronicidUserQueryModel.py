#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserElectronicidUserQueryModel(object):

    def __init__(self):
        self._barcode = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserElectronicidUserQueryModel()
        if 'barcode' in d:
            o.barcode = d['barcode']
        return o


