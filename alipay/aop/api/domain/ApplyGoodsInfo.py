#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApplyGoodsInfo(object):

    def __init__(self):
        self._alipay_goods_id = None
        self._goods_name = None
        self._remark = None
        self._show_url_1 = None
        self._show_url_2 = None
        self._show_url_3 = None
        self._three_dimension = None
        self._weight = None

    @property
    def alipay_goods_id(self):
        return self._alipay_goods_id

    @alipay_goods_id.setter
    def alipay_goods_id(self, value):
        self._alipay_goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def show_url_1(self):
        return self._show_url_1

    @show_url_1.setter
    def show_url_1(self, value):
        self._show_url_1 = value
    @property
    def show_url_2(self):
        return self._show_url_2

    @show_url_2.setter
    def show_url_2(self, value):
        self._show_url_2 = value
    @property
    def show_url_3(self):
        return self._show_url_3

    @show_url_3.setter
    def show_url_3(self, value):
        self._show_url_3 = value
    @property
    def three_dimension(self):
        return self._three_dimension

    @three_dimension.setter
    def three_dimension(self, value):
        self._three_dimension = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_goods_id:
            if hasattr(self.alipay_goods_id, 'to_alipay_dict'):
                params['alipay_goods_id'] = self.alipay_goods_id.to_alipay_dict()
            else:
                params['alipay_goods_id'] = self.alipay_goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.show_url_1:
            if hasattr(self.show_url_1, 'to_alipay_dict'):
                params['show_url_1'] = self.show_url_1.to_alipay_dict()
            else:
                params['show_url_1'] = self.show_url_1
        if self.show_url_2:
            if hasattr(self.show_url_2, 'to_alipay_dict'):
                params['show_url_2'] = self.show_url_2.to_alipay_dict()
            else:
                params['show_url_2'] = self.show_url_2
        if self.show_url_3:
            if hasattr(self.show_url_3, 'to_alipay_dict'):
                params['show_url_3'] = self.show_url_3.to_alipay_dict()
            else:
                params['show_url_3'] = self.show_url_3
        if self.three_dimension:
            if hasattr(self.three_dimension, 'to_alipay_dict'):
                params['three_dimension'] = self.three_dimension.to_alipay_dict()
            else:
                params['three_dimension'] = self.three_dimension
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyGoodsInfo()
        if 'alipay_goods_id' in d:
            o.alipay_goods_id = d['alipay_goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'remark' in d:
            o.remark = d['remark']
        if 'show_url_1' in d:
            o.show_url_1 = d['show_url_1']
        if 'show_url_2' in d:
            o.show_url_2 = d['show_url_2']
        if 'show_url_3' in d:
            o.show_url_3 = d['show_url_3']
        if 'three_dimension' in d:
            o.three_dimension = d['three_dimension']
        if 'weight' in d:
            o.weight = d['weight']
        return o


