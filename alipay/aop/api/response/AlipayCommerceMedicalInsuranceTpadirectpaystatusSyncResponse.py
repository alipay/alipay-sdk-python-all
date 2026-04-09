#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceTpadirectpaystatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceTpadirectpaystatusSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceTpadirectpaystatusSyncResponse, self).parse_response_content(response_content)
