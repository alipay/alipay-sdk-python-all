#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingActivityOrdervoucherRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherRefundResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherRefundResponse, self).parse_response_content(response_content)
