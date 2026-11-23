#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceEncryptfileTransformResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceEncryptfileTransformResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceEncryptfileTransformResponse, self).parse_response_content(response_content)
