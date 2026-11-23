#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenProductResSubscribeModel(object):

    def __init__(self):
        self._biz_request_id = None
        self._channel_code = None
        self._oid = None
        self._open_id = None
        self._product_code = None

    @property
    def biz_request_id(self):
        return self._biz_request_id

    @biz_request_id.setter
    def biz_request_id(self, value):
        self._biz_request_id = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_request_id:
            if hasattr(self.biz_request_id, 'to_alipay_dict'):
                params['biz_request_id'] = self.biz_request_id.to_alipay_dict()
            else:
                params['biz_request_id'] = self.biz_request_id
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.oid:
            if hasattr(self.oid, 'to_alipay_dict'):
                params['oid'] = self.oid.to_alipay_dict()
            else:
                params['oid'] = self.oid
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayOpenProductResSubscribeModel()
        if 'biz_request_id' in d:
            o.biz_request_id = d['biz_request_id']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'oid' in d:
            o.oid = d['oid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


