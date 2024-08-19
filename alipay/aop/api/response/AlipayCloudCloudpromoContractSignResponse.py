#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoContractSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoContractSignResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoContractSignResponse, self).parse_response_content(response_content)
