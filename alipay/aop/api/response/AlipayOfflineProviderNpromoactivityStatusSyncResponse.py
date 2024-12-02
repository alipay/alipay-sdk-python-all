#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNpromoactivityStatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpromoactivityStatusSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpromoactivityStatusSyncResponse, self).parse_response_content(response_content)
