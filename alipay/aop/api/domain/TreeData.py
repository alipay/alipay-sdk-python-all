#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TreeData(object):

    def __init__(self):
        self._cooperation = None
        self._num = None
        self._tree_alias = None
        self._tree_type = None

    @property
    def cooperation(self):
        return self._cooperation

    @cooperation.setter
    def cooperation(self, value):
        self._cooperation = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def tree_alias(self):
        return self._tree_alias

    @tree_alias.setter
    def tree_alias(self, value):
        self._tree_alias = value
    @property
    def tree_type(self):
        return self._tree_type

    @tree_type.setter
    def tree_type(self, value):
        self._tree_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cooperation:
            if hasattr(self.cooperation, 'to_alipay_dict'):
                params['cooperation'] = self.cooperation.to_alipay_dict()
            else:
                params['cooperation'] = self.cooperation
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.tree_alias:
            if hasattr(self.tree_alias, 'to_alipay_dict'):
                params['tree_alias'] = self.tree_alias.to_alipay_dict()
            else:
                params['tree_alias'] = self.tree_alias
        if self.tree_type:
            if hasattr(self.tree_type, 'to_alipay_dict'):
                params['tree_type'] = self.tree_type.to_alipay_dict()
            else:
                params['tree_type'] = self.tree_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TreeData()
        if 'cooperation' in d:
            o.cooperation = d['cooperation']
        if 'num' in d:
            o.num = d['num']
        if 'tree_alias' in d:
            o.tree_alias = d['tree_alias']
        if 'tree_type' in d:
            o.tree_type = d['tree_type']
        return o


