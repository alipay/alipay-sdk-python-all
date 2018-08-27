#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMerchantDepartmentBatchBindResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantDepartmentBatchBindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantDepartmentBatchBindResponse, self).parse_response_content(response_content)
