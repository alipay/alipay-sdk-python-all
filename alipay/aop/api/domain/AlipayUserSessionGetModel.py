#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserSessionGetModel(object):

    def __init__(self):
        self._agent_app_id = None
        self._login_code = None

    @property
    def agent_app_id(self):
        return self._agent_app_id

    @agent_app_id.setter
    def agent_app_id(self, value):
        self._agent_app_id = value
    @property
    def login_code(self):
        return self._login_code

    @login_code.setter
    def login_code(self, value):
        self._login_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_app_id:
            if hasattr(self.agent_app_id, 'to_alipay_dict'):
                params['agent_app_id'] = self.agent_app_id.to_alipay_dict()
            else:
                params['agent_app_id'] = self.agent_app_id
        if self.login_code:
            if hasattr(self.login_code, 'to_alipay_dict'):
                params['login_code'] = self.login_code.to_alipay_dict()
            else:
                params['login_code'] = self.login_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserSessionGetModel()
        if 'agent_app_id' in d:
            o.agent_app_id = d['agent_app_id']
        if 'login_code' in d:
            o.login_code = d['login_code']
        return o


