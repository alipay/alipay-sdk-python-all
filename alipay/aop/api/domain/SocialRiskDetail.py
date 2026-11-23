#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SocialRiskDetail(object):

    def __init__(self):
        self._count = None
        self._elimination_rule_result = None
        self._has = None
        self._name = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def elimination_rule_result(self):
        return self._elimination_rule_result

    @elimination_rule_result.setter
    def elimination_rule_result(self, value):
        self._elimination_rule_result = value
    @property
    def has(self):
        return self._has

    @has.setter
    def has(self, value):
        self._has = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.elimination_rule_result:
            if hasattr(self.elimination_rule_result, 'to_alipay_dict'):
                params['elimination_rule_result'] = self.elimination_rule_result.to_alipay_dict()
            else:
                params['elimination_rule_result'] = self.elimination_rule_result
        if self.has:
            if hasattr(self.has, 'to_alipay_dict'):
                params['has'] = self.has.to_alipay_dict()
            else:
                params['has'] = self.has
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
        o = SocialRiskDetail()
        if 'count' in d:
            o.count = d['count']
        if 'elimination_rule_result' in d:
            o.elimination_rule_result = d['elimination_rule_result']
        if 'has' in d:
            o.has = d['has']
        if 'name' in d:
            o.name = d['name']
        return o


