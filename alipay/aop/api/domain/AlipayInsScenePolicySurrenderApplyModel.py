#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsScenePolicySurrenderApplyModel(object):

    def __init__(self):
        self._biz_data = None
        self._policy_no = None
        self._surrender_price_type = None
        self._surrender_reason = None
        self._surrender_time = None

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
    @property
    def surrender_price_type(self):
        return self._surrender_price_type

    @surrender_price_type.setter
    def surrender_price_type(self, value):
        self._surrender_price_type = value
    @property
    def surrender_reason(self):
        return self._surrender_reason

    @surrender_reason.setter
    def surrender_reason(self, value):
        self._surrender_reason = value
    @property
    def surrender_time(self):
        return self._surrender_time

    @surrender_time.setter
    def surrender_time(self, value):
        self._surrender_time = value


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
        if self.surrender_price_type:
            if hasattr(self.surrender_price_type, 'to_alipay_dict'):
                params['surrender_price_type'] = self.surrender_price_type.to_alipay_dict()
            else:
                params['surrender_price_type'] = self.surrender_price_type
        if self.surrender_reason:
            if hasattr(self.surrender_reason, 'to_alipay_dict'):
                params['surrender_reason'] = self.surrender_reason.to_alipay_dict()
            else:
                params['surrender_reason'] = self.surrender_reason
        if self.surrender_time:
            if hasattr(self.surrender_time, 'to_alipay_dict'):
                params['surrender_time'] = self.surrender_time.to_alipay_dict()
            else:
                params['surrender_time'] = self.surrender_time
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
        if 'surrender_price_type' in d:
            o.surrender_price_type = d['surrender_price_type']
        if 'surrender_reason' in d:
            o.surrender_reason = d['surrender_reason']
        if 'surrender_time' in d:
            o.surrender_time = d['surrender_time']
        return o


