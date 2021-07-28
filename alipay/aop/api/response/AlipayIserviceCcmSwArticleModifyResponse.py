#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmSwArticleModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwArticleModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwArticleModifyResponse, self).parse_response_content(response_content)
