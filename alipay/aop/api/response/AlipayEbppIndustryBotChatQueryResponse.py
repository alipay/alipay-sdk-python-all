#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BotChatLog import BotChatLog


class AlipayEbppIndustryBotChatQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryBotChatQueryResponse, self).__init__()
        self._answer_list = None
        self._current_page = None
        self._has_next = None
        self._total = None

    @property
    def answer_list(self):
        return self._answer_list

    @answer_list.setter
    def answer_list(self, value):
        if isinstance(value, list):
            self._answer_list = list()
            for i in value:
                if isinstance(i, BotChatLog):
                    self._answer_list.append(i)
                else:
                    self._answer_list.append(BotChatLog.from_alipay_dict(i))
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryBotChatQueryResponse, self).parse_response_content(response_content)
        if 'answer_list' in response:
            self.answer_list = response['answer_list']
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'total' in response:
            self.total = response['total']
