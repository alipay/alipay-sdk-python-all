#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScoreRangeInfo(object):

    def __init__(self):
        self._category_score_max = None
        self._category_score_min = None
        self._crowd_score_max = None
        self._crowd_score_min = None
        self._crowd_score_type = None
        self._sale_score_max = None
        self._sale_score_min = None

    @property
    def category_score_max(self):
        return self._category_score_max

    @category_score_max.setter
    def category_score_max(self, value):
        self._category_score_max = value
    @property
    def category_score_min(self):
        return self._category_score_min

    @category_score_min.setter
    def category_score_min(self, value):
        self._category_score_min = value
    @property
    def crowd_score_max(self):
        return self._crowd_score_max

    @crowd_score_max.setter
    def crowd_score_max(self, value):
        self._crowd_score_max = value
    @property
    def crowd_score_min(self):
        return self._crowd_score_min

    @crowd_score_min.setter
    def crowd_score_min(self, value):
        self._crowd_score_min = value
    @property
    def crowd_score_type(self):
        return self._crowd_score_type

    @crowd_score_type.setter
    def crowd_score_type(self, value):
        self._crowd_score_type = value
    @property
    def sale_score_max(self):
        return self._sale_score_max

    @sale_score_max.setter
    def sale_score_max(self, value):
        self._sale_score_max = value
    @property
    def sale_score_min(self):
        return self._sale_score_min

    @sale_score_min.setter
    def sale_score_min(self, value):
        self._sale_score_min = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_score_max:
            if hasattr(self.category_score_max, 'to_alipay_dict'):
                params['category_score_max'] = self.category_score_max.to_alipay_dict()
            else:
                params['category_score_max'] = self.category_score_max
        if self.category_score_min:
            if hasattr(self.category_score_min, 'to_alipay_dict'):
                params['category_score_min'] = self.category_score_min.to_alipay_dict()
            else:
                params['category_score_min'] = self.category_score_min
        if self.crowd_score_max:
            if hasattr(self.crowd_score_max, 'to_alipay_dict'):
                params['crowd_score_max'] = self.crowd_score_max.to_alipay_dict()
            else:
                params['crowd_score_max'] = self.crowd_score_max
        if self.crowd_score_min:
            if hasattr(self.crowd_score_min, 'to_alipay_dict'):
                params['crowd_score_min'] = self.crowd_score_min.to_alipay_dict()
            else:
                params['crowd_score_min'] = self.crowd_score_min
        if self.crowd_score_type:
            if hasattr(self.crowd_score_type, 'to_alipay_dict'):
                params['crowd_score_type'] = self.crowd_score_type.to_alipay_dict()
            else:
                params['crowd_score_type'] = self.crowd_score_type
        if self.sale_score_max:
            if hasattr(self.sale_score_max, 'to_alipay_dict'):
                params['sale_score_max'] = self.sale_score_max.to_alipay_dict()
            else:
                params['sale_score_max'] = self.sale_score_max
        if self.sale_score_min:
            if hasattr(self.sale_score_min, 'to_alipay_dict'):
                params['sale_score_min'] = self.sale_score_min.to_alipay_dict()
            else:
                params['sale_score_min'] = self.sale_score_min
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScoreRangeInfo()
        if 'category_score_max' in d:
            o.category_score_max = d['category_score_max']
        if 'category_score_min' in d:
            o.category_score_min = d['category_score_min']
        if 'crowd_score_max' in d:
            o.crowd_score_max = d['crowd_score_max']
        if 'crowd_score_min' in d:
            o.crowd_score_min = d['crowd_score_min']
        if 'crowd_score_type' in d:
            o.crowd_score_type = d['crowd_score_type']
        if 'sale_score_max' in d:
            o.sale_score_max = d['sale_score_max']
        if 'sale_score_min' in d:
            o.sale_score_min = d['sale_score_min']
        return o


