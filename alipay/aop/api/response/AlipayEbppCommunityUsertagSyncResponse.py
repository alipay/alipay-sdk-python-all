#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityUsertagSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityUsertagSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityUsertagSyncResponse, self).parse_response_content(response_content)
