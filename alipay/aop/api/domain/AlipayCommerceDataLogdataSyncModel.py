#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDataLogdataSyncModel(object):

    def __init__(self):
        self._log = None
        self._namespace = None

    @property
    def log(self):
        return self._log

    @log.setter
    def log(self, value):
        self._log = value
    @property
    def namespace(self):
        return self._namespace

    @namespace.setter
    def namespace(self, value):
        self._namespace = value


    def to_alipay_dict(self):
        params = dict()
        if self.log:
            if hasattr(self.log, 'to_alipay_dict'):
                params['log'] = self.log.to_alipay_dict()
            else:
                params['log'] = self.log
        if self.namespace:
            if hasattr(self.namespace, 'to_alipay_dict'):
                params['namespace'] = self.namespace.to_alipay_dict()
            else:
                params['namespace'] = self.namespace
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataLogdataSyncModel()
        if 'log' in d:
            o.log = d['log']
        if 'namespace' in d:
            o.namespace = d['namespace']
        return o


