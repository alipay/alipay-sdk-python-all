#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderbillExpenseBatchqueryModel(object):

    def __init__(self):
        self._trade_no_list = None

    @property
    def trade_no_list(self):
        return self._trade_no_list

    @trade_no_list.setter
    def trade_no_list(self, value):
        if isinstance(value, list):
            self._trade_no_list = list()
            for i in value:
                self._trade_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.trade_no_list:
            if isinstance(self.trade_no_list, list):
                for i in range(0, len(self.trade_no_list)):
                    element = self.trade_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_no_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_no_list, 'to_alipay_dict'):
                params['trade_no_list'] = self.trade_no_list.to_alipay_dict()
            else:
                params['trade_no_list'] = self.trade_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniOrderbillExpenseBatchqueryModel()
        if 'trade_no_list' in d:
            o.trade_no_list = d['trade_no_list']
        return o


