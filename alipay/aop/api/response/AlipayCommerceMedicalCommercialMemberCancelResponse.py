#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCommercialMemberCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialMemberCancelResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialMemberCancelResponse, self).parse_response_content(response_content)
