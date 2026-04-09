#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMarketingTaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMarketingTaskCreateResponse, self).__init__()
        self._plan_id = None
        self._status_code = None

    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMarketingTaskCreateResponse, self).parse_response_content(response_content)
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'status_code' in response:
            self.status_code = response['status_code']
