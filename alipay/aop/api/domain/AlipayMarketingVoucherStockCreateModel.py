#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingVoucherStockCreateModel(object):

    def __init__(self):
        self._entity_list = None
        self._out_biz_no = None
        self._stock_id = None

    @property
    def entity_list(self):
        return self._entity_list

    @entity_list.setter
    def entity_list(self, value):
        if isinstance(value, list):
            self._entity_list = list()
            for i in value:
                self._entity_list.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def stock_id(self):
        return self._stock_id

    @stock_id.setter
    def stock_id(self, value):
        self._stock_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_list:
            if isinstance(self.entity_list, list):
                for i in range(0, len(self.entity_list)):
                    element = self.entity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entity_list[i] = element.to_alipay_dict()
            if hasattr(self.entity_list, 'to_alipay_dict'):
                params['entity_list'] = self.entity_list.to_alipay_dict()
            else:
                params['entity_list'] = self.entity_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.stock_id:
            if hasattr(self.stock_id, 'to_alipay_dict'):
                params['stock_id'] = self.stock_id.to_alipay_dict()
            else:
                params['stock_id'] = self.stock_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingVoucherStockCreateModel()
        if 'entity_list' in d:
            o.entity_list = d['entity_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'stock_id' in d:
            o.stock_id = d['stock_id']
        return o


