#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskHufuAuthCreateModel(object):

    def __init__(self):
        self._callback = None
        self._policy = None
        self._serial = None
        self._strategies = None
        self._uid = None
        self._user = None

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, value):
        self._callback = value
    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, value):
        self._policy = value
    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, value):
        self._serial = value
    @property
    def strategies(self):
        return self._strategies

    @strategies.setter
    def strategies(self, value):
        self._strategies = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value


    def to_alipay_dict(self):
        params = dict()
        if self.callback:
            if hasattr(self.callback, 'to_alipay_dict'):
                params['callback'] = self.callback.to_alipay_dict()
            else:
                params['callback'] = self.callback
        if self.policy:
            if hasattr(self.policy, 'to_alipay_dict'):
                params['policy'] = self.policy.to_alipay_dict()
            else:
                params['policy'] = self.policy
        if self.serial:
            if hasattr(self.serial, 'to_alipay_dict'):
                params['serial'] = self.serial.to_alipay_dict()
            else:
                params['serial'] = self.serial
        if self.strategies:
            if hasattr(self.strategies, 'to_alipay_dict'):
                params['strategies'] = self.strategies.to_alipay_dict()
            else:
                params['strategies'] = self.strategies
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskHufuAuthCreateModel()
        if 'callback' in d:
            o.callback = d['callback']
        if 'policy' in d:
            o.policy = d['policy']
        if 'serial' in d:
            o.serial = d['serial']
        if 'strategies' in d:
            o.strategies = d['strategies']
        if 'uid' in d:
            o.uid = d['uid']
        if 'user' in d:
            o.user = d['user']
        return o


