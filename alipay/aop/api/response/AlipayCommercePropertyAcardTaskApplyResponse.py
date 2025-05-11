#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePropertyAcardTaskApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyAcardTaskApplyResponse, self).__init__()
        self._card_no = None
        self._task_id = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyAcardTaskApplyResponse, self).parse_response_content(response_content)
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'task_id' in response:
            self.task_id = response['task_id']
