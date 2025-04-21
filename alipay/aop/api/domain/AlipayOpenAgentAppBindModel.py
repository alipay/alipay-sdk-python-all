#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentAppBindModel(object):

    def __init__(self):
        self._app_agentcode = None

    @property
    def app_agentcode(self):
        return self._app_agentcode

    @app_agentcode.setter
    def app_agentcode(self, value):
        self._app_agentcode = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_agentcode:
            if hasattr(self.app_agentcode, 'to_alipay_dict'):
                params['app_agentcode'] = self.app_agentcode.to_alipay_dict()
            else:
                params['app_agentcode'] = self.app_agentcode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentAppBindModel()
        if 'app_agentcode' in d:
            o.app_agentcode = d['app_agentcode']
        return o


