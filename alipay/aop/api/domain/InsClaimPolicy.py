#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsClaimPolicy(object):

    def __init__(self):
        self._policy_no = None

    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value


    def to_alipay_dict(self):
        params = dict()
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
        o = InsClaimPolicy()
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        return o


