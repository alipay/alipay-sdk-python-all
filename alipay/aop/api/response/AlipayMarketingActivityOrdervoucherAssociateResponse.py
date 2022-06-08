#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingActivityOrdervoucherAssociateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherAssociateResponse, self).__init__()
        self._associate_time = None

    @property
    def associate_time(self):
        return self._associate_time

    @associate_time.setter
    def associate_time(self, value):
        self._associate_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherAssociateResponse, self).parse_response_content(response_content)
        if 'associate_time' in response:
            self.associate_time = response['associate_time']
