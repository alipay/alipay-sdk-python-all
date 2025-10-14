#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalPromoEventNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPromoEventNotifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPromoEventNotifyResponse, self).parse_response_content(response_content)
