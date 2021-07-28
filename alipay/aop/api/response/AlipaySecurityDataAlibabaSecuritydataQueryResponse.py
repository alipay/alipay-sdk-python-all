#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityDataAlibabaSecuritydataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataAlibabaSecuritydataQueryResponse, self).__init__()
        self._content = None
        self._identify_result = None
        self._risk_label = None
        self._risk_score = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def identify_result(self):
        return self._identify_result

    @identify_result.setter
    def identify_result(self, value):
        self._identify_result = value
    @property
    def risk_label(self):
        return self._risk_label

    @risk_label.setter
    def risk_label(self, value):
        self._risk_label = value
    @property
    def risk_score(self):
        return self._risk_score

    @risk_score.setter
    def risk_score(self, value):
        self._risk_score = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataAlibabaSecuritydataQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'identify_result' in response:
            self.identify_result = response['identify_result']
        if 'risk_label' in response:
            self.risk_label = response['risk_label']
        if 'risk_score' in response:
            self.risk_score = response['risk_score']
