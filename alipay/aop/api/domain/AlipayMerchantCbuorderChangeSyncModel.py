#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantCbuorderChangeSyncModel(object):

    def __init__(self):
        self._biz_source = None
        self._change_data = None
        self._change_time = None
        self._order_id = None

    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def change_data(self):
        return self._change_data

    @change_data.setter
    def change_data(self, value):
        self._change_data = value
    @property
    def change_time(self):
        return self._change_time

    @change_time.setter
    def change_time(self, value):
        self._change_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.change_data:
            if hasattr(self.change_data, 'to_alipay_dict'):
                params['change_data'] = self.change_data.to_alipay_dict()
            else:
                params['change_data'] = self.change_data
        if self.change_time:
            if hasattr(self.change_time, 'to_alipay_dict'):
                params['change_time'] = self.change_time.to_alipay_dict()
            else:
                params['change_time'] = self.change_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantCbuorderChangeSyncModel()
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'change_data' in d:
            o.change_data = d['change_data']
        if 'change_time' in d:
            o.change_time = d['change_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


