#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VcpBizIndicatorChildren import VcpBizIndicatorChildren


class VcpBizIndicator(object):

    def __init__(self):
        self._children = None
        self._target_code = None
        self._target_name = None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, VcpBizIndicatorChildren):
            self._children = value
        else:
            self._children = VcpBizIndicatorChildren.from_alipay_dict(value)
    @property
    def target_code(self):
        return self._target_code

    @target_code.setter
    def target_code(self, value):
        self._target_code = value
    @property
    def target_name(self):
        return self._target_name

    @target_name.setter
    def target_name(self, value):
        self._target_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.children:
            if hasattr(self.children, 'to_alipay_dict'):
                params['children'] = self.children.to_alipay_dict()
            else:
                params['children'] = self.children
        if self.target_code:
            if hasattr(self.target_code, 'to_alipay_dict'):
                params['target_code'] = self.target_code.to_alipay_dict()
            else:
                params['target_code'] = self.target_code
        if self.target_name:
            if hasattr(self.target_name, 'to_alipay_dict'):
                params['target_name'] = self.target_name.to_alipay_dict()
            else:
                params['target_name'] = self.target_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpBizIndicator()
        if 'children' in d:
            o.children = d['children']
        if 'target_code' in d:
            o.target_code = d['target_code']
        if 'target_name' in d:
            o.target_name = d['target_name']
        return o


