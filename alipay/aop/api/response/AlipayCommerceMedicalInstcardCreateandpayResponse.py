#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInstcardCreateandpayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInstcardCreateandpayResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInstcardCreateandpayResponse, self).parse_response_content(response_content)
