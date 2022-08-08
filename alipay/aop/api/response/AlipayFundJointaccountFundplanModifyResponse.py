#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountFundplanModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountFundplanModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountFundplanModifyResponse, self).parse_response_content(response_content)
