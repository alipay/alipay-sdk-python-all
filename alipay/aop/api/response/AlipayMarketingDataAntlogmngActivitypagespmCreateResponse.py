#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingDataAntlogmngActivitypagespmCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingDataAntlogmngActivitypagespmCreateResponse, self).__init__()
        self._issuc = None
        self._message = None

    @property
    def issuc(self):
        return self._issuc

    @issuc.setter
    def issuc(self, value):
        self._issuc = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingDataAntlogmngActivitypagespmCreateResponse, self).parse_response_content(response_content)
        if 'issuc' in response:
            self.issuc = response['issuc']
        if 'message' in response:
            self.message = response['message']
