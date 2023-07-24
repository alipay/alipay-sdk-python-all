#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneParams(object):

    def __init__(self):
        self._auth_flag = None
        self._call_back_action_code = None
        self._env_data = None
        self._render_group = None

    @property
    def auth_flag(self):
        return self._auth_flag

    @auth_flag.setter
    def auth_flag(self, value):
        self._auth_flag = value
    @property
    def call_back_action_code(self):
        return self._call_back_action_code

    @call_back_action_code.setter
    def call_back_action_code(self, value):
        self._call_back_action_code = value
    @property
    def env_data(self):
        return self._env_data

    @env_data.setter
    def env_data(self, value):
        self._env_data = value
    @property
    def render_group(self):
        return self._render_group

    @render_group.setter
    def render_group(self, value):
        self._render_group = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_flag:
            if hasattr(self.auth_flag, 'to_alipay_dict'):
                params['auth_flag'] = self.auth_flag.to_alipay_dict()
            else:
                params['auth_flag'] = self.auth_flag
        if self.call_back_action_code:
            if hasattr(self.call_back_action_code, 'to_alipay_dict'):
                params['call_back_action_code'] = self.call_back_action_code.to_alipay_dict()
            else:
                params['call_back_action_code'] = self.call_back_action_code
        if self.env_data:
            if hasattr(self.env_data, 'to_alipay_dict'):
                params['env_data'] = self.env_data.to_alipay_dict()
            else:
                params['env_data'] = self.env_data
        if self.render_group:
            if hasattr(self.render_group, 'to_alipay_dict'):
                params['render_group'] = self.render_group.to_alipay_dict()
            else:
                params['render_group'] = self.render_group
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneParams()
        if 'auth_flag' in d:
            o.auth_flag = d['auth_flag']
        if 'call_back_action_code' in d:
            o.call_back_action_code = d['call_back_action_code']
        if 'env_data' in d:
            o.env_data = d['env_data']
        if 'render_group' in d:
            o.render_group = d['render_group']
        return o


