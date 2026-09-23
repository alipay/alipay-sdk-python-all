#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDevinDistributeruleCreateModel(object):

    def __init__(self):
        self._data = None
        self._form_code = None
        self._tenant_id = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def form_code(self):
        return self._form_code

    @form_code.setter
    def form_code(self, value):
        self._form_code = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.form_code:
            if hasattr(self.form_code, 'to_alipay_dict'):
                params['form_code'] = self.form_code.to_alipay_dict()
            else:
                params['form_code'] = self.form_code
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDevinDistributeruleCreateModel()
        if 'data' in d:
            o.data = d['data']
        if 'form_code' in d:
            o.form_code = d['form_code']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


