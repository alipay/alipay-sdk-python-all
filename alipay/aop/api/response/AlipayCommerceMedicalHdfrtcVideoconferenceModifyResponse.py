#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfrtcVideoconferenceModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcVideoconferenceModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcVideoconferenceModifyResponse, self).parse_response_content(response_content)
