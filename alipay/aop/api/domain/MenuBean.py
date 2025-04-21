#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MenuBean(object):

    def __init__(self):
        self._menu_id = None
        self._name = None
        self._required = None
        self._sort = None

    @property
    def menu_id(self):
        return self._menu_id

    @menu_id.setter
    def menu_id(self, value):
        self._menu_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.menu_id:
            if hasattr(self.menu_id, 'to_alipay_dict'):
                params['menu_id'] = self.menu_id.to_alipay_dict()
            else:
                params['menu_id'] = self.menu_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MenuBean()
        if 'menu_id' in d:
            o.menu_id = d['menu_id']
        if 'name' in d:
            o.name = d['name']
        if 'required' in d:
            o.required = d['required']
        if 'sort' in d:
            o.sort = d['sort']
        return o


