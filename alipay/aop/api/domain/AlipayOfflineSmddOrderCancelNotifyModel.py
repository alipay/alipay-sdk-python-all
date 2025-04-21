#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CodeExtBean import CodeExtBean


class AlipayOfflineSmddOrderCancelNotifyModel(object):

    def __init__(self):
        self._buyer_id = None
        self._code_ext = None
        self._order_id = None
        self._shop_id = None
        self._type = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def code_ext(self):
        return self._code_ext

    @code_ext.setter
    def code_ext(self, value):
        if isinstance(value, CodeExtBean):
            self._code_ext = value
        else:
            self._code_ext = CodeExtBean.from_alipay_dict(value)
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.code_ext:
            if hasattr(self.code_ext, 'to_alipay_dict'):
                params['code_ext'] = self.code_ext.to_alipay_dict()
            else:
                params['code_ext'] = self.code_ext
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineSmddOrderCancelNotifyModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'code_ext' in d:
            o.code_ext = d['code_ext']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'type' in d:
            o.type = d['type']
        return o


