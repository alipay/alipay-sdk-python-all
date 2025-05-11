#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantMultiendserviceprodQrcodeMatchModel(object):

    def __init__(self):
        self._qrcode_value = None

    @property
    def qrcode_value(self):
        return self._qrcode_value

    @qrcode_value.setter
    def qrcode_value(self, value):
        self._qrcode_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.qrcode_value:
            if hasattr(self.qrcode_value, 'to_alipay_dict'):
                params['qrcode_value'] = self.qrcode_value.to_alipay_dict()
            else:
                params['qrcode_value'] = self.qrcode_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantMultiendserviceprodQrcodeMatchModel()
        if 'qrcode_value' in d:
            o.qrcode_value = d['qrcode_value']
        return o


