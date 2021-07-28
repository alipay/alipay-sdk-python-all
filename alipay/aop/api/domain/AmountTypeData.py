#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZMGoOutDiscountInfo import ZMGoOutDiscountInfo
from alipay.aop.api.domain.ZMGoTradeInfo import ZMGoTradeInfo


class AmountTypeData(object):

    def __init__(self):
        self._name = None
        self._out_discount_infos = None
        self._trade_info = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_discount_infos(self):
        return self._out_discount_infos

    @out_discount_infos.setter
    def out_discount_infos(self, value):
        if isinstance(value, list):
            self._out_discount_infos = list()
            for i in value:
                if isinstance(i, ZMGoOutDiscountInfo):
                    self._out_discount_infos.append(i)
                else:
                    self._out_discount_infos.append(ZMGoOutDiscountInfo.from_alipay_dict(i))
    @property
    def trade_info(self):
        return self._trade_info

    @trade_info.setter
    def trade_info(self, value):
        if isinstance(value, ZMGoTradeInfo):
            self._trade_info = value
        else:
            self._trade_info = ZMGoTradeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_discount_infos:
            if isinstance(self.out_discount_infos, list):
                for i in range(0, len(self.out_discount_infos)):
                    element = self.out_discount_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_discount_infos[i] = element.to_alipay_dict()
            if hasattr(self.out_discount_infos, 'to_alipay_dict'):
                params['out_discount_infos'] = self.out_discount_infos.to_alipay_dict()
            else:
                params['out_discount_infos'] = self.out_discount_infos
        if self.trade_info:
            if hasattr(self.trade_info, 'to_alipay_dict'):
                params['trade_info'] = self.trade_info.to_alipay_dict()
            else:
                params['trade_info'] = self.trade_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmountTypeData()
        if 'name' in d:
            o.name = d['name']
        if 'out_discount_infos' in d:
            o.out_discount_infos = d['out_discount_infos']
        if 'trade_info' in d:
            o.trade_info = d['trade_info']
        return o


