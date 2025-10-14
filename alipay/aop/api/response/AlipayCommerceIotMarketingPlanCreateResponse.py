#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMarketingPlanCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMarketingPlanCreateResponse, self).__init__()
        self._plan_id = None
        self._status = None

    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMarketingPlanCreateResponse, self).parse_response_content(response_content)
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'status' in response:
            self.status = response['status']
