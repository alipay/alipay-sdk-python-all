#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniOrderInstallmentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderInstallmentCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderInstallmentCreateResponse, self).parse_response_content(response_content)
