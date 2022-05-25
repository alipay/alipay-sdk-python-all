#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RuleHitResult import RuleHitResult


class DialogueAuditResult(object):

    def __init__(self):
        self._request_id = None
        self._rule_hit_results = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def rule_hit_results(self):
        return self._rule_hit_results

    @rule_hit_results.setter
    def rule_hit_results(self, value):
        if isinstance(value, list):
            self._rule_hit_results = list()
            for i in value:
                if isinstance(i, RuleHitResult):
                    self._rule_hit_results.append(i)
                else:
                    self._rule_hit_results.append(RuleHitResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.rule_hit_results:
            if isinstance(self.rule_hit_results, list):
                for i in range(0, len(self.rule_hit_results)):
                    element = self.rule_hit_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_hit_results[i] = element.to_alipay_dict()
            if hasattr(self.rule_hit_results, 'to_alipay_dict'):
                params['rule_hit_results'] = self.rule_hit_results.to_alipay_dict()
            else:
                params['rule_hit_results'] = self.rule_hit_results
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DialogueAuditResult()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'rule_hit_results' in d:
            o.rule_hit_results = d['rule_hit_results']
        return o


