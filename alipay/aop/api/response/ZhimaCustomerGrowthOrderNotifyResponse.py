#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerGrowthOrderNotifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerGrowthOrderNotifyResponse, self).__init__()
        self._process_status = None

    @property
    def process_status(self):
        return self._process_status

    @process_status.setter
    def process_status(self, value):
        self._process_status = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerGrowthOrderNotifyResponse, self).parse_response_content(response_content)
        if 'process_status' in response:
            self.process_status = response['process_status']
