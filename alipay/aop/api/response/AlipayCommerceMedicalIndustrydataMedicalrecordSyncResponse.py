#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIndustrydataMedicalrecordSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataMedicalrecordSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataMedicalrecordSyncResponse, self).parse_response_content(response_content)
