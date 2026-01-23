#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHmEquityorderstatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHmEquityorderstatusSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHmEquityorderstatusSyncResponse, self).parse_response_content(response_content)
