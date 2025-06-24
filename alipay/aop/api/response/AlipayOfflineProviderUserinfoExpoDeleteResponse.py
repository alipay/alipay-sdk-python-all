#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderUserinfoExpoDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderUserinfoExpoDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderUserinfoExpoDeleteResponse, self).parse_response_content(response_content)
