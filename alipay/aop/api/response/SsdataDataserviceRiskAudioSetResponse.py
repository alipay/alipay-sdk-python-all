#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskAudioSetResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskAudioSetResponse, self).__init__()
        self._count = None
        self._keyword_list = None
        self._success = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def keyword_list(self):
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, value):
        if isinstance(value, list):
            self._keyword_list = list()
            for i in value:
                self._keyword_list.append(i)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskAudioSetResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'keyword_list' in response:
            self.keyword_list = response['keyword_list']
        if 'success' in response:
            self.success = response['success']
