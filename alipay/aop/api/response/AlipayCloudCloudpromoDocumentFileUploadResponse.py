#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoDocumentFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoDocumentFileUploadResponse, self).__init__()
        self._document_id = None

    @property
    def document_id(self):
        return self._document_id

    @document_id.setter
    def document_id(self, value):
        self._document_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoDocumentFileUploadResponse, self).parse_response_content(response_content)
        if 'document_id' in response:
            self.document_id = response['document_id']
