#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceCpaNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceCpaNotifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceCpaNotifyResponse, self).parse_response_content(response_content)
