#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Hylabel(object):

    def __init__(self):
        self._id = None
        self._name = None
        self._probabilities = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def probabilities(self):
        return self._probabilities

    @probabilities.setter
    def probabilities(self, value):
        self._probabilities = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.probabilities:
            if hasattr(self.probabilities, 'to_alipay_dict'):
                params['probabilities'] = self.probabilities.to_alipay_dict()
            else:
                params['probabilities'] = self.probabilities
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Hylabel()
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'probabilities' in d:
            o.probabilities = d['probabilities']
        return o


