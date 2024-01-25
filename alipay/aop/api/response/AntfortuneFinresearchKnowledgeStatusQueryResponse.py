#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneFinresearchKnowledgeStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneFinresearchKnowledgeStatusQueryResponse, self).__init__()
        self._upload_status = None

    @property
    def upload_status(self):
        return self._upload_status

    @upload_status.setter
    def upload_status(self, value):
        self._upload_status = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneFinresearchKnowledgeStatusQueryResponse, self).parse_response_content(response_content)
        if 'upload_status' in response:
            self.upload_status = response['upload_status']
