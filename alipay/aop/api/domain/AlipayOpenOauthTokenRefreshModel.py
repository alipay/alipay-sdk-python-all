#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOauthTokenRefreshModel(object):

    def __init__(self):
        self._agent_id = None
        self._refresh_token = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.refresh_token:
            if hasattr(self.refresh_token, 'to_alipay_dict'):
                params['refresh_token'] = self.refresh_token.to_alipay_dict()
            else:
                params['refresh_token'] = self.refresh_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOauthTokenRefreshModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'refresh_token' in d:
            o.refresh_token = d['refresh_token']
        return o


