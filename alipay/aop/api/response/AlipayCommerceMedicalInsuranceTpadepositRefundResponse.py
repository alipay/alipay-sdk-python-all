#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceTpadepositRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceTpadepositRefundResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceTpadepositRefundResponse, self).parse_response_content(response_content)
