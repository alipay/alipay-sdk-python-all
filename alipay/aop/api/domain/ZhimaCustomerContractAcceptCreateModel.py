#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerContractAcceptCreateModel(object):

    def __init__(self):
        self._biz_principal_id = None
        self._biz_principal_type = None
        self._contract_no = None
        self._user_id = None

    @property
    def biz_principal_id(self):
        return self._biz_principal_id

    @biz_principal_id.setter
    def biz_principal_id(self, value):
        self._biz_principal_id = value
    @property
    def biz_principal_type(self):
        return self._biz_principal_type

    @biz_principal_type.setter
    def biz_principal_type(self, value):
        self._biz_principal_type = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_principal_id:
            if hasattr(self.biz_principal_id, 'to_alipay_dict'):
                params['biz_principal_id'] = self.biz_principal_id.to_alipay_dict()
            else:
                params['biz_principal_id'] = self.biz_principal_id
        if self.biz_principal_type:
            if hasattr(self.biz_principal_type, 'to_alipay_dict'):
                params['biz_principal_type'] = self.biz_principal_type.to_alipay_dict()
            else:
                params['biz_principal_type'] = self.biz_principal_type
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerContractAcceptCreateModel()
        if 'biz_principal_id' in d:
            o.biz_principal_id = d['biz_principal_id']
        if 'biz_principal_type' in d:
            o.biz_principal_type = d['biz_principal_type']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


