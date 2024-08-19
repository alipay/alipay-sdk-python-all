#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistCarfinRepayplanchangeNotifyResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistCarfinRepayplanchangeNotifyResponse, self).__init__()
        self._repayplan_content = None

    @property
    def repayplan_content(self):
        return self._repayplan_content

    @repayplan_content.setter
    def repayplan_content(self, value):
        self._repayplan_content = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistCarfinRepayplanchangeNotifyResponse, self).parse_response_content(response_content)
        if 'repayplan_content' in response:
            self.repayplan_content = response['repayplan_content']
