#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DocumentInfo import DocumentInfo
from alipay.aop.api.domain.FaqInfo import FaqInfo


class DatadigitalAnttechDtsparkChatQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechDtsparkChatQueryResponse, self).__init__()
        self._content = None
        self._doc_infos = None
        self._faqs = None
        self._session_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def doc_infos(self):
        return self._doc_infos

    @doc_infos.setter
    def doc_infos(self, value):
        if isinstance(value, list):
            self._doc_infos = list()
            for i in value:
                if isinstance(i, DocumentInfo):
                    self._doc_infos.append(i)
                else:
                    self._doc_infos.append(DocumentInfo.from_alipay_dict(i))
    @property
    def faqs(self):
        return self._faqs

    @faqs.setter
    def faqs(self, value):
        if isinstance(value, list):
            self._faqs = list()
            for i in value:
                if isinstance(i, FaqInfo):
                    self._faqs.append(i)
                else:
                    self._faqs.append(FaqInfo.from_alipay_dict(i))
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechDtsparkChatQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'doc_infos' in response:
            self.doc_infos = response['doc_infos']
        if 'faqs' in response:
            self.faqs = response['faqs']
        if 'session_id' in response:
            self.session_id = response['session_id']
