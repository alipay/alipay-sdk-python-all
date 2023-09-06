#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppxCategoryVO(object):

    def __init__(self):
        self._cat_id = None
        self._cat_level = None
        self._cat_name = None
        self._cat_status = None
        self._f_cat_id = None
        self._item_types = None
        self._qualification_status = None

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
    def cat_status(self):
        return self._cat_status

    @cat_status.setter
    def cat_status(self, value):
        self._cat_status = value
    @property
    def f_cat_id(self):
        return self._f_cat_id

    @f_cat_id.setter
    def f_cat_id(self, value):
        self._f_cat_id = value
    @property
    def item_types(self):
        return self._item_types

    @item_types.setter
    def item_types(self, value):
        if isinstance(value, list):
            self._item_types = list()
            for i in value:
                self._item_types.append(i)
    @property
    def qualification_status(self):
        return self._qualification_status

    @qualification_status.setter
    def qualification_status(self, value):
        self._qualification_status = value


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
        if self.cat_status:
            if hasattr(self.cat_status, 'to_alipay_dict'):
                params['cat_status'] = self.cat_status.to_alipay_dict()
            else:
                params['cat_status'] = self.cat_status
        if self.f_cat_id:
            if hasattr(self.f_cat_id, 'to_alipay_dict'):
                params['f_cat_id'] = self.f_cat_id.to_alipay_dict()
            else:
                params['f_cat_id'] = self.f_cat_id
        if self.item_types:
            if isinstance(self.item_types, list):
                for i in range(0, len(self.item_types)):
                    element = self.item_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_types[i] = element.to_alipay_dict()
            if hasattr(self.item_types, 'to_alipay_dict'):
                params['item_types'] = self.item_types.to_alipay_dict()
            else:
                params['item_types'] = self.item_types
        if self.qualification_status:
            if hasattr(self.qualification_status, 'to_alipay_dict'):
                params['qualification_status'] = self.qualification_status.to_alipay_dict()
            else:
                params['qualification_status'] = self.qualification_status
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
        if 'cat_status' in d:
            o.cat_status = d['cat_status']
        if 'f_cat_id' in d:
            o.f_cat_id = d['f_cat_id']
        if 'item_types' in d:
            o.item_types = d['item_types']
        if 'qualification_status' in d:
            o.qualification_status = d['qualification_status']
        return o


