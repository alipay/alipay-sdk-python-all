#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Argument(object):

    def __init__(self):
        self._args = None
        self._gmt_modified = None
        self._name = None

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, value):
        self._args = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.args:
            if hasattr(self.args, 'to_alipay_dict'):
                params['args'] = self.args.to_alipay_dict()
            else:
                params['args'] = self.args
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Argument()
        if 'args' in d:
            o.args = d['args']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'name' in d:
            o.name = d['name']
        return o


