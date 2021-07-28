#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FlowSigner(object):

    def __init__(self):
        self._org_third_party_user_id = None
        self._sign_status = None
        self._signer_account_type = None
        self._third_party_user_id = None

    @property
    def org_third_party_user_id(self):
        return self._org_third_party_user_id

    @org_third_party_user_id.setter
    def org_third_party_user_id(self, value):
        self._org_third_party_user_id = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def signer_account_type(self):
        return self._signer_account_type

    @signer_account_type.setter
    def signer_account_type(self, value):
        self._signer_account_type = value
    @property
    def third_party_user_id(self):
        return self._third_party_user_id

    @third_party_user_id.setter
    def third_party_user_id(self, value):
        self._third_party_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_third_party_user_id:
            if hasattr(self.org_third_party_user_id, 'to_alipay_dict'):
                params['org_third_party_user_id'] = self.org_third_party_user_id.to_alipay_dict()
            else:
                params['org_third_party_user_id'] = self.org_third_party_user_id
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
        if self.signer_account_type:
            if hasattr(self.signer_account_type, 'to_alipay_dict'):
                params['signer_account_type'] = self.signer_account_type.to_alipay_dict()
            else:
                params['signer_account_type'] = self.signer_account_type
        if self.third_party_user_id:
            if hasattr(self.third_party_user_id, 'to_alipay_dict'):
                params['third_party_user_id'] = self.third_party_user_id.to_alipay_dict()
            else:
                params['third_party_user_id'] = self.third_party_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FlowSigner()
        if 'org_third_party_user_id' in d:
            o.org_third_party_user_id = d['org_third_party_user_id']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        if 'signer_account_type' in d:
            o.signer_account_type = d['signer_account_type']
        if 'third_party_user_id' in d:
            o.third_party_user_id = d['third_party_user_id']
        return o


