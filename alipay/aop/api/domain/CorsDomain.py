#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorsDomain(object):

    def __init__(self):
        self._domain_name = None

    @property
    def domain_name(self):
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        self._domain_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.domain_name:
            if hasattr(self.domain_name, 'to_alipay_dict'):
                params['domain_name'] = self.domain_name.to_alipay_dict()
            else:
                params['domain_name'] = self.domain_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorsDomain()
        if 'domain_name' in d:
            o.domain_name = d['domain_name']
        return o


