#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerZmcardProfessionalAddResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerZmcardProfessionalAddResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerZmcardProfessionalAddResponse, self).parse_response_content(response_content)
