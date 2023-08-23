#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseDatabaseCommandApplyModel(object):

    def __init__(self):
        self._args = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._command = None

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, value):
        self._args = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value


    def to_alipay_dict(self):
        params = dict()
        if self.args:
            if hasattr(self.args, 'to_alipay_dict'):
                params['args'] = self.args.to_alipay_dict()
            else:
                params['args'] = self.args
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.command:
            if hasattr(self.command, 'to_alipay_dict'):
                params['command'] = self.command.to_alipay_dict()
            else:
                params['command'] = self.command
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseDatabaseCommandApplyModel()
        if 'args' in d:
            o.args = d['args']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'command' in d:
            o.command = d['command']
        return o


