#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpMcpDetailQueryModel(object):

    def __init__(self):
        self._ability_code = None
        self._ability_version = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpMcpDetailQueryModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'ability_version' in d:
            o.ability_version = d['ability_version']
        return o


