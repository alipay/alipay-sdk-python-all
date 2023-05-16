#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SolutionAttributeInfoOpenVO(object):

    def __init__(self):
        self._access_config_code = None
        self._verify_code = None

    @property
    def access_config_code(self):
        return self._access_config_code

    @access_config_code.setter
    def access_config_code(self, value):
        self._access_config_code = value
    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, value):
        self._verify_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_config_code:
            if hasattr(self.access_config_code, 'to_alipay_dict'):
                params['access_config_code'] = self.access_config_code.to_alipay_dict()
            else:
                params['access_config_code'] = self.access_config_code
        if self.verify_code:
            if hasattr(self.verify_code, 'to_alipay_dict'):
                params['verify_code'] = self.verify_code.to_alipay_dict()
            else:
                params['verify_code'] = self.verify_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SolutionAttributeInfoOpenVO()
        if 'access_config_code' in d:
            o.access_config_code = d['access_config_code']
        if 'verify_code' in d:
            o.verify_code = d['verify_code']
        return o


