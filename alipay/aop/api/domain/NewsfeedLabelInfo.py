#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewsfeedLabelInfo(object):

    def __init__(self):
        self._action = None
        self._scheme = None
        self._target = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, value):
        self._scheme = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.scheme:
            if hasattr(self.scheme, 'to_alipay_dict'):
                params['scheme'] = self.scheme.to_alipay_dict()
            else:
                params['scheme'] = self.scheme
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NewsfeedLabelInfo()
        if 'action' in d:
            o.action = d['action']
        if 'scheme' in d:
            o.scheme = d['scheme']
        if 'target' in d:
            o.target = d['target']
        return o


