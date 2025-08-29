#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoKnowledgeDocumentUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoKnowledgeDocumentUnbindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoKnowledgeDocumentUnbindResponse, self).parse_response_content(response_content)
