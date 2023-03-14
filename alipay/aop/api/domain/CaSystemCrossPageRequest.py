#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CaSystemCrossPageRequest(object):

    def __init__(self):
        self._default_cross_page = None
        self._default_cross_page_rule = None
        self._pos_page_end = None
        self._pos_page_start = None
        self._pos_x = None
        self._pos_y = None
        self._seal_times = None

    @property
    def default_cross_page(self):
        return self._default_cross_page

    @default_cross_page.setter
    def default_cross_page(self, value):
        self._default_cross_page = value
    @property
    def default_cross_page_rule(self):
        return self._default_cross_page_rule

    @default_cross_page_rule.setter
    def default_cross_page_rule(self, value):
        self._default_cross_page_rule = value
    @property
    def pos_page_end(self):
        return self._pos_page_end

    @pos_page_end.setter
    def pos_page_end(self, value):
        self._pos_page_end = value
    @property
    def pos_page_start(self):
        return self._pos_page_start

    @pos_page_start.setter
    def pos_page_start(self, value):
        self._pos_page_start = value
    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value):
        self._pos_x = value
    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        self._pos_y = value
    @property
    def seal_times(self):
        return self._seal_times

    @seal_times.setter
    def seal_times(self, value):
        self._seal_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.default_cross_page:
            if hasattr(self.default_cross_page, 'to_alipay_dict'):
                params['default_cross_page'] = self.default_cross_page.to_alipay_dict()
            else:
                params['default_cross_page'] = self.default_cross_page
        if self.default_cross_page_rule:
            if hasattr(self.default_cross_page_rule, 'to_alipay_dict'):
                params['default_cross_page_rule'] = self.default_cross_page_rule.to_alipay_dict()
            else:
                params['default_cross_page_rule'] = self.default_cross_page_rule
        if self.pos_page_end:
            if hasattr(self.pos_page_end, 'to_alipay_dict'):
                params['pos_page_end'] = self.pos_page_end.to_alipay_dict()
            else:
                params['pos_page_end'] = self.pos_page_end
        if self.pos_page_start:
            if hasattr(self.pos_page_start, 'to_alipay_dict'):
                params['pos_page_start'] = self.pos_page_start.to_alipay_dict()
            else:
                params['pos_page_start'] = self.pos_page_start
        if self.pos_x:
            if hasattr(self.pos_x, 'to_alipay_dict'):
                params['pos_x'] = self.pos_x.to_alipay_dict()
            else:
                params['pos_x'] = self.pos_x
        if self.pos_y:
            if hasattr(self.pos_y, 'to_alipay_dict'):
                params['pos_y'] = self.pos_y.to_alipay_dict()
            else:
                params['pos_y'] = self.pos_y
        if self.seal_times:
            if hasattr(self.seal_times, 'to_alipay_dict'):
                params['seal_times'] = self.seal_times.to_alipay_dict()
            else:
                params['seal_times'] = self.seal_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaSystemCrossPageRequest()
        if 'default_cross_page' in d:
            o.default_cross_page = d['default_cross_page']
        if 'default_cross_page_rule' in d:
            o.default_cross_page_rule = d['default_cross_page_rule']
        if 'pos_page_end' in d:
            o.pos_page_end = d['pos_page_end']
        if 'pos_page_start' in d:
            o.pos_page_start = d['pos_page_start']
        if 'pos_x' in d:
            o.pos_x = d['pos_x']
        if 'pos_y' in d:
            o.pos_y = d['pos_y']
        if 'seal_times' in d:
            o.seal_times = d['seal_times']
        return o


