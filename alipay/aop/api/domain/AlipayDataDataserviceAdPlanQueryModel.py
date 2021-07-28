#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdPlanQueryModel(object):

    def __init__(self):
        self._biz_token = None
        self._plan_outer_id = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def plan_outer_id(self):
        return self._plan_outer_id

    @plan_outer_id.setter
    def plan_outer_id(self, value):
        self._plan_outer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.plan_outer_id:
            if hasattr(self.plan_outer_id, 'to_alipay_dict'):
                params['plan_outer_id'] = self.plan_outer_id.to_alipay_dict()
            else:
                params['plan_outer_id'] = self.plan_outer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdPlanQueryModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'plan_outer_id' in d:
            o.plan_outer_id = d['plan_outer_id']
        return o


