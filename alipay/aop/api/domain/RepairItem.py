#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepairItem(object):

    def __init__(self):
        self._part_id = None
        self._pay_type = None
        self._price = None
        self._repair_degree = None
        self._repair_type = None

    @property
    def part_id(self):
        return self._part_id

    @part_id.setter
    def part_id(self, value):
        self._part_id = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def repair_degree(self):
        return self._repair_degree

    @repair_degree.setter
    def repair_degree(self, value):
        self._repair_degree = value
    @property
    def repair_type(self):
        return self._repair_type

    @repair_type.setter
    def repair_type(self, value):
        self._repair_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.part_id:
            if hasattr(self.part_id, 'to_alipay_dict'):
                params['part_id'] = self.part_id.to_alipay_dict()
            else:
                params['part_id'] = self.part_id
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.repair_degree:
            if hasattr(self.repair_degree, 'to_alipay_dict'):
                params['repair_degree'] = self.repair_degree.to_alipay_dict()
            else:
                params['repair_degree'] = self.repair_degree
        if self.repair_type:
            if hasattr(self.repair_type, 'to_alipay_dict'):
                params['repair_type'] = self.repair_type.to_alipay_dict()
            else:
                params['repair_type'] = self.repair_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepairItem()
        if 'part_id' in d:
            o.part_id = d['part_id']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'price' in d:
            o.price = d['price']
        if 'repair_degree' in d:
            o.repair_degree = d['repair_degree']
        if 'repair_type' in d:
            o.repair_type = d['repair_type']
        return o


