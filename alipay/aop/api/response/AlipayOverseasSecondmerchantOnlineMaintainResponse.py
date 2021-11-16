#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasSecondmerchantOnlineMaintainResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasSecondmerchantOnlineMaintainResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOverseasSecondmerchantOnlineMaintainResponse, self).parse_response_content(response_content)
