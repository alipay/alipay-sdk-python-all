#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMallEventSendModel(object):

    def __init__(self):
        self._biz_id = None
        self._data = None
        self._event_code = None
        self._product_code = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMallEventSendModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'data' in d:
            o.data = d['data']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


