#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationIsvQrcodeUnbindModel(object):

    def __init__(self):
        self._qrcode_url = None

    @property
    def qrcode_url(self):
        return self._qrcode_url

    @qrcode_url.setter
    def qrcode_url(self, value):
        self._qrcode_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.qrcode_url:
            if hasattr(self.qrcode_url, 'to_alipay_dict'):
                params['qrcode_url'] = self.qrcode_url.to_alipay_dict()
            else:
                params['qrcode_url'] = self.qrcode_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationIsvQrcodeUnbindModel()
        if 'qrcode_url' in d:
            o.qrcode_url = d['qrcode_url']
        return o


