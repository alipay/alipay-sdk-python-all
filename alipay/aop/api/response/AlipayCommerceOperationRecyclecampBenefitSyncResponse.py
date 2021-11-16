#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationRecyclecampBenefitSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationRecyclecampBenefitSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationRecyclecampBenefitSyncResponse, self).parse_response_content(response_content)
