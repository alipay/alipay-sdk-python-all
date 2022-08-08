#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountAccountModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountAccountModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountAccountModifyResponse, self).parse_response_content(response_content)
