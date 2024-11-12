#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationDistributionPhonecardPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDistributionPhonecardPreconsultResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDistributionPhonecardPreconsultResponse, self).parse_response_content(response_content)
