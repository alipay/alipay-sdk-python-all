#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankDailybillCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankDailybillCreateResponse, self).__init__()
        self._bill_application_id = None

    @property
    def bill_application_id(self):
        return self._bill_application_id

    @bill_application_id.setter
    def bill_application_id(self, value):
        self._bill_application_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankDailybillCreateResponse, self).parse_response_content(response_content)
        if 'bill_application_id' in response:
            self.bill_application_id = response['bill_application_id']
