#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegisterItemInfo(object):

    def __init__(self):
        self._enabled = None
        self._item_code = None
        self._item_prop = None
        self._label = None
        self._parent_code = None
        self._sort = None

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_prop(self):
        return self._item_prop

    @item_prop.setter
    def item_prop(self, value):
        self._item_prop = value
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def parent_code(self):
        return self._parent_code

    @parent_code.setter
    def parent_code(self, value):
        self._parent_code = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.enabled:
            if hasattr(self.enabled, 'to_alipay_dict'):
                params['enabled'] = self.enabled.to_alipay_dict()
            else:
                params['enabled'] = self.enabled
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_prop:
            if hasattr(self.item_prop, 'to_alipay_dict'):
                params['item_prop'] = self.item_prop.to_alipay_dict()
            else:
                params['item_prop'] = self.item_prop
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.parent_code:
            if hasattr(self.parent_code, 'to_alipay_dict'):
                params['parent_code'] = self.parent_code.to_alipay_dict()
            else:
                params['parent_code'] = self.parent_code
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
        o = RegisterItemInfo()
        if 'enabled' in d:
            o.enabled = d['enabled']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_prop' in d:
            o.item_prop = d['item_prop']
        if 'label' in d:
            o.label = d['label']
        if 'parent_code' in d:
            o.parent_code = d['parent_code']
        if 'sort' in d:
            o.sort = d['sort']
        return o


