#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdcampaignPlanCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignPlanCreateormodifyResponse, self).__init__()
        self._plan_id = None
        self._plan_name = None

    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignPlanCreateormodifyResponse, self).parse_response_content(response_content)
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'plan_name' in response:
            self.plan_name = response['plan_name']
