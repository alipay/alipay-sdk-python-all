#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthenticationInfo import AuthenticationInfo


class AlipaySecurityRiskAuthenticationInitializeModel(object):

    def __init__(self):
        self._authentication_info = None
        self._biz_info = None
        self._env_info = None

    @property
    def authentication_info(self):
        return self._authentication_info

    @authentication_info.setter
    def authentication_info(self, value):
        if isinstance(value, AuthenticationInfo):
            self._authentication_info = value
        else:
            self._authentication_info = AuthenticationInfo.from_alipay_dict(value)
    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def env_info(self):
        return self._env_info

    @env_info.setter
    def env_info(self, value):
        self._env_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.authentication_info:
            if hasattr(self.authentication_info, 'to_alipay_dict'):
                params['authentication_info'] = self.authentication_info.to_alipay_dict()
            else:
                params['authentication_info'] = self.authentication_info
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.env_info:
            if hasattr(self.env_info, 'to_alipay_dict'):
                params['env_info'] = self.env_info.to_alipay_dict()
            else:
                params['env_info'] = self.env_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskAuthenticationInitializeModel()
        if 'authentication_info' in d:
            o.authentication_info = d['authentication_info']
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'env_info' in d:
            o.env_info = d['env_info']
        return o


