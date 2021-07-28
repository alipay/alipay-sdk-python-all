#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenBpaasPushSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenBpaasPushSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenBpaasPushSyncResponse, self).parse_response_content(response_content)
