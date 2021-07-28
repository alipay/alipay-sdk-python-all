#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItapDeviceControlAction(object):

    def __init__(self):
        self._action = None
        self._params = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItapDeviceControlAction()
        if 'action' in d:
            o.action = d['action']
        if 'params' in d:
            o.params = d['params']
        return o


