#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementSignConfirmModel(object):

    def __init__(self):
        self._apply_token = None
        self._cert_no = None
        self._confirm_no = None

    @property
    def apply_token(self):
        return self._apply_token

    @apply_token.setter
    def apply_token(self, value):
        self._apply_token = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def confirm_no(self):
        return self._confirm_no

    @confirm_no.setter
    def confirm_no(self, value):
        self._confirm_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_token:
            if hasattr(self.apply_token, 'to_alipay_dict'):
                params['apply_token'] = self.apply_token.to_alipay_dict()
            else:
                params['apply_token'] = self.apply_token
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.confirm_no:
            if hasattr(self.confirm_no, 'to_alipay_dict'):
                params['confirm_no'] = self.confirm_no.to_alipay_dict()
            else:
                params['confirm_no'] = self.confirm_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementSignConfirmModel()
        if 'apply_token' in d:
            o.apply_token = d['apply_token']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'confirm_no' in d:
            o.confirm_no = d['confirm_no']
        return o


