#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmSwArticlePublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwArticlePublishResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwArticlePublishResponse, self).parse_response_content(response_content)
