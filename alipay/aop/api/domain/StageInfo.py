#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StageInfo(object):

    def __init__(self):
        self._group = None
        self._name = None
        self._round = None
        self._type = None

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, value):
        self._round = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.group:
            if hasattr(self.group, 'to_alipay_dict'):
                params['group'] = self.group.to_alipay_dict()
            else:
                params['group'] = self.group
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.round:
            if hasattr(self.round, 'to_alipay_dict'):
                params['round'] = self.round.to_alipay_dict()
            else:
                params['round'] = self.round
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StageInfo()
        if 'group' in d:
            o.group = d['group']
        if 'name' in d:
            o.name = d['name']
        if 'round' in d:
            o.round = d['round']
        if 'type' in d:
            o.type = d['type']
        return o


