#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DateTabs(object):

    def __init__(self):
        self._axis_x = None
        self._axis_y = None
        self._color = None
        self._font_size = None
        self._use_date_tab = None

    @property
    def axis_x(self):
        return self._axis_x

    @axis_x.setter
    def axis_x(self, value):
        self._axis_x = value
    @property
    def axis_y(self):
        return self._axis_y

    @axis_y.setter
    def axis_y(self, value):
        self._axis_y = value
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = value
    @property
    def use_date_tab(self):
        return self._use_date_tab

    @use_date_tab.setter
    def use_date_tab(self, value):
        self._use_date_tab = value


    def to_alipay_dict(self):
        params = dict()
        if self.axis_x:
            if hasattr(self.axis_x, 'to_alipay_dict'):
                params['axis_x'] = self.axis_x.to_alipay_dict()
            else:
                params['axis_x'] = self.axis_x
        if self.axis_y:
            if hasattr(self.axis_y, 'to_alipay_dict'):
                params['axis_y'] = self.axis_y.to_alipay_dict()
            else:
                params['axis_y'] = self.axis_y
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.font_size:
            if hasattr(self.font_size, 'to_alipay_dict'):
                params['font_size'] = self.font_size.to_alipay_dict()
            else:
                params['font_size'] = self.font_size
        if self.use_date_tab:
            if hasattr(self.use_date_tab, 'to_alipay_dict'):
                params['use_date_tab'] = self.use_date_tab.to_alipay_dict()
            else:
                params['use_date_tab'] = self.use_date_tab
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DateTabs()
        if 'axis_x' in d:
            o.axis_x = d['axis_x']
        if 'axis_y' in d:
            o.axis_y = d['axis_y']
        if 'color' in d:
            o.color = d['color']
        if 'font_size' in d:
            o.font_size = d['font_size']
        if 'use_date_tab' in d:
            o.use_date_tab = d['use_date_tab']
        return o


