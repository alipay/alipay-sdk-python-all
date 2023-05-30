#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClassMethodConfig(object):

    def __init__(self):
        self._class_name = None
        self._methods = None

    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = value
    @property
    def methods(self):
        return self._methods

    @methods.setter
    def methods(self, value):
        self._methods = value


    def to_alipay_dict(self):
        params = dict()
        if self.class_name:
            if hasattr(self.class_name, 'to_alipay_dict'):
                params['class_name'] = self.class_name.to_alipay_dict()
            else:
                params['class_name'] = self.class_name
        if self.methods:
            if hasattr(self.methods, 'to_alipay_dict'):
                params['methods'] = self.methods.to_alipay_dict()
            else:
                params['methods'] = self.methods
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClassMethodConfig()
        if 'class_name' in d:
            o.class_name = d['class_name']
        if 'methods' in d:
            o.methods = d['methods']
        return o


