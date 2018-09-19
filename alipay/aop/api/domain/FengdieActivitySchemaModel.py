#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FengdieActivitySchemaModel(object):

    def __init__(self):
        self._schema_data = None
        self._schema_path = None

    @property
    def schema_data(self):
        return self._schema_data

    @schema_data.setter
    def schema_data(self, value):
        self._schema_data = value
    @property
    def schema_path(self):
        return self._schema_path

    @schema_path.setter
    def schema_path(self, value):
        self._schema_path = value


    def to_alipay_dict(self):
        params = dict()
        if self.schema_data:
            if hasattr(self.schema_data, 'to_alipay_dict'):
                params['schema_data'] = self.schema_data.to_alipay_dict()
            else:
                params['schema_data'] = self.schema_data
        if self.schema_path:
            if hasattr(self.schema_path, 'to_alipay_dict'):
                params['schema_path'] = self.schema_path.to_alipay_dict()
            else:
                params['schema_path'] = self.schema_path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieActivitySchemaModel()
        if 'schema_data' in d:
            o.schema_data = d['schema_data']
        if 'schema_path' in d:
            o.schema_path = d['schema_path']
        return o


