#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalServicepackageServicelauchCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServicepackageServicelauchCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServicepackageServicelauchCreateResponse, self).parse_response_content(response_content)
