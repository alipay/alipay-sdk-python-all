#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceFundBindCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceFundBindCancelResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceFundBindCancelResponse, self).parse_response_content(response_content)
