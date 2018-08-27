#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaintainBizOrderServer(object):

    def __init__(self):
        self._order_server_id = None
        self._origin_cost = None
        self._out_product_id = None
        self._real_cost = None
        self._sale_num = None
        self._service_category_id = None

    @property
    def order_server_id(self):
        return self._order_server_id

    @order_server_id.setter
    def order_server_id(self, value):
        self._order_server_id = value
    @property
    def origin_cost(self):
        return self._origin_cost

    @origin_cost.setter
    def origin_cost(self, value):
        self._origin_cost = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def real_cost(self):
        return self._real_cost

    @real_cost.setter
    def real_cost(self, value):
        self._real_cost = value
    @property
    def sale_num(self):
        return self._sale_num

    @sale_num.setter
    def sale_num(self, value):
        self._sale_num = value
    @property
    def service_category_id(self):
        return self._service_category_id

    @service_category_id.setter
    def service_category_id(self, value):
        self._service_category_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_server_id:
            if hasattr(self.order_server_id, 'to_alipay_dict'):
                params['order_server_id'] = self.order_server_id.to_alipay_dict()
            else:
                params['order_server_id'] = self.order_server_id
        if self.origin_cost:
            if hasattr(self.origin_cost, 'to_alipay_dict'):
                params['origin_cost'] = self.origin_cost.to_alipay_dict()
            else:
                params['origin_cost'] = self.origin_cost
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        if self.real_cost:
            if hasattr(self.real_cost, 'to_alipay_dict'):
                params['real_cost'] = self.real_cost.to_alipay_dict()
            else:
                params['real_cost'] = self.real_cost
        if self.sale_num:
            if hasattr(self.sale_num, 'to_alipay_dict'):
                params['sale_num'] = self.sale_num.to_alipay_dict()
            else:
                params['sale_num'] = self.sale_num
        if self.service_category_id:
            if hasattr(self.service_category_id, 'to_alipay_dict'):
                params['service_category_id'] = self.service_category_id.to_alipay_dict()
            else:
                params['service_category_id'] = self.service_category_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MaintainBizOrderServer()
        if 'order_server_id' in d:
            o.order_server_id = d['order_server_id']
        if 'origin_cost' in d:
            o.origin_cost = d['origin_cost']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        if 'real_cost' in d:
            o.real_cost = d['real_cost']
        if 'sale_num' in d:
            o.sale_num = d['sale_num']
        if 'service_category_id' in d:
            o.service_category_id = d['service_category_id']
        return o


