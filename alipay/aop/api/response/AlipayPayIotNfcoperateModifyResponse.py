#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayIotNfcoperateModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayIotNfcoperateModifyResponse, self).__init__()
        self._operate_plan = None

    @property
    def operate_plan(self):
        return self._operate_plan

    @operate_plan.setter
    def operate_plan(self, value):
        self._operate_plan = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayIotNfcoperateModifyResponse, self).parse_response_content(response_content)
        if 'operate_plan' in response:
            self.operate_plan = response['operate_plan']
