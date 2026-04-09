#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgentSignParams import AgentSignParams


class AlipayTradeAgentPayModel(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_sign_params = None
        self._prepay_id = None
        self._user_token = None
        self._user_token_type = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_sign_params(self):
        return self._agreement_sign_params

    @agreement_sign_params.setter
    def agreement_sign_params(self, value):
        if isinstance(value, AgentSignParams):
            self._agreement_sign_params = value
        else:
            self._agreement_sign_params = AgentSignParams.from_alipay_dict(value)
    @property
    def prepay_id(self):
        return self._prepay_id

    @prepay_id.setter
    def prepay_id(self, value):
        self._prepay_id = value
    @property
    def user_token(self):
        return self._user_token

    @user_token.setter
    def user_token(self, value):
        self._user_token = value
    @property
    def user_token_type(self):
        return self._user_token_type

    @user_token_type.setter
    def user_token_type(self, value):
        self._user_token_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_sign_params:
            if hasattr(self.agreement_sign_params, 'to_alipay_dict'):
                params['agreement_sign_params'] = self.agreement_sign_params.to_alipay_dict()
            else:
                params['agreement_sign_params'] = self.agreement_sign_params
        if self.prepay_id:
            if hasattr(self.prepay_id, 'to_alipay_dict'):
                params['prepay_id'] = self.prepay_id.to_alipay_dict()
            else:
                params['prepay_id'] = self.prepay_id
        if self.user_token:
            if hasattr(self.user_token, 'to_alipay_dict'):
                params['user_token'] = self.user_token.to_alipay_dict()
            else:
                params['user_token'] = self.user_token
        if self.user_token_type:
            if hasattr(self.user_token_type, 'to_alipay_dict'):
                params['user_token_type'] = self.user_token_type.to_alipay_dict()
            else:
                params['user_token_type'] = self.user_token_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeAgentPayModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_sign_params' in d:
            o.agreement_sign_params = d['agreement_sign_params']
        if 'prepay_id' in d:
            o.prepay_id = d['prepay_id']
        if 'user_token' in d:
            o.user_token = d['user_token']
        if 'user_token_type' in d:
            o.user_token_type = d['user_token_type']
        return o


