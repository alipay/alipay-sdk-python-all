#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlisisReportColumn(object):

    def __init__(self):
        self._alias = None
        self._data = None

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


    def to_alipay_dict(self):
        params = dict()
        if self.alias:
            if hasattr(self.alias, 'to_alipay_dict'):
                params['alias'] = self.alias.to_alipay_dict()
            else:
                params['alias'] = self.alias
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlisisReportColumn()
        if 'alias' in d:
            o.alias = d['alias']
        if 'data' in d:
            o.data = d['data']
        return o


