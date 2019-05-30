#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppModelQueryResponse(object):

    def __init__(self):
        self._model_type = None
        self._records = None

    @property
    def model_type(self):
        return self._model_type

    @model_type.setter
    def model_type(self, value):
        self._model_type = value
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                self._records.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.model_type:
            if hasattr(self.model_type, 'to_alipay_dict'):
                params['model_type'] = self.model_type.to_alipay_dict()
            else:
                params['model_type'] = self.model_type
        if self.records:
            if isinstance(self.records, list):
                for i in range(0, len(self.records)):
                    element = self.records[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.records[i] = element.to_alipay_dict()
            if hasattr(self.records, 'to_alipay_dict'):
                params['records'] = self.records.to_alipay_dict()
            else:
                params['records'] = self.records
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppModelQueryResponse()
        if 'model_type' in d:
            o.model_type = d['model_type']
        if 'records' in d:
            o.records = d['records']
        return o


