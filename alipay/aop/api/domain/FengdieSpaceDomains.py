#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FengdieSpaceDomains(object):

    def __init__(self):
        self._domain = None
        self._is_default = None
        self._status = None

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
    @property
    def is_default(self):
        return self._is_default

    @is_default.setter
    def is_default(self, value):
        self._is_default = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
        if self.is_default:
            if hasattr(self.is_default, 'to_alipay_dict'):
                params['is_default'] = self.is_default.to_alipay_dict()
            else:
                params['is_default'] = self.is_default
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieSpaceDomains()
        if 'domain' in d:
            o.domain = d['domain']
        if 'is_default' in d:
            o.is_default = d['is_default']
        if 'status' in d:
            o.status = d['status']
        return o


