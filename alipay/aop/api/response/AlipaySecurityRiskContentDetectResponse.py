#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskContentDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskContentDetectResponse, self).__init__()
        self._action = None
        self._keywords = None
        self._unique_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, list):
            self._keywords = list()
            for i in value:
                self._keywords.append(i)
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskContentDetectResponse, self).parse_response_content(response_content)
        if 'action' in response:
            self.action = response['action']
        if 'keywords' in response:
            self.keywords = response['keywords']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
