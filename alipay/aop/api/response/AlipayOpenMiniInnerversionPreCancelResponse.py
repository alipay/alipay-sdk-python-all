#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionPreCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionPreCancelResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionPreCancelResponse, self).parse_response_content(response_content)
