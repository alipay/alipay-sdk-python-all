#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransAppConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransAppConsultResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayFundTransAppConsultResponse, self).parse_response_content(response_content)
