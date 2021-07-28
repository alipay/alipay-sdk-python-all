#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoContractProcessDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoContractProcessDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoContractProcessDeleteResponse, self).parse_response_content(response_content)
