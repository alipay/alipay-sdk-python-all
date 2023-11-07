#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdReportConversionDataDetail(object):

    def __init__(self):
        self._conversion_result = None
        self._conversion_type = None
        self._conversion_type_name = None

    @property
    def conversion_result(self):
        return self._conversion_result

    @conversion_result.setter
    def conversion_result(self, value):
        self._conversion_result = value
    @property
    def conversion_type(self):
        return self._conversion_type

    @conversion_type.setter
    def conversion_type(self, value):
        self._conversion_type = value
    @property
    def conversion_type_name(self):
        return self._conversion_type_name

    @conversion_type_name.setter
    def conversion_type_name(self, value):
        self._conversion_type_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.conversion_result:
            if hasattr(self.conversion_result, 'to_alipay_dict'):
                params['conversion_result'] = self.conversion_result.to_alipay_dict()
            else:
                params['conversion_result'] = self.conversion_result
        if self.conversion_type:
            if hasattr(self.conversion_type, 'to_alipay_dict'):
                params['conversion_type'] = self.conversion_type.to_alipay_dict()
            else:
                params['conversion_type'] = self.conversion_type
        if self.conversion_type_name:
            if hasattr(self.conversion_type_name, 'to_alipay_dict'):
                params['conversion_type_name'] = self.conversion_type_name.to_alipay_dict()
            else:
                params['conversion_type_name'] = self.conversion_type_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdReportConversionDataDetail()
        if 'conversion_result' in d:
            o.conversion_result = d['conversion_result']
        if 'conversion_type' in d:
            o.conversion_type = d['conversion_type']
        if 'conversion_type_name' in d:
            o.conversion_type_name = d['conversion_type_name']
        return o


