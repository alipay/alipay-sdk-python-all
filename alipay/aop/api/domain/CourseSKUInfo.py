#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CourseSKUInfo(object):

    def __init__(self):
        self._course_num = None
        self._cur_price = None
        self._ori_price = None
        self._out_sku_id = None
        self._stock_num = None

    @property
    def course_num(self):
        return self._course_num

    @course_num.setter
    def course_num(self, value):
        self._course_num = value
    @property
    def cur_price(self):
        return self._cur_price

    @cur_price.setter
    def cur_price(self, value):
        self._cur_price = value
    @property
    def ori_price(self):
        return self._ori_price

    @ori_price.setter
    def ori_price(self, value):
        self._ori_price = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_num:
            if hasattr(self.course_num, 'to_alipay_dict'):
                params['course_num'] = self.course_num.to_alipay_dict()
            else:
                params['course_num'] = self.course_num
        if self.cur_price:
            if hasattr(self.cur_price, 'to_alipay_dict'):
                params['cur_price'] = self.cur_price.to_alipay_dict()
            else:
                params['cur_price'] = self.cur_price
        if self.ori_price:
            if hasattr(self.ori_price, 'to_alipay_dict'):
                params['ori_price'] = self.ori_price.to_alipay_dict()
            else:
                params['ori_price'] = self.ori_price
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CourseSKUInfo()
        if 'course_num' in d:
            o.course_num = d['course_num']
        if 'cur_price' in d:
            o.cur_price = d['cur_price']
        if 'ori_price' in d:
            o.ori_price = d['ori_price']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        return o


