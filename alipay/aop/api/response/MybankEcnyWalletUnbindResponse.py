#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyWalletUnbindResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyWalletUnbindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(MybankEcnyWalletUnbindResponse, self).parse_response_content(response_content)
