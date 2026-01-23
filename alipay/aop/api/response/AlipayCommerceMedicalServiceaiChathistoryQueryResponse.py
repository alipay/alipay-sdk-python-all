#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LlmChatHistoryVO import LlmChatHistoryVO


class AlipayCommerceMedicalServiceaiChathistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServiceaiChathistoryQueryResponse, self).__init__()
        self._content_list = None
        self._has_next = None
        self._latest_time = None
        self._page_size = None

    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                if isinstance(i, LlmChatHistoryVO):
                    self._content_list.append(i)
                else:
                    self._content_list.append(LlmChatHistoryVO.from_alipay_dict(i))
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def latest_time(self):
        return self._latest_time

    @latest_time.setter
    def latest_time(self, value):
        self._latest_time = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServiceaiChathistoryQueryResponse, self).parse_response_content(response_content)
        if 'content_list' in response:
            self.content_list = response['content_list']
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'latest_time' in response:
            self.latest_time = response['latest_time']
        if 'page_size' in response:
            self.page_size = response['page_size']
