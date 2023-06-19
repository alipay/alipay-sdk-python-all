#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Pariticipant(object):

    def __init__(self):
        self._identity = None
        self._identity_type = None
        self._name = None
        self._settle_in_time = None

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def settle_in_time(self):
        return self._settle_in_time

    @settle_in_time.setter
    def settle_in_time(self, value):
        self._settle_in_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.settle_in_time:
            if hasattr(self.settle_in_time, 'to_alipay_dict'):
                params['settle_in_time'] = self.settle_in_time.to_alipay_dict()
            else:
                params['settle_in_time'] = self.settle_in_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Pariticipant()
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'name' in d:
            o.name = d['name']
        if 'settle_in_time' in d:
            o.settle_in_time = d['settle_in_time']
        return o


