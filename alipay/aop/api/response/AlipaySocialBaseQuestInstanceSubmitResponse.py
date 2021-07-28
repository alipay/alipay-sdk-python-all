#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseQuestInstanceSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseQuestInstanceSubmitResponse, self).__init__()
        self._daily_count = None
        self._mark_amount = None
        self._mark_time = None
        self._mark_tip = None

    @property
    def daily_count(self):
        return self._daily_count

    @daily_count.setter
    def daily_count(self, value):
        self._daily_count = value
    @property
    def mark_amount(self):
        return self._mark_amount

    @mark_amount.setter
    def mark_amount(self, value):
        self._mark_amount = value
    @property
    def mark_time(self):
        return self._mark_time

    @mark_time.setter
    def mark_time(self, value):
        self._mark_time = value
    @property
    def mark_tip(self):
        return self._mark_tip

    @mark_tip.setter
    def mark_tip(self, value):
        self._mark_tip = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseQuestInstanceSubmitResponse, self).parse_response_content(response_content)
        if 'daily_count' in response:
            self.daily_count = response['daily_count']
        if 'mark_amount' in response:
            self.mark_amount = response['mark_amount']
        if 'mark_time' in response:
            self.mark_time = response['mark_time']
        if 'mark_tip' in response:
            self.mark_tip = response['mark_tip']
