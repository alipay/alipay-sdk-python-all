#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNpromoactivityCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpromoactivityCancelResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpromoactivityCancelResponse, self).parse_response_content(response_content)
