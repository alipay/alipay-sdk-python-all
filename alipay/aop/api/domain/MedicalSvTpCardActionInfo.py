#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalSvTpCardActionInfo(object):

    def __init__(self):
        self._action_code = None
        self._action_name = None
        self._action_url = None

    @property
    def action_code(self):
        return self._action_code

    @action_code.setter
    def action_code(self, value):
        self._action_code = value
    @property
    def action_name(self):
        return self._action_name

    @action_name.setter
    def action_name(self, value):
        self._action_name = value
    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_code:
            if hasattr(self.action_code, 'to_alipay_dict'):
                params['action_code'] = self.action_code.to_alipay_dict()
            else:
                params['action_code'] = self.action_code
        if self.action_name:
            if hasattr(self.action_name, 'to_alipay_dict'):
                params['action_name'] = self.action_name.to_alipay_dict()
            else:
                params['action_name'] = self.action_name
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalSvTpCardActionInfo()
        if 'action_code' in d:
            o.action_code = d['action_code']
        if 'action_name' in d:
            o.action_name = d['action_name']
        if 'action_url' in d:
            o.action_url = d['action_url']
        return o


