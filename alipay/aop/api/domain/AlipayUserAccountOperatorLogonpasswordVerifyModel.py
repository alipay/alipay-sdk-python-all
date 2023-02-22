#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountOperatorLogonpasswordVerifyModel(object):

    def __init__(self):
        self._biz_code = None
        self._operator_logon_id = None
        self._operator_logon_pwd = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def operator_logon_id(self):
        return self._operator_logon_id

    @operator_logon_id.setter
    def operator_logon_id(self, value):
        self._operator_logon_id = value
    @property
    def operator_logon_pwd(self):
        return self._operator_logon_pwd

    @operator_logon_pwd.setter
    def operator_logon_pwd(self, value):
        self._operator_logon_pwd = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.operator_logon_id:
            if hasattr(self.operator_logon_id, 'to_alipay_dict'):
                params['operator_logon_id'] = self.operator_logon_id.to_alipay_dict()
            else:
                params['operator_logon_id'] = self.operator_logon_id
        if self.operator_logon_pwd:
            if hasattr(self.operator_logon_pwd, 'to_alipay_dict'):
                params['operator_logon_pwd'] = self.operator_logon_pwd.to_alipay_dict()
            else:
                params['operator_logon_pwd'] = self.operator_logon_pwd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountOperatorLogonpasswordVerifyModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'operator_logon_id' in d:
            o.operator_logon_id = d['operator_logon_id']
        if 'operator_logon_pwd' in d:
            o.operator_logon_pwd = d['operator_logon_pwd']
        return o


