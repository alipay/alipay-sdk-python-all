#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FengdieActivityCreatePageData(object):

    def __init__(self):
        self._name = None
        self._schema_data = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def schema_data(self):
        return self._schema_data

    @schema_data.setter
    def schema_data(self, value):
        self._schema_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.schema_data:
            if hasattr(self.schema_data, 'to_alipay_dict'):
                params['schema_data'] = self.schema_data.to_alipay_dict()
            else:
                params['schema_data'] = self.schema_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieActivityCreatePageData()
        if 'name' in d:
            o.name = d['name']
        if 'schema_data' in d:
            o.schema_data = d['schema_data']
        return o


