#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDaoweiOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDaoweiOrderRefundResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDaoweiOrderRefundResponse, self).parse_response_content(response_content)
