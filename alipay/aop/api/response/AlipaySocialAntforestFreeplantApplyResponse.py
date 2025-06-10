#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestFreeplantApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestFreeplantApplyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestFreeplantApplyResponse, self).parse_response_content(response_content)
