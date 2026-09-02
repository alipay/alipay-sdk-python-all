#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalServiceuserAuthticketVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServiceuserAuthticketVerifyResponse, self).__init__()
        self._doc_id = None
        self._health_doc_id = None

    @property
    def doc_id(self):
        return self._doc_id

    @doc_id.setter
    def doc_id(self, value):
        self._doc_id = value
    @property
    def health_doc_id(self):
        return self._health_doc_id

    @health_doc_id.setter
    def health_doc_id(self, value):
        self._health_doc_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServiceuserAuthticketVerifyResponse, self).parse_response_content(response_content)
        if 'doc_id' in response:
            self.doc_id = response['doc_id']
        if 'health_doc_id' in response:
            self.health_doc_id = response['health_doc_id']
