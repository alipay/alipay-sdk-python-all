#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserPointRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPointRefundResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserPointRefundResponse, self).parse_response_content(response_content)
