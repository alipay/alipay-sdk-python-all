#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIndustrydataUserdoctorrelationSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataUserdoctorrelationSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataUserdoctorrelationSyncResponse, self).parse_response_content(response_content)
