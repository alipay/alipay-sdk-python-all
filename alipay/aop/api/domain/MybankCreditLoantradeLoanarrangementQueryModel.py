#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeLoanarrangementQueryModel(object):

    def __init__(self):
        self._ip_role_id = None
        self._loan_ar_no = None
        self._mybk_auth_scene_code = None
        self._mybk_auth_token = None

    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value
    @property
    def mybk_auth_scene_code(self):
        return self._mybk_auth_scene_code

    @mybk_auth_scene_code.setter
    def mybk_auth_scene_code(self, value):
        self._mybk_auth_scene_code = value
    @property
    def mybk_auth_token(self):
        return self._mybk_auth_token

    @mybk_auth_token.setter
    def mybk_auth_token(self, value):
        self._mybk_auth_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.loan_ar_no:
            if hasattr(self.loan_ar_no, 'to_alipay_dict'):
                params['loan_ar_no'] = self.loan_ar_no.to_alipay_dict()
            else:
                params['loan_ar_no'] = self.loan_ar_no
        if self.mybk_auth_scene_code:
            if hasattr(self.mybk_auth_scene_code, 'to_alipay_dict'):
                params['mybk_auth_scene_code'] = self.mybk_auth_scene_code.to_alipay_dict()
            else:
                params['mybk_auth_scene_code'] = self.mybk_auth_scene_code
        if self.mybk_auth_token:
            if hasattr(self.mybk_auth_token, 'to_alipay_dict'):
                params['mybk_auth_token'] = self.mybk_auth_token.to_alipay_dict()
            else:
                params['mybk_auth_token'] = self.mybk_auth_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeLoanarrangementQueryModel()
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'loan_ar_no' in d:
            o.loan_ar_no = d['loan_ar_no']
        if 'mybk_auth_scene_code' in d:
            o.mybk_auth_scene_code = d['mybk_auth_scene_code']
        if 'mybk_auth_token' in d:
            o.mybk_auth_token = d['mybk_auth_token']
        return o


