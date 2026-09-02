#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAiKnowledgeDocumentModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAiKnowledgeDocumentModifyResponse, self).__init__()
        self._data_source_id = None
        self._document_id = None
        self._submit_status = None

    @property
    def data_source_id(self):
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, value):
        self._data_source_id = value
    @property
    def document_id(self):
        return self._document_id

    @document_id.setter
    def document_id(self, value):
        self._document_id = value
    @property
    def submit_status(self):
        return self._submit_status

    @submit_status.setter
    def submit_status(self, value):
        self._submit_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAiKnowledgeDocumentModifyResponse, self).parse_response_content(response_content)
        if 'data_source_id' in response:
            self.data_source_id = response['data_source_id']
        if 'document_id' in response:
            self.document_id = response['document_id']
        if 'submit_status' in response:
            self.submit_status = response['submit_status']
