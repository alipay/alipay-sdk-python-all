#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserLoginCodeGetModel(object):

    def __init__(self):
        self._agent_app_id = None
        self._agent_pid = None
        self._agent_user_id = None

    @property
    def agent_app_id(self):
        return self._agent_app_id

    @agent_app_id.setter
    def agent_app_id(self, value):
        self._agent_app_id = value
    @property
    def agent_pid(self):
        return self._agent_pid

    @agent_pid.setter
    def agent_pid(self, value):
        self._agent_pid = value
    @property
    def agent_user_id(self):
        return self._agent_user_id

    @agent_user_id.setter
    def agent_user_id(self, value):
        self._agent_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_app_id:
            if hasattr(self.agent_app_id, 'to_alipay_dict'):
                params['agent_app_id'] = self.agent_app_id.to_alipay_dict()
            else:
                params['agent_app_id'] = self.agent_app_id
        if self.agent_pid:
            if hasattr(self.agent_pid, 'to_alipay_dict'):
                params['agent_pid'] = self.agent_pid.to_alipay_dict()
            else:
                params['agent_pid'] = self.agent_pid
        if self.agent_user_id:
            if hasattr(self.agent_user_id, 'to_alipay_dict'):
                params['agent_user_id'] = self.agent_user_id.to_alipay_dict()
            else:
                params['agent_user_id'] = self.agent_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserLoginCodeGetModel()
        if 'agent_app_id' in d:
            o.agent_app_id = d['agent_app_id']
        if 'agent_pid' in d:
            o.agent_pid = d['agent_pid']
        if 'agent_user_id' in d:
            o.agent_user_id = d['agent_user_id']
        return o


