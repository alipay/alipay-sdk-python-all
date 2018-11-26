#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportAdPlanCertifyModel(object):

    def __init__(self):
        self._ad_user_id = None
        self._plan_id = None

    @property
    def ad_user_id(self):
        return self._ad_user_id

    @ad_user_id.setter
    def ad_user_id(self, value):
        self._ad_user_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_user_id:
            if hasattr(self.ad_user_id, 'to_alipay_dict'):
                params['ad_user_id'] = self.ad_user_id.to_alipay_dict()
            else:
                params['ad_user_id'] = self.ad_user_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportAdPlanCertifyModel()
        if 'ad_user_id' in d:
            o.ad_user_id = d['ad_user_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        return o


