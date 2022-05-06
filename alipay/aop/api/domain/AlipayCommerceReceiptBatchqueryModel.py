#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceReceiptBatchqueryModel(object):

    def __init__(self):
        self._level = None
        self._out_biz_no_list = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def out_biz_no_list(self):
        return self._out_biz_no_list

    @out_biz_no_list.setter
    def out_biz_no_list(self, value):
        if isinstance(value, list):
            self._out_biz_no_list = list()
            for i in value:
                self._out_biz_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.out_biz_no_list:
            if isinstance(self.out_biz_no_list, list):
                for i in range(0, len(self.out_biz_no_list)):
                    element = self.out_biz_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_biz_no_list[i] = element.to_alipay_dict()
            if hasattr(self.out_biz_no_list, 'to_alipay_dict'):
                params['out_biz_no_list'] = self.out_biz_no_list.to_alipay_dict()
            else:
                params['out_biz_no_list'] = self.out_biz_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceReceiptBatchqueryModel()
        if 'level' in d:
            o.level = d['level']
        if 'out_biz_no_list' in d:
            o.out_biz_no_list = d['out_biz_no_list']
        return o


