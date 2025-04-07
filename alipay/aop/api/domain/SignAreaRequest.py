#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignAreaRequest(object):

    def __init__(self):
        self._pos_page = None
        self._pos_x = None
        self._pos_y = None

    @property
    def pos_page(self):
        return self._pos_page

    @pos_page.setter
    def pos_page(self, value):
        self._pos_page = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.pos_page:
            if hasattr(self.pos_page, 'to_alipay_dict'):
                params['pos_page'] = self.pos_page.to_alipay_dict()
            else:
                params['pos_page'] = self.pos_page
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignAreaRequest()
        if 'pos_page' in d:
            o.pos_page = d['pos_page']
        if 'pos_x' in d:
            o.pos_x = d['pos_x']
        if 'pos_y' in d:
            o.pos_y = d['pos_y']
        return o


