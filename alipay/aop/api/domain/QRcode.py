#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QRcode(object):

    def __init__(self):
        self._card_id = None
        self._qrcode_url = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def qrcode_url(self):
        return self._qrcode_url

    @qrcode_url.setter
    def qrcode_url(self, value):
        self._qrcode_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
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
        o = QRcode()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'qrcode_url' in d:
            o.qrcode_url = d['qrcode_url']
        return o


