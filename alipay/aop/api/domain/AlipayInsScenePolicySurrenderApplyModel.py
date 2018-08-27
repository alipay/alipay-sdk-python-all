#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsScenePolicySurrenderApplyModel(object):

    def __init__(self):
        self._biz_data = None
        self._policy_no = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
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
        o = AlipayInsScenePolicySurrenderApplyModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        return o


