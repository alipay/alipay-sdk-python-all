#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySecurityKnowledgeCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySecurityKnowledgeCheckResponse, self).__init__()
        self._no_passed_link_index_list = None
        self._no_passed_pic_url_index_list = None
        self._no_passed_text_index_list = None
        self._safe = None

    @property
    def no_passed_link_index_list(self):
        return self._no_passed_link_index_list

    @no_passed_link_index_list.setter
    def no_passed_link_index_list(self, value):
        if isinstance(value, list):
            self._no_passed_link_index_list = list()
            for i in value:
                self._no_passed_link_index_list.append(i)
    @property
    def no_passed_pic_url_index_list(self):
        return self._no_passed_pic_url_index_list

    @no_passed_pic_url_index_list.setter
    def no_passed_pic_url_index_list(self, value):
        if isinstance(value, list):
            self._no_passed_pic_url_index_list = list()
            for i in value:
                self._no_passed_pic_url_index_list.append(i)
    @property
    def no_passed_text_index_list(self):
        return self._no_passed_text_index_list

    @no_passed_text_index_list.setter
    def no_passed_text_index_list(self, value):
        if isinstance(value, list):
            self._no_passed_text_index_list = list()
            for i in value:
                self._no_passed_text_index_list.append(i)
    @property
    def safe(self):
        return self._safe

    @safe.setter
    def safe(self, value):
        self._safe = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySecurityKnowledgeCheckResponse, self).parse_response_content(response_content)
        if 'no_passed_link_index_list' in response:
            self.no_passed_link_index_list = response['no_passed_link_index_list']
        if 'no_passed_pic_url_index_list' in response:
            self.no_passed_pic_url_index_list = response['no_passed_pic_url_index_list']
        if 'no_passed_text_index_list' in response:
            self.no_passed_text_index_list = response['no_passed_text_index_list']
        if 'safe' in response:
            self.safe = response['safe']
