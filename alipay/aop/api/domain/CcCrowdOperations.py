#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CcCrowdOperations(object):

    def __init__(self):
        self._crowd_id = None
        self._deadline = None
        self._operator = None
        self._ttl = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def ttl(self):
        return self._ttl

    @ttl.setter
    def ttl(self, value):
        self._ttl = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.deadline:
            if hasattr(self.deadline, 'to_alipay_dict'):
                params['deadline'] = self.deadline.to_alipay_dict()
            else:
                params['deadline'] = self.deadline
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.ttl:
            if hasattr(self.ttl, 'to_alipay_dict'):
                params['ttl'] = self.ttl.to_alipay_dict()
            else:
                params['ttl'] = self.ttl
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CcCrowdOperations()
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'deadline' in d:
            o.deadline = d['deadline']
        if 'operator' in d:
            o.operator = d['operator']
        if 'ttl' in d:
            o.ttl = d['ttl']
        return o


