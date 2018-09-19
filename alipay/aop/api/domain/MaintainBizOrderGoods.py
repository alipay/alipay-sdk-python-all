#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaintainBizOrderGoods(object):

    def __init__(self):
        self._goods_image = None
        self._order_goods_id = None
        self._original_cost = None
        self._out_goods_no = None
        self._out_package_id = None
        self._package_name = None
        self._real_cost = None
        self._sale_num = None

    @property
    def goods_image(self):
        return self._goods_image

    @goods_image.setter
    def goods_image(self, value):
        self._goods_image = value
    @property
    def order_goods_id(self):
        return self._order_goods_id

    @order_goods_id.setter
    def order_goods_id(self, value):
        self._order_goods_id = value
    @property
    def original_cost(self):
        return self._original_cost

    @original_cost.setter
    def original_cost(self, value):
        self._original_cost = value
    @property
    def out_goods_no(self):
        return self._out_goods_no

    @out_goods_no.setter
    def out_goods_no(self, value):
        self._out_goods_no = value
    @property
    def out_package_id(self):
        return self._out_package_id

    @out_package_id.setter
    def out_package_id(self, value):
        self._out_package_id = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.goods_image:
            if hasattr(self.goods_image, 'to_alipay_dict'):
                params['goods_image'] = self.goods_image.to_alipay_dict()
            else:
                params['goods_image'] = self.goods_image
        if self.order_goods_id:
            if hasattr(self.order_goods_id, 'to_alipay_dict'):
                params['order_goods_id'] = self.order_goods_id.to_alipay_dict()
            else:
                params['order_goods_id'] = self.order_goods_id
        if self.original_cost:
            if hasattr(self.original_cost, 'to_alipay_dict'):
                params['original_cost'] = self.original_cost.to_alipay_dict()
            else:
                params['original_cost'] = self.original_cost
        if self.out_goods_no:
            if hasattr(self.out_goods_no, 'to_alipay_dict'):
                params['out_goods_no'] = self.out_goods_no.to_alipay_dict()
            else:
                params['out_goods_no'] = self.out_goods_no
        if self.out_package_id:
            if hasattr(self.out_package_id, 'to_alipay_dict'):
                params['out_package_id'] = self.out_package_id.to_alipay_dict()
            else:
                params['out_package_id'] = self.out_package_id
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MaintainBizOrderGoods()
        if 'goods_image' in d:
            o.goods_image = d['goods_image']
        if 'order_goods_id' in d:
            o.order_goods_id = d['order_goods_id']
        if 'original_cost' in d:
            o.original_cost = d['original_cost']
        if 'out_goods_no' in d:
            o.out_goods_no = d['out_goods_no']
        if 'out_package_id' in d:
            o.out_package_id = d['out_package_id']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'real_cost' in d:
            o.real_cost = d['real_cost']
        if 'sale_num' in d:
            o.sale_num = d['sale_num']
        return o


