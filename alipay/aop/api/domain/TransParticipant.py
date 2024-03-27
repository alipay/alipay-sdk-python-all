#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankCardExtInfoDTO import BankCardExtInfoDTO


class TransParticipant(object):

    def __init__(self):
        self._bankcard_ext_info = None
        self._identity = None
        self._identity_type = None
        self._name = None

    @property
    def bankcard_ext_info(self):
        return self._bankcard_ext_info

    @bankcard_ext_info.setter
    def bankcard_ext_info(self, value):
        if isinstance(value, BankCardExtInfoDTO):
            self._bankcard_ext_info = value
        else:
            self._bankcard_ext_info = BankCardExtInfoDTO.from_alipay_dict(value)
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
        o = TransParticipant()
        if 'bankcard_ext_info' in d:
            o.bankcard_ext_info = d['bankcard_ext_info']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'name' in d:
            o.name = d['name']
        return o


