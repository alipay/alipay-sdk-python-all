#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerappPluginsyncmodeModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerappPluginsyncmodeModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerappPluginsyncmodeModifyResponse, self).parse_response_content(response_content)
