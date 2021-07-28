#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodCommonQueryModel(object):

    def __init__(self):
        self._app_seq_no = None
        self._ext_param = None
        self._operation_type = None
        self._org_code = None
        self._product_code = None
        self._seq_no = None

    @property
    def app_seq_no(self):
        return self._app_seq_no

    @app_seq_no.setter
    def app_seq_no(self, value):
        self._app_seq_no = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def seq_no(self):
        return self._seq_no

    @seq_no.setter
    def seq_no(self, value):
        self._seq_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_seq_no:
            if hasattr(self.app_seq_no, 'to_alipay_dict'):
                params['app_seq_no'] = self.app_seq_no.to_alipay_dict()
            else:
                params['app_seq_no'] = self.app_seq_no
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.seq_no:
            if hasattr(self.seq_no, 'to_alipay_dict'):
                params['seq_no'] = self.seq_no.to_alipay_dict()
            else:
                params['seq_no'] = self.seq_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodCommonQueryModel()
        if 'app_seq_no' in d:
            o.app_seq_no = d['app_seq_no']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'seq_no' in d:
            o.seq_no = d['seq_no']
        return o


