#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiAdvertCommissionChannelDeleteResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertCommissionChannelDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertCommissionChannelDeleteResponse, self).parse_response_content(response_content)
