#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClaimResultPolicyInfo(object):

    def __init__(self):
        self._dplan_code = None
        self._policy_no = None

    @property
    def dplan_code(self):
        return self._dplan_code

    @dplan_code.setter
    def dplan_code(self, value):
        self._dplan_code = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.dplan_code:
            if hasattr(self.dplan_code, 'to_alipay_dict'):
                params['dplan_code'] = self.dplan_code.to_alipay_dict()
            else:
                params['dplan_code'] = self.dplan_code
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClaimResultPolicyInfo()
        if 'dplan_code' in d:
            o.dplan_code = d['dplan_code']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        return o


