#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleSubOrderInspectProductVO import RecycleSubOrderInspectProductVO


class RecycleSubOrderInspectConfirmVO(object):

    def __init__(self):
        self._sub_order_id = None
        self._sub_order_inspect_price = None
        self._sub_order_inspect_product_list = None
        self._sub_out_order_id = None

    @property
    def sub_order_id(self):
        return self._sub_order_id

    @sub_order_id.setter
    def sub_order_id(self, value):
        self._sub_order_id = value
    @property
    def sub_order_inspect_price(self):
        return self._sub_order_inspect_price

    @sub_order_inspect_price.setter
    def sub_order_inspect_price(self, value):
        self._sub_order_inspect_price = value
    @property
    def sub_order_inspect_product_list(self):
        return self._sub_order_inspect_product_list

    @sub_order_inspect_product_list.setter
    def sub_order_inspect_product_list(self, value):
        if isinstance(value, list):
            self._sub_order_inspect_product_list = list()
            for i in value:
                if isinstance(i, RecycleSubOrderInspectProductVO):
                    self._sub_order_inspect_product_list.append(i)
                else:
                    self._sub_order_inspect_product_list.append(RecycleSubOrderInspectProductVO.from_alipay_dict(i))
    @property
    def sub_out_order_id(self):
        return self._sub_out_order_id

    @sub_out_order_id.setter
    def sub_out_order_id(self, value):
        self._sub_out_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_order_id:
            if hasattr(self.sub_order_id, 'to_alipay_dict'):
                params['sub_order_id'] = self.sub_order_id.to_alipay_dict()
            else:
                params['sub_order_id'] = self.sub_order_id
        if self.sub_order_inspect_price:
            if hasattr(self.sub_order_inspect_price, 'to_alipay_dict'):
                params['sub_order_inspect_price'] = self.sub_order_inspect_price.to_alipay_dict()
            else:
                params['sub_order_inspect_price'] = self.sub_order_inspect_price
        if self.sub_order_inspect_product_list:
            if isinstance(self.sub_order_inspect_product_list, list):
                for i in range(0, len(self.sub_order_inspect_product_list)):
                    element = self.sub_order_inspect_product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_order_inspect_product_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_order_inspect_product_list, 'to_alipay_dict'):
                params['sub_order_inspect_product_list'] = self.sub_order_inspect_product_list.to_alipay_dict()
            else:
                params['sub_order_inspect_product_list'] = self.sub_order_inspect_product_list
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
        o = RecycleSubOrderInspectConfirmVO()
        if 'sub_order_id' in d:
            o.sub_order_id = d['sub_order_id']
        if 'sub_order_inspect_price' in d:
            o.sub_order_inspect_price = d['sub_order_inspect_price']
        if 'sub_order_inspect_product_list' in d:
            o.sub_order_inspect_product_list = d['sub_order_inspect_product_list']
        if 'sub_out_order_id' in d:
            o.sub_out_order_id = d['sub_out_order_id']
        return o


