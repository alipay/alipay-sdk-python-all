#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelBizData(object):

    def __init__(self):
        self._goods_info = None
        self._order_info = None
        self._order_no = None
        self._premium_factor = None

    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        self._goods_info = value
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        self._order_info = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def premium_factor(self):
        return self._premium_factor

    @premium_factor.setter
    def premium_factor(self, value):
        self._premium_factor = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_info:
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        if self.order_info:
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.premium_factor:
            if hasattr(self.premium_factor, 'to_alipay_dict'):
                params['premium_factor'] = self.premium_factor.to_alipay_dict()
            else:
                params['premium_factor'] = self.premium_factor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelBizData()
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        if 'order_info' in d:
            o.order_info = d['order_info']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'premium_factor' in d:
            o.premium_factor = d['premium_factor']
        return o


