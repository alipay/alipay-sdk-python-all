#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessProduceQrcode(object):

    def __init__(self):
        self._batch_id = None
        self._core_url = None
        self._produce_order_id = None
        self._qrcode = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def core_url(self):
        return self._core_url

    @core_url.setter
    def core_url(self, value):
        self._core_url = value
    @property
    def produce_order_id(self):
        return self._produce_order_id

    @produce_order_id.setter
    def produce_order_id(self, value):
        self._produce_order_id = value
    @property
    def qrcode(self):
        return self._qrcode

    @qrcode.setter
    def qrcode(self, value):
        self._qrcode = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.core_url:
            if hasattr(self.core_url, 'to_alipay_dict'):
                params['core_url'] = self.core_url.to_alipay_dict()
            else:
                params['core_url'] = self.core_url
        if self.produce_order_id:
            if hasattr(self.produce_order_id, 'to_alipay_dict'):
                params['produce_order_id'] = self.produce_order_id.to_alipay_dict()
            else:
                params['produce_order_id'] = self.produce_order_id
        if self.qrcode:
            if hasattr(self.qrcode, 'to_alipay_dict'):
                params['qrcode'] = self.qrcode.to_alipay_dict()
            else:
                params['qrcode'] = self.qrcode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessProduceQrcode()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'core_url' in d:
            o.core_url = d['core_url']
        if 'produce_order_id' in d:
            o.produce_order_id = d['produce_order_id']
        if 'qrcode' in d:
            o.qrcode = d['qrcode']
        return o


