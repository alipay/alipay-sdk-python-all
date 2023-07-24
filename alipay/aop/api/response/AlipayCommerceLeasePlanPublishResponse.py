#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLeasePlanPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLeasePlanPublishResponse, self).__init__()
        self._plan_id = None

    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLeasePlanPublishResponse, self).parse_response_content(response_content)
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
