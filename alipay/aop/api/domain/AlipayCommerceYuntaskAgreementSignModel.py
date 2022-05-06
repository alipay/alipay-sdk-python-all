#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskAgreementSignModel(object):

    def __init__(self):
        self._external_agreement_no = None
        self._sign_user_id = None

    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_agreement_no:
            if hasattr(self.external_agreement_no, 'to_alipay_dict'):
                params['external_agreement_no'] = self.external_agreement_no.to_alipay_dict()
            else:
                params['external_agreement_no'] = self.external_agreement_no
        if self.sign_user_id:
            if hasattr(self.sign_user_id, 'to_alipay_dict'):
                params['sign_user_id'] = self.sign_user_id.to_alipay_dict()
            else:
                params['sign_user_id'] = self.sign_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskAgreementSignModel()
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        return o


