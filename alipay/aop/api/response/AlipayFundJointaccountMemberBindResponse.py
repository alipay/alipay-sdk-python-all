#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountMemberBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountMemberBindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountMemberBindResponse, self).parse_response_content(response_content)
