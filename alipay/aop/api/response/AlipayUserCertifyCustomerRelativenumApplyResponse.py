#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyCustomerRelativenumApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyCustomerRelativenumApplyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyCustomerRelativenumApplyResponse, self).parse_response_content(response_content)
