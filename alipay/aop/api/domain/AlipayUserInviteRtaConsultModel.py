#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserInviteRtaConsultModel(object):

    def __init__(self):
        self._encrypt_type = None
        self._principal = None
        self._principal_type = None
        self._target_crowd_package_key = None

    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value
    @property
    def target_crowd_package_key(self):
        return self._target_crowd_package_key

    @target_crowd_package_key.setter
    def target_crowd_package_key(self, value):
        self._target_crowd_package_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_type:
            if hasattr(self.encrypt_type, 'to_alipay_dict'):
                params['encrypt_type'] = self.encrypt_type.to_alipay_dict()
            else:
                params['encrypt_type'] = self.encrypt_type
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        if self.target_crowd_package_key:
            if hasattr(self.target_crowd_package_key, 'to_alipay_dict'):
                params['target_crowd_package_key'] = self.target_crowd_package_key.to_alipay_dict()
            else:
                params['target_crowd_package_key'] = self.target_crowd_package_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserInviteRtaConsultModel()
        if 'encrypt_type' in d:
            o.encrypt_type = d['encrypt_type']
        if 'principal' in d:
            o.principal = d['principal']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        if 'target_crowd_package_key' in d:
            o.target_crowd_package_key = d['target_crowd_package_key']
        return o


