#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRpcQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRpcQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRpcQueryResponse, self).parse_response_content(response_content)
