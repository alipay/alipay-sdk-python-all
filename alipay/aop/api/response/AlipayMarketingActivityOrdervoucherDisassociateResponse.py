#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingActivityOrdervoucherDisassociateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherDisassociateResponse, self).__init__()
        self._disassociate_time = None

    @property
    def disassociate_time(self):
        return self._disassociate_time

    @disassociate_time.setter
    def disassociate_time(self, value):
        self._disassociate_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherDisassociateResponse, self).parse_response_content(response_content)
        if 'disassociate_time' in response:
            self.disassociate_time = response['disassociate_time']
