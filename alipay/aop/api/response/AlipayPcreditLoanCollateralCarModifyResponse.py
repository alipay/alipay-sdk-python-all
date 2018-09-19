#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanCollateralCarModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanCollateralCarModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanCollateralCarModifyResponse, self).parse_response_content(response_content)
