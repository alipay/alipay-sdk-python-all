#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdPlan import AdPlan


class AlipayCommerceTransportAdPlanGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdPlanGetResponse, self).__init__()
        self._plan_result = None

    @property
    def plan_result(self):
        return self._plan_result

    @plan_result.setter
    def plan_result(self, value):
        if isinstance(value, AdPlan):
            self._plan_result = value
        else:
            self._plan_result = AdPlan.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdPlanGetResponse, self).parse_response_content(response_content)
        if 'plan_result' in response:
            self.plan_result = response['plan_result']
