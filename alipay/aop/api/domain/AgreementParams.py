#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgreementParams(object):

    def __init__(self):
        self._agreement_no = None
        self._apply_token = None
        self._auth_confirm_no = None
        self._deduct_permission = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def apply_token(self):
        return self._apply_token

    @apply_token.setter
    def apply_token(self, value):
        self._apply_token = value
    @property
    def auth_confirm_no(self):
        return self._auth_confirm_no

    @auth_confirm_no.setter
    def auth_confirm_no(self, value):
        self._auth_confirm_no = value
    @property
    def deduct_permission(self):
        return self._deduct_permission

    @deduct_permission.setter
    def deduct_permission(self, value):
        self._deduct_permission = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.apply_token:
            if hasattr(self.apply_token, 'to_alipay_dict'):
                params['apply_token'] = self.apply_token.to_alipay_dict()
            else:
                params['apply_token'] = self.apply_token
        if self.auth_confirm_no:
            if hasattr(self.auth_confirm_no, 'to_alipay_dict'):
                params['auth_confirm_no'] = self.auth_confirm_no.to_alipay_dict()
            else:
                params['auth_confirm_no'] = self.auth_confirm_no
        if self.deduct_permission:
            if hasattr(self.deduct_permission, 'to_alipay_dict'):
                params['deduct_permission'] = self.deduct_permission.to_alipay_dict()
            else:
                params['deduct_permission'] = self.deduct_permission
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgreementParams()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'apply_token' in d:
            o.apply_token = d['apply_token']
        if 'auth_confirm_no' in d:
            o.auth_confirm_no = d['auth_confirm_no']
        if 'deduct_permission' in d:
            o.deduct_permission = d['deduct_permission']
        return o


