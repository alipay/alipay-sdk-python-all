#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractSignArea(object):

    def __init__(self):
        self._page_num = None
        self._pos_x = None
        self._pos_y = None
        self._user_type = None
        self._width = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
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
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
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
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractSignArea()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'pos_x' in d:
            o.pos_x = d['pos_x']
        if 'pos_y' in d:
            o.pos_y = d['pos_y']
        if 'user_type' in d:
            o.user_type = d['user_type']
        if 'width' in d:
            o.width = d['width']
        return o


