#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApeRecommendStrategy(object):

    def __init__(self):
        self._fatigue_click_interval = None
        self._fatigue_expose_interval = None
        self._scatter_brand_window_size = None
        self._scatter_cate_level = None
        self._scatter_cate_window_size = None
        self._target_tendency_attr = None

    @property
    def fatigue_click_interval(self):
        return self._fatigue_click_interval

    @fatigue_click_interval.setter
    def fatigue_click_interval(self, value):
        self._fatigue_click_interval = value
    @property
    def fatigue_expose_interval(self):
        return self._fatigue_expose_interval

    @fatigue_expose_interval.setter
    def fatigue_expose_interval(self, value):
        self._fatigue_expose_interval = value
    @property
    def scatter_brand_window_size(self):
        return self._scatter_brand_window_size

    @scatter_brand_window_size.setter
    def scatter_brand_window_size(self, value):
        self._scatter_brand_window_size = value
    @property
    def scatter_cate_level(self):
        return self._scatter_cate_level

    @scatter_cate_level.setter
    def scatter_cate_level(self, value):
        self._scatter_cate_level = value
    @property
    def scatter_cate_window_size(self):
        return self._scatter_cate_window_size

    @scatter_cate_window_size.setter
    def scatter_cate_window_size(self, value):
        self._scatter_cate_window_size = value
    @property
    def target_tendency_attr(self):
        return self._target_tendency_attr

    @target_tendency_attr.setter
    def target_tendency_attr(self, value):
        self._target_tendency_attr = value


    def to_alipay_dict(self):
        params = dict()
        if self.fatigue_click_interval:
            if hasattr(self.fatigue_click_interval, 'to_alipay_dict'):
                params['fatigue_click_interval'] = self.fatigue_click_interval.to_alipay_dict()
            else:
                params['fatigue_click_interval'] = self.fatigue_click_interval
        if self.fatigue_expose_interval:
            if hasattr(self.fatigue_expose_interval, 'to_alipay_dict'):
                params['fatigue_expose_interval'] = self.fatigue_expose_interval.to_alipay_dict()
            else:
                params['fatigue_expose_interval'] = self.fatigue_expose_interval
        if self.scatter_brand_window_size:
            if hasattr(self.scatter_brand_window_size, 'to_alipay_dict'):
                params['scatter_brand_window_size'] = self.scatter_brand_window_size.to_alipay_dict()
            else:
                params['scatter_brand_window_size'] = self.scatter_brand_window_size
        if self.scatter_cate_level:
            if hasattr(self.scatter_cate_level, 'to_alipay_dict'):
                params['scatter_cate_level'] = self.scatter_cate_level.to_alipay_dict()
            else:
                params['scatter_cate_level'] = self.scatter_cate_level
        if self.scatter_cate_window_size:
            if hasattr(self.scatter_cate_window_size, 'to_alipay_dict'):
                params['scatter_cate_window_size'] = self.scatter_cate_window_size.to_alipay_dict()
            else:
                params['scatter_cate_window_size'] = self.scatter_cate_window_size
        if self.target_tendency_attr:
            if hasattr(self.target_tendency_attr, 'to_alipay_dict'):
                params['target_tendency_attr'] = self.target_tendency_attr.to_alipay_dict()
            else:
                params['target_tendency_attr'] = self.target_tendency_attr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApeRecommendStrategy()
        if 'fatigue_click_interval' in d:
            o.fatigue_click_interval = d['fatigue_click_interval']
        if 'fatigue_expose_interval' in d:
            o.fatigue_expose_interval = d['fatigue_expose_interval']
        if 'scatter_brand_window_size' in d:
            o.scatter_brand_window_size = d['scatter_brand_window_size']
        if 'scatter_cate_level' in d:
            o.scatter_cate_level = d['scatter_cate_level']
        if 'scatter_cate_window_size' in d:
            o.scatter_cate_window_size = d['scatter_cate_window_size']
        if 'target_tendency_attr' in d:
            o.target_tendency_attr = d['target_tendency_attr']
        return o


