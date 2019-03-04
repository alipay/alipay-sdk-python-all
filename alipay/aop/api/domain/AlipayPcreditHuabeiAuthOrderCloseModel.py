#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiAuthOrderCloseModel(object):

    def __init__(self):
        self._auth_opt_id = None
        self._operator_id = None
        self._out_request_no = None

    @property
    def auth_opt_id(self):
        return self._auth_opt_id

    @auth_opt_id.setter
    def auth_opt_id(self, value):
        self._auth_opt_id = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_opt_id:
            if hasattr(self.auth_opt_id, 'to_alipay_dict'):
                params['auth_opt_id'] = self.auth_opt_id.to_alipay_dict()
            else:
                params['auth_opt_id'] = self.auth_opt_id
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiAuthOrderCloseModel()
        if 'auth_opt_id' in d:
            o.auth_opt_id = d['auth_opt_id']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


