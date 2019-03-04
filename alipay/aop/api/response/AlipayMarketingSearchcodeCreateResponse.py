#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingSearchcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingSearchcodeCreateResponse, self).__init__()
        self._end_content = None
        self._keywords = None
        self._pre_content = None
        self._search_code = None

    @property
    def end_content(self):
        return self._end_content

    @end_content.setter
    def end_content(self, value):
        self._end_content = value
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        self._keywords = value
    @property
    def pre_content(self):
        return self._pre_content

    @pre_content.setter
    def pre_content(self, value):
        self._pre_content = value
    @property
    def search_code(self):
        return self._search_code

    @search_code.setter
    def search_code(self, value):
        self._search_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingSearchcodeCreateResponse, self).parse_response_content(response_content)
        if 'end_content' in response:
            self.end_content = response['end_content']
        if 'keywords' in response:
            self.keywords = response['keywords']
        if 'pre_content' in response:
            self.pre_content = response['pre_content']
        if 'search_code' in response:
            self.search_code = response['search_code']
