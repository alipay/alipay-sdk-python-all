#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceIsresourceThirdaccountModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIsresourceThirdaccountModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIsresourceThirdaccountModifyResponse, self).parse_response_content(response_content)
