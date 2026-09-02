#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalDoctorMsgcountSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctorMsgcountSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctorMsgcountSyncResponse, self).parse_response_content(response_content)
