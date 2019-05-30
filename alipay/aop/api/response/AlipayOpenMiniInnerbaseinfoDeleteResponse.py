#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerbaseinfoDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerbaseinfoDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerbaseinfoDeleteResponse, self).parse_response_content(response_content)
