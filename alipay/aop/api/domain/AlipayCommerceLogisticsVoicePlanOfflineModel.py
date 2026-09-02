#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsVoicePlanOfflineModel(object):

    def __init__(self):
        self._logistics_voice_plan_id = None

    @property
    def logistics_voice_plan_id(self):
        return self._logistics_voice_plan_id

    @logistics_voice_plan_id.setter
    def logistics_voice_plan_id(self, value):
        self._logistics_voice_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_voice_plan_id:
            if hasattr(self.logistics_voice_plan_id, 'to_alipay_dict'):
                params['logistics_voice_plan_id'] = self.logistics_voice_plan_id.to_alipay_dict()
            else:
                params['logistics_voice_plan_id'] = self.logistics_voice_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsVoicePlanOfflineModel()
        if 'logistics_voice_plan_id' in d:
            o.logistics_voice_plan_id = d['logistics_voice_plan_id']
        return o


