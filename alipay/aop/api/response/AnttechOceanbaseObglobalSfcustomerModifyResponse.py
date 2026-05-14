#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseObglobalSfcustomerModifyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalSfcustomerModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalSfcustomerModifyResponse, self).parse_response_content(response_content)
