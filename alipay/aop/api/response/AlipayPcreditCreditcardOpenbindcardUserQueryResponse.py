#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditCreditcardOpenbindcardUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditCreditcardOpenbindcardUserQueryResponse, self).__init__()
        self._admit = None
        self._completed_activity = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def completed_activity(self):
        return self._completed_activity

    @completed_activity.setter
    def completed_activity(self, value):
        self._completed_activity = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditCreditcardOpenbindcardUserQueryResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'completed_activity' in response:
            self.completed_activity = response['completed_activity']
