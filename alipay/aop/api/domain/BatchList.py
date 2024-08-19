#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BatchList(object):

    def __init__(self):
        self._action = None
        self._count = None
        self._object_being_acted = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def object_being_acted(self):
        return self._object_being_acted

    @object_being_acted.setter
    def object_being_acted(self, value):
        self._object_being_acted = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.object_being_acted:
            if hasattr(self.object_being_acted, 'to_alipay_dict'):
                params['object_being_acted'] = self.object_being_acted.to_alipay_dict()
            else:
                params['object_being_acted'] = self.object_being_acted
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchList()
        if 'action' in d:
            o.action = d['action']
        if 'count' in d:
            o.count = d['count']
        if 'object_being_acted' in d:
            o.object_being_acted = d['object_being_acted']
        return o


