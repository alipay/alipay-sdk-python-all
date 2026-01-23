#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalUserHomedoctorSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalUserHomedoctorSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalUserHomedoctorSyncResponse, self).parse_response_content(response_content)
