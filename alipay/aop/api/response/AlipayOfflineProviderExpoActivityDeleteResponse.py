#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderExpoActivityDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderExpoActivityDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderExpoActivityDeleteResponse, self).parse_response_content(response_content)
