#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyInfoPersonApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyInfoPersonApplyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyInfoPersonApplyResponse, self).parse_response_content(response_content)
