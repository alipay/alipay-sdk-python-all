#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppxCategoryVO(object):

    def __init__(self):
        self._cat_id = None
        self._cat_level = None
        self._cat_name = None
        self._f_cat_id = None

    @property
    def cat_id(self):
        return self._cat_id

    @cat_id.setter
    def cat_id(self, value):
        self._cat_id = value
    @property
    def cat_level(self):
        return self._cat_level

    @cat_level.setter
    def cat_level(self, value):
        self._cat_level = value
    @property
    def cat_name(self):
        return self._cat_name

    @cat_name.setter
    def cat_name(self, value):
        self._cat_name = value
    @property
    def f_cat_id(self):
        return self._f_cat_id

    @f_cat_id.setter
    def f_cat_id(self, value):
        self._f_cat_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cat_id:
            if hasattr(self.cat_id, 'to_alipay_dict'):
                params['cat_id'] = self.cat_id.to_alipay_dict()
            else:
                params['cat_id'] = self.cat_id
        if self.cat_level:
            if hasattr(self.cat_level, 'to_alipay_dict'):
                params['cat_level'] = self.cat_level.to_alipay_dict()
            else:
                params['cat_level'] = self.cat_level
        if self.cat_name:
            if hasattr(self.cat_name, 'to_alipay_dict'):
                params['cat_name'] = self.cat_name.to_alipay_dict()
            else:
                params['cat_name'] = self.cat_name
        if self.f_cat_id:
            if hasattr(self.f_cat_id, 'to_alipay_dict'):
                params['f_cat_id'] = self.f_cat_id.to_alipay_dict()
            else:
                params['f_cat_id'] = self.f_cat_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppxCategoryVO()
        if 'cat_id' in d:
            o.cat_id = d['cat_id']
        if 'cat_level' in d:
            o.cat_level = d['cat_level']
        if 'cat_name' in d:
            o.cat_name = d['cat_name']
        if 'f_cat_id' in d:
            o.f_cat_id = d['f_cat_id']
        return o


