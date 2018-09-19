#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementAuthConfirmModel(object):

    def __init__(self):
        self._agreement_no = None
        self._apply_token = None
        self._auth_confirm_no = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementAuthConfirmModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'apply_token' in d:
            o.apply_token = d['apply_token']
        if 'auth_confirm_no' in d:
            o.auth_confirm_no = d['auth_confirm_no']
        return o


