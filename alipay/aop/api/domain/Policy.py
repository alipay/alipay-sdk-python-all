#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PolicyDetail import PolicyDetail


class Policy(object):

    def __init__(self):
        self._airline_no = None
        self._policies = None
        self._type = None

    @property
    def airline_no(self):
        return self._airline_no

    @airline_no.setter
    def airline_no(self, value):
        self._airline_no = value
    @property
    def policies(self):
        return self._policies

    @policies.setter
    def policies(self, value):
        if isinstance(value, list):
            self._policies = list()
            for i in value:
                if isinstance(i, PolicyDetail):
                    self._policies.append(i)
                else:
                    self._policies.append(PolicyDetail.from_alipay_dict(i))
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.airline_no:
            if hasattr(self.airline_no, 'to_alipay_dict'):
                params['airline_no'] = self.airline_no.to_alipay_dict()
            else:
                params['airline_no'] = self.airline_no
        if self.policies:
            if isinstance(self.policies, list):
                for i in range(0, len(self.policies)):
                    element = self.policies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.policies[i] = element.to_alipay_dict()
            if hasattr(self.policies, 'to_alipay_dict'):
                params['policies'] = self.policies.to_alipay_dict()
            else:
                params['policies'] = self.policies
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
        o = Policy()
        if 'airline_no' in d:
            o.airline_no = d['airline_no']
        if 'policies' in d:
            o.policies = d['policies']
        if 'type' in d:
            o.type = d['type']
        return o


