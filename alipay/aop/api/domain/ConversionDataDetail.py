#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConversionDataDetail(object):

    def __init__(self):
        self._conversion_id = None
        self._conversion_result = None

    @property
    def conversion_id(self):
        return self._conversion_id

    @conversion_id.setter
    def conversion_id(self, value):
        self._conversion_id = value
    @property
    def conversion_result(self):
        return self._conversion_result

    @conversion_result.setter
    def conversion_result(self, value):
        self._conversion_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.conversion_id:
            if hasattr(self.conversion_id, 'to_alipay_dict'):
                params['conversion_id'] = self.conversion_id.to_alipay_dict()
            else:
                params['conversion_id'] = self.conversion_id
        if self.conversion_result:
            if hasattr(self.conversion_result, 'to_alipay_dict'):
                params['conversion_result'] = self.conversion_result.to_alipay_dict()
            else:
                params['conversion_result'] = self.conversion_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConversionDataDetail()
        if 'conversion_id' in d:
            o.conversion_id = d['conversion_id']
        if 'conversion_result' in d:
            o.conversion_result = d['conversion_result']
        return o


