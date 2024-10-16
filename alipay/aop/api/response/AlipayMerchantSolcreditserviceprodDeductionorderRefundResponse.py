#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantSolcreditserviceprodDeductionorderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolcreditserviceprodDeductionorderRefundResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolcreditserviceprodDeductionorderRefundResponse, self).parse_response_content(response_content)
