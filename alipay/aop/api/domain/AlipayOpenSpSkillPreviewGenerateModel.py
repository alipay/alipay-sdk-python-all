#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpSkillPreviewGenerateModel(object):

    def __init__(self):
        self._ability_code = None
        self._ability_version = None
        self._operator_account = None
        self._timeout_seconds = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def ability_version(self):
        return self._ability_version

    @ability_version.setter
    def ability_version(self, value):
        self._ability_version = value
    @property
    def operator_account(self):
        return self._operator_account

    @operator_account.setter
    def operator_account(self, value):
        self._operator_account = value
    @property
    def timeout_seconds(self):
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, value):
        self._timeout_seconds = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.ability_version:
            if hasattr(self.ability_version, 'to_alipay_dict'):
                params['ability_version'] = self.ability_version.to_alipay_dict()
            else:
                params['ability_version'] = self.ability_version
        if self.operator_account:
            if hasattr(self.operator_account, 'to_alipay_dict'):
                params['operator_account'] = self.operator_account.to_alipay_dict()
            else:
                params['operator_account'] = self.operator_account
        if self.timeout_seconds:
            if hasattr(self.timeout_seconds, 'to_alipay_dict'):
                params['timeout_seconds'] = self.timeout_seconds.to_alipay_dict()
            else:
                params['timeout_seconds'] = self.timeout_seconds
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpSkillPreviewGenerateModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'ability_version' in d:
            o.ability_version = d['ability_version']
        if 'operator_account' in d:
            o.operator_account = d['operator_account']
        if 'timeout_seconds' in d:
            o.timeout_seconds = d['timeout_seconds']
        return o


