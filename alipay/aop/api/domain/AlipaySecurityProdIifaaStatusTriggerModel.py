#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdIifaaStatusTriggerModel(object):

    def __init__(self):
        self._action = None
        self._request_param = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def request_param(self):
        return self._request_param

    @request_param.setter
    def request_param(self, value):
        self._request_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.request_param:
            if hasattr(self.request_param, 'to_alipay_dict'):
                params['request_param'] = self.request_param.to_alipay_dict()
            else:
                params['request_param'] = self.request_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdIifaaStatusTriggerModel()
        if 'action' in d:
            o.action = d['action']
        if 'request_param' in d:
            o.request_param = d['request_param']
        return o


