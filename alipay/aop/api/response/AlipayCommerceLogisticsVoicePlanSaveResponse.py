#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsVoicePlanSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsVoicePlanSaveResponse, self).__init__()
        self._logistics_voice_plan_id = None

    @property
    def logistics_voice_plan_id(self):
        return self._logistics_voice_plan_id

    @logistics_voice_plan_id.setter
    def logistics_voice_plan_id(self, value):
        self._logistics_voice_plan_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsVoicePlanSaveResponse, self).parse_response_content(response_content)
        if 'logistics_voice_plan_id' in response:
            self.logistics_voice_plan_id = response['logistics_voice_plan_id']
