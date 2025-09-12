#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleSubOrderAfterSaleInfoVO(object):

    def __init__(self):
        self._sub_after_sales_id = None
        self._sub_order_id = None
        self._sub_out_order_id = None

    @property
    def sub_after_sales_id(self):
        return self._sub_after_sales_id

    @sub_after_sales_id.setter
    def sub_after_sales_id(self, value):
        self._sub_after_sales_id = value
    @property
    def sub_order_id(self):
        return self._sub_order_id

    @sub_order_id.setter
    def sub_order_id(self, value):
        self._sub_order_id = value
    @property
    def sub_out_order_id(self):
        return self._sub_out_order_id

    @sub_out_order_id.setter
    def sub_out_order_id(self, value):
        self._sub_out_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_after_sales_id:
            if hasattr(self.sub_after_sales_id, 'to_alipay_dict'):
                params['sub_after_sales_id'] = self.sub_after_sales_id.to_alipay_dict()
            else:
                params['sub_after_sales_id'] = self.sub_after_sales_id
        if self.sub_order_id:
            if hasattr(self.sub_order_id, 'to_alipay_dict'):
                params['sub_order_id'] = self.sub_order_id.to_alipay_dict()
            else:
                params['sub_order_id'] = self.sub_order_id
        if self.sub_out_order_id:
            if hasattr(self.sub_out_order_id, 'to_alipay_dict'):
                params['sub_out_order_id'] = self.sub_out_order_id.to_alipay_dict()
            else:
                params['sub_out_order_id'] = self.sub_out_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSubOrderAfterSaleInfoVO()
        if 'sub_after_sales_id' in d:
            o.sub_after_sales_id = d['sub_after_sales_id']
        if 'sub_order_id' in d:
            o.sub_order_id = d['sub_order_id']
        if 'sub_out_order_id' in d:
            o.sub_out_order_id = d['sub_out_order_id']
        return o


