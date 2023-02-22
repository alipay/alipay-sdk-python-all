#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomizeRuleResult(object):

    def __init__(self):
        self._request_id = None
        self._rule_code = None
        self._rule_status = None
        self._scene_code = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def rule_code(self):
        return self._rule_code

    @rule_code.setter
    def rule_code(self, value):
        self._rule_code = value
    @property
    def rule_status(self):
        return self._rule_status

    @rule_status.setter
    def rule_status(self, value):
        self._rule_status = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.rule_code:
            if hasattr(self.rule_code, 'to_alipay_dict'):
                params['rule_code'] = self.rule_code.to_alipay_dict()
            else:
                params['rule_code'] = self.rule_code
        if self.rule_status:
            if hasattr(self.rule_status, 'to_alipay_dict'):
                params['rule_status'] = self.rule_status.to_alipay_dict()
            else:
                params['rule_status'] = self.rule_status
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomizeRuleResult()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'rule_code' in d:
            o.rule_code = d['rule_code']
        if 'rule_status' in d:
            o.rule_status = d['rule_status']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


