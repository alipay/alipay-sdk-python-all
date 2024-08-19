#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoContractSignModel(object):

    def __init__(self):
        self._apdid_token = None
        self._contract_id = None
        self._customer_id = None
        self._logon_id = None
        self._role_type = None
        self._sign_pic = None
        self._source_id = None

    @property
    def apdid_token(self):
        return self._apdid_token

    @apdid_token.setter
    def apdid_token(self, value):
        self._apdid_token = value
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def sign_pic(self):
        return self._sign_pic

    @sign_pic.setter
    def sign_pic(self, value):
        self._sign_pic = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apdid_token:
            if hasattr(self.apdid_token, 'to_alipay_dict'):
                params['apdid_token'] = self.apdid_token.to_alipay_dict()
            else:
                params['apdid_token'] = self.apdid_token
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.sign_pic:
            if hasattr(self.sign_pic, 'to_alipay_dict'):
                params['sign_pic'] = self.sign_pic.to_alipay_dict()
            else:
                params['sign_pic'] = self.sign_pic
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoContractSignModel()
        if 'apdid_token' in d:
            o.apdid_token = d['apdid_token']
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'sign_pic' in d:
            o.sign_pic = d['sign_pic']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


