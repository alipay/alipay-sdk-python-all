#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRecycleOrderInspectConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleOrderInspectConfirmResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleOrderInspectConfirmResponse, self).parse_response_content(response_content)
