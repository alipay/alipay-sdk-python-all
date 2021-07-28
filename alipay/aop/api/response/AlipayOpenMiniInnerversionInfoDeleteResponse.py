#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionInfoDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionInfoDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionInfoDeleteResponse, self).parse_response_content(response_content)
