#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntpaasTokenThirdTrustLoginModel(object):

    def __init__(self):
        self._login_target = None

    @property
    def login_target(self):
        return self._login_target

    @login_target.setter
    def login_target(self, value):
        self._login_target = value


    def to_alipay_dict(self):
        params = dict()
        if self.login_target:
            if hasattr(self.login_target, 'to_alipay_dict'):
                params['login_target'] = self.login_target.to_alipay_dict()
            else:
                params['login_target'] = self.login_target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntpaasTokenThirdTrustLoginModel()
        if 'login_target' in d:
            o.login_target = d['login_target']
        return o


