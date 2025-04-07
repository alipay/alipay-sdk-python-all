#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalStoreBusinessOfflineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalStoreBusinessOfflineResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalStoreBusinessOfflineResponse, self).parse_response_content(response_content)
