#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataTag(object):

    def __init__(self):
        self._aggregate = None
        self._alias = None
        self._code = None

    @property
    def aggregate(self):
        return self._aggregate

    @aggregate.setter
    def aggregate(self, value):
        self._aggregate = value
    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggregate:
            if hasattr(self.aggregate, 'to_alipay_dict'):
                params['aggregate'] = self.aggregate.to_alipay_dict()
            else:
                params['aggregate'] = self.aggregate
        if self.alias:
            if hasattr(self.alias, 'to_alipay_dict'):
                params['alias'] = self.alias.to_alipay_dict()
            else:
                params['alias'] = self.alias
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataTag()
        if 'aggregate' in d:
            o.aggregate = d['aggregate']
        if 'alias' in d:
            o.alias = d['alias']
        if 'code' in d:
            o.code = d['code']
        return o


