#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyApplyQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._ext_params = None
        self._name = None
        self._subapply_no = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def subapply_no(self):
        return self._subapply_no

    @subapply_no.setter
    def subapply_no(self, value):
        self._subapply_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.subapply_no:
            if hasattr(self.subapply_no, 'to_alipay_dict'):
                params['subapply_no'] = self.subapply_no.to_alipay_dict()
            else:
                params['subapply_no'] = self.subapply_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyApplyQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'name' in d:
            o.name = d['name']
        if 'subapply_no' in d:
            o.subapply_no = d['subapply_no']
        return o


