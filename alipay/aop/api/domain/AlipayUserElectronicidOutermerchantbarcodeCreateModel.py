#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserElectronicidOutermerchantbarcodeCreateModel(object):

    def __init__(self):
        self._barcode_type = None
        self._expire_time = None
        self._merchant_type = None
        self._redirect_url = None

    @property
    def barcode_type(self):
        return self._barcode_type

    @barcode_type.setter
    def barcode_type(self, value):
        self._barcode_type = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode_type:
            if hasattr(self.barcode_type, 'to_alipay_dict'):
                params['barcode_type'] = self.barcode_type.to_alipay_dict()
            else:
                params['barcode_type'] = self.barcode_type
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserElectronicidOutermerchantbarcodeCreateModel()
        if 'barcode_type' in d:
            o.barcode_type = d['barcode_type']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        return o


