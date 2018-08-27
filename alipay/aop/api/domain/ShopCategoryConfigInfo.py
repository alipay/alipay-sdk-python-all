#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopCategoryConfigInfo(object):

    def __init__(self):
        self._id = None
        self._is_leaf = None
        self._level = None
        self._link = None
        self._nm = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_leaf(self):
        return self._is_leaf

    @is_leaf.setter
    def is_leaf(self, value):
        self._is_leaf = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def nm(self):
        return self._nm

    @nm.setter
    def nm(self, value):
        self._nm = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_leaf:
            if hasattr(self.is_leaf, 'to_alipay_dict'):
                params['is_leaf'] = self.is_leaf.to_alipay_dict()
            else:
                params['is_leaf'] = self.is_leaf
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.nm:
            if hasattr(self.nm, 'to_alipay_dict'):
                params['nm'] = self.nm.to_alipay_dict()
            else:
                params['nm'] = self.nm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopCategoryConfigInfo()
        if 'id' in d:
            o.id = d['id']
        if 'is_leaf' in d:
            o.is_leaf = d['is_leaf']
        if 'level' in d:
            o.level = d['level']
        if 'link' in d:
            o.link = d['link']
        if 'nm' in d:
            o.nm = d['nm']
        return o


