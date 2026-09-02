#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalDoctorMsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctorMsgSendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctorMsgSendResponse, self).parse_response_content(response_content)
