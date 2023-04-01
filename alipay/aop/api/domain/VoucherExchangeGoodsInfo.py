#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherExchangeGoodsInfo(object):

    def __init__(self):
        self._exchange_goods_name = None

    @property
    def exchange_goods_name(self):
        return self._exchange_goods_name

    @exchange_goods_name.setter
    def exchange_goods_name(self, value):
        self._exchange_goods_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.exchange_goods_name:
            if hasattr(self.exchange_goods_name, 'to_alipay_dict'):
                params['exchange_goods_name'] = self.exchange_goods_name.to_alipay_dict()
            else:
                params['exchange_goods_name'] = self.exchange_goods_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherExchangeGoodsInfo()
        if 'exchange_goods_name' in d:
            o.exchange_goods_name = d['exchange_goods_name']
        return o


