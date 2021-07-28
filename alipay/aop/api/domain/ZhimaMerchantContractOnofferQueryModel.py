#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantContractOnofferQueryModel(object):

    def __init__(self):
        self._offer_no = None
        self._sign_principal_id = None
        self._sign_principal_type = None

    @property
    def offer_no(self):
        return self._offer_no

    @offer_no.setter
    def offer_no(self, value):
        self._offer_no = value
    @property
    def sign_principal_id(self):
        return self._sign_principal_id

    @sign_principal_id.setter
    def sign_principal_id(self, value):
        self._sign_principal_id = value
    @property
    def sign_principal_type(self):
        return self._sign_principal_type

    @sign_principal_type.setter
    def sign_principal_type(self, value):
        self._sign_principal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.offer_no:
            if hasattr(self.offer_no, 'to_alipay_dict'):
                params['offer_no'] = self.offer_no.to_alipay_dict()
            else:
                params['offer_no'] = self.offer_no
        if self.sign_principal_id:
            if hasattr(self.sign_principal_id, 'to_alipay_dict'):
                params['sign_principal_id'] = self.sign_principal_id.to_alipay_dict()
            else:
                params['sign_principal_id'] = self.sign_principal_id
        if self.sign_principal_type:
            if hasattr(self.sign_principal_type, 'to_alipay_dict'):
                params['sign_principal_type'] = self.sign_principal_type.to_alipay_dict()
            else:
                params['sign_principal_type'] = self.sign_principal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantContractOnofferQueryModel()
        if 'offer_no' in d:
            o.offer_no = d['offer_no']
        if 'sign_principal_id' in d:
            o.sign_principal_id = d['sign_principal_id']
        if 'sign_principal_type' in d:
            o.sign_principal_type = d['sign_principal_type']
        return o


