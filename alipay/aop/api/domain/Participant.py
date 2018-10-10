#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankcardExtInfo import BankcardExtInfo


class Participant(object):

    def __init__(self):
        self._bankcard_ext_info = None
        self._ext_info = None
        self._identity = None
        self._identity_type = None
        self._merchant_user_info = None
        self._name = None

    @property
    def bankcard_ext_info(self):
        return self._bankcard_ext_info

    @bankcard_ext_info.setter
    def bankcard_ext_info(self, value):
        if isinstance(value, BankcardExtInfo):
            self._bankcard_ext_info = value
        else:
            self._bankcard_ext_info = BankcardExtInfo.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def merchant_user_info(self):
        return self._merchant_user_info

    @merchant_user_info.setter
    def merchant_user_info(self, value):
        self._merchant_user_info = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bankcard_ext_info:
            if hasattr(self.bankcard_ext_info, 'to_alipay_dict'):
                params['bankcard_ext_info'] = self.bankcard_ext_info.to_alipay_dict()
            else:
                params['bankcard_ext_info'] = self.bankcard_ext_info
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.merchant_user_info:
            if hasattr(self.merchant_user_info, 'to_alipay_dict'):
                params['merchant_user_info'] = self.merchant_user_info.to_alipay_dict()
            else:
                params['merchant_user_info'] = self.merchant_user_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Participant()
        if 'bankcard_ext_info' in d:
            o.bankcard_ext_info = d['bankcard_ext_info']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'merchant_user_info' in d:
            o.merchant_user_info = d['merchant_user_info']
        if 'name' in d:
            o.name = d['name']
        return o


