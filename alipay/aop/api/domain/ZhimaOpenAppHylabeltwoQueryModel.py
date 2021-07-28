#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaOpenAppHylabeltwoQueryModel(object):

    def __init__(self):
        self._name = None
        self._opr_scope = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def opr_scope(self):
        return self._opr_scope

    @opr_scope.setter
    def opr_scope(self, value):
        self._opr_scope = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.opr_scope:
            if hasattr(self.opr_scope, 'to_alipay_dict'):
                params['opr_scope'] = self.opr_scope.to_alipay_dict()
            else:
                params['opr_scope'] = self.opr_scope
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaOpenAppHylabeltwoQueryModel()
        if 'name' in d:
            o.name = d['name']
        if 'opr_scope' in d:
            o.opr_scope = d['opr_scope']
        return o


