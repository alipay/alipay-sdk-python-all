#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountSignResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountSignResponse, self).parse_response_content(response_content)
