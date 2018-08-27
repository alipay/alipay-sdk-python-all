#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingVoucherTemplateDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherTemplateDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherTemplateDeleteResponse, self).parse_response_content(response_content)
