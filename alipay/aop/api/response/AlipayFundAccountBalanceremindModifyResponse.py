#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAccountBalanceremindModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountBalanceremindModifyResponse, self).__init__()
        self._plan_version = None

    @property
    def plan_version(self):
        return self._plan_version

    @plan_version.setter
    def plan_version(self, value):
        self._plan_version = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountBalanceremindModifyResponse, self).parse_response_content(response_content)
        if 'plan_version' in response:
            self.plan_version = response['plan_version']
