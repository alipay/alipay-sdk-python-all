#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdTestMtestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdTestMtestQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayBossProdTestMtestQueryResponse, self).parse_response_content(response_content)
