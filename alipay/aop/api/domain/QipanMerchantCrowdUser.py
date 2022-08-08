#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QipanMerchantCrowdUser(object):

    def __init__(self):
        self._encrypt_identity_id = None
        self._encrypt_identity_type = None

    @property
    def encrypt_identity_id(self):
        return self._encrypt_identity_id

    @encrypt_identity_id.setter
    def encrypt_identity_id(self, value):
        self._encrypt_identity_id = value
    @property
    def encrypt_identity_type(self):
        return self._encrypt_identity_type

    @encrypt_identity_type.setter
    def encrypt_identity_type(self, value):
        self._encrypt_identity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_identity_id:
            if hasattr(self.encrypt_identity_id, 'to_alipay_dict'):
                params['encrypt_identity_id'] = self.encrypt_identity_id.to_alipay_dict()
            else:
                params['encrypt_identity_id'] = self.encrypt_identity_id
        if self.encrypt_identity_type:
            if hasattr(self.encrypt_identity_type, 'to_alipay_dict'):
                params['encrypt_identity_type'] = self.encrypt_identity_type.to_alipay_dict()
            else:
                params['encrypt_identity_type'] = self.encrypt_identity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QipanMerchantCrowdUser()
        if 'encrypt_identity_id' in d:
            o.encrypt_identity_id = d['encrypt_identity_id']
        if 'encrypt_identity_type' in d:
            o.encrypt_identity_type = d['encrypt_identity_type']
        return o


