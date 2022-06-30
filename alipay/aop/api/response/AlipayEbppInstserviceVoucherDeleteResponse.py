#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceVoucherDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceVoucherDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceVoucherDeleteResponse, self).parse_response_content(response_content)
