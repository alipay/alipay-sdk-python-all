#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendServiceInfo(object):

    def __init__(self):
        self._cate_1 = None
        self._cate_2 = None
        self._cate_3 = None
        self._first_choose = None
        self._max_price = None
        self._min_price = None
        self._recommend_reason = None
        self._star = None

    @property
    def cate_1(self):
        return self._cate_1

    @cate_1.setter
    def cate_1(self, value):
        self._cate_1 = value
    @property
    def cate_2(self):
        return self._cate_2

    @cate_2.setter
    def cate_2(self, value):
        self._cate_2 = value
    @property
    def cate_3(self):
        return self._cate_3

    @cate_3.setter
    def cate_3(self, value):
        self._cate_3 = value
    @property
    def first_choose(self):
        return self._first_choose

    @first_choose.setter
    def first_choose(self, value):
        self._first_choose = value
    @property
    def max_price(self):
        return self._max_price

    @max_price.setter
    def max_price(self, value):
        self._max_price = value
    @property
    def min_price(self):
        return self._min_price

    @min_price.setter
    def min_price(self, value):
        self._min_price = value
    @property
    def recommend_reason(self):
        return self._recommend_reason

    @recommend_reason.setter
    def recommend_reason(self, value):
        self._recommend_reason = value
    @property
    def star(self):
        return self._star

    @star.setter
    def star(self, value):
        self._star = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_1:
            if hasattr(self.cate_1, 'to_alipay_dict'):
                params['cate_1'] = self.cate_1.to_alipay_dict()
            else:
                params['cate_1'] = self.cate_1
        if self.cate_2:
            if hasattr(self.cate_2, 'to_alipay_dict'):
                params['cate_2'] = self.cate_2.to_alipay_dict()
            else:
                params['cate_2'] = self.cate_2
        if self.cate_3:
            if hasattr(self.cate_3, 'to_alipay_dict'):
                params['cate_3'] = self.cate_3.to_alipay_dict()
            else:
                params['cate_3'] = self.cate_3
        if self.first_choose:
            if hasattr(self.first_choose, 'to_alipay_dict'):
                params['first_choose'] = self.first_choose.to_alipay_dict()
            else:
                params['first_choose'] = self.first_choose
        if self.max_price:
            if hasattr(self.max_price, 'to_alipay_dict'):
                params['max_price'] = self.max_price.to_alipay_dict()
            else:
                params['max_price'] = self.max_price
        if self.min_price:
            if hasattr(self.min_price, 'to_alipay_dict'):
                params['min_price'] = self.min_price.to_alipay_dict()
            else:
                params['min_price'] = self.min_price
        if self.recommend_reason:
            if hasattr(self.recommend_reason, 'to_alipay_dict'):
                params['recommend_reason'] = self.recommend_reason.to_alipay_dict()
            else:
                params['recommend_reason'] = self.recommend_reason
        if self.star:
            if hasattr(self.star, 'to_alipay_dict'):
                params['star'] = self.star.to_alipay_dict()
            else:
                params['star'] = self.star
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecommendServiceInfo()
        if 'cate_1' in d:
            o.cate_1 = d['cate_1']
        if 'cate_2' in d:
            o.cate_2 = d['cate_2']
        if 'cate_3' in d:
            o.cate_3 = d['cate_3']
        if 'first_choose' in d:
            o.first_choose = d['first_choose']
        if 'max_price' in d:
            o.max_price = d['max_price']
        if 'min_price' in d:
            o.min_price = d['min_price']
        if 'recommend_reason' in d:
            o.recommend_reason = d['recommend_reason']
        if 'star' in d:
            o.star = d['star']
        return o


