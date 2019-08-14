#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KeyWordDTO import KeyWordDTO


class AlipayIserviceCognitiveClassificationWasteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveClassificationWasteQueryResponse, self).__init__()
        self._cognition_type = None
        self._err_code = None
        self._err_msg = None
        self._key_words = None
        self._origin_content = None
        self._rewrite_content = None
        self._success = None
        self._trace_id = None

    @property
    def cognition_type(self):
        return self._cognition_type

    @cognition_type.setter
    def cognition_type(self, value):
        self._cognition_type = value
    @property
    def err_code(self):
        return self._err_code

    @err_code.setter
    def err_code(self, value):
        self._err_code = value
    @property
    def err_msg(self):
        return self._err_msg

    @err_msg.setter
    def err_msg(self, value):
        self._err_msg = value
    @property
    def key_words(self):
        return self._key_words

    @key_words.setter
    def key_words(self, value):
        if isinstance(value, list):
            self._key_words = list()
            for i in value:
                if isinstance(i, KeyWordDTO):
                    self._key_words.append(i)
                else:
                    self._key_words.append(KeyWordDTO.from_alipay_dict(i))
    @property
    def origin_content(self):
        return self._origin_content

    @origin_content.setter
    def origin_content(self, value):
        self._origin_content = value
    @property
    def rewrite_content(self):
        return self._rewrite_content

    @rewrite_content.setter
    def rewrite_content(self, value):
        self._rewrite_content = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveClassificationWasteQueryResponse, self).parse_response_content(response_content)
        if 'cognition_type' in response:
            self.cognition_type = response['cognition_type']
        if 'err_code' in response:
            self.err_code = response['err_code']
        if 'err_msg' in response:
            self.err_msg = response['err_msg']
        if 'key_words' in response:
            self.key_words = response['key_words']
        if 'origin_content' in response:
            self.origin_content = response['origin_content']
        if 'rewrite_content' in response:
            self.rewrite_content = response['rewrite_content']
        if 'success' in response:
            self.success = response['success']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
