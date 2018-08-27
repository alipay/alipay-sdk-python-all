#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrincipalInfo(object):

    def __init__(self):
        self._mobile_no = None
        self._operator_cert_no = None
        self._operator_cert_type = None
        self._params = None
        self._tnt_inst_id = None
        self._user_id = None
        self._user_name = None

    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def operator_cert_no(self):
        return self._operator_cert_no

    @operator_cert_no.setter
    def operator_cert_no(self, value):
        self._operator_cert_no = value
    @property
    def operator_cert_type(self):
        return self._operator_cert_type

    @operator_cert_type.setter
    def operator_cert_type(self, value):
        self._operator_cert_type = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.operator_cert_no:
            if hasattr(self.operator_cert_no, 'to_alipay_dict'):
                params['operator_cert_no'] = self.operator_cert_no.to_alipay_dict()
            else:
                params['operator_cert_no'] = self.operator_cert_no
        if self.operator_cert_type:
            if hasattr(self.operator_cert_type, 'to_alipay_dict'):
                params['operator_cert_type'] = self.operator_cert_type.to_alipay_dict()
            else:
                params['operator_cert_type'] = self.operator_cert_type
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrincipalInfo()
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'operator_cert_no' in d:
            o.operator_cert_no = d['operator_cert_no']
        if 'operator_cert_type' in d:
            o.operator_cert_type = d['operator_cert_type']
        if 'params' in d:
            o.params = d['params']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


