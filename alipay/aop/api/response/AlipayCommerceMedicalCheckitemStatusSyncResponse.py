#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCheckitemStatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCheckitemStatusSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCheckitemStatusSyncResponse, self).parse_response_content(response_content)
