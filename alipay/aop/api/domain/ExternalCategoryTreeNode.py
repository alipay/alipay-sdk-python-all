#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalCategoryTreeNode(object):

    def __init__(self):
        self._cate_id = None
        self._cate_name = None
        self._leaf = None
        self._parent_cate_id = None

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value
    @property
    def cate_name(self):
        return self._cate_name

    @cate_name.setter
    def cate_name(self, value):
        self._cate_name = value
    @property
    def leaf(self):
        return self._leaf

    @leaf.setter
    def leaf(self, value):
        self._leaf = value
    @property
    def parent_cate_id(self):
        return self._parent_cate_id

    @parent_cate_id.setter
    def parent_cate_id(self, value):
        self._parent_cate_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_id:
            if hasattr(self.cate_id, 'to_alipay_dict'):
                params['cate_id'] = self.cate_id.to_alipay_dict()
            else:
                params['cate_id'] = self.cate_id
        if self.cate_name:
            if hasattr(self.cate_name, 'to_alipay_dict'):
                params['cate_name'] = self.cate_name.to_alipay_dict()
            else:
                params['cate_name'] = self.cate_name
        if self.leaf:
            if hasattr(self.leaf, 'to_alipay_dict'):
                params['leaf'] = self.leaf.to_alipay_dict()
            else:
                params['leaf'] = self.leaf
        if self.parent_cate_id:
            if hasattr(self.parent_cate_id, 'to_alipay_dict'):
                params['parent_cate_id'] = self.parent_cate_id.to_alipay_dict()
            else:
                params['parent_cate_id'] = self.parent_cate_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExternalCategoryTreeNode()
        if 'cate_id' in d:
            o.cate_id = d['cate_id']
        if 'cate_name' in d:
            o.cate_name = d['cate_name']
        if 'leaf' in d:
            o.leaf = d['leaf']
        if 'parent_cate_id' in d:
            o.parent_cate_id = d['parent_cate_id']
        return o


