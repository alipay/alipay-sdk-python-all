#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCharityRecordexistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCharityRecordexistQueryResponse, self).__init__()
        self._donation_tag = None
        self._donation_times = None

    @property
    def donation_tag(self):
        return self._donation_tag

    @donation_tag.setter
    def donation_tag(self, value):
        self._donation_tag = value
    @property
    def donation_times(self):
        return self._donation_times

    @donation_times.setter
    def donation_times(self, value):
        self._donation_times = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCharityRecordexistQueryResponse, self).parse_response_content(response_content)
        if 'donation_tag' in response:
            self.donation_tag = response['donation_tag']
        if 'donation_times' in response:
            self.donation_times = response['donation_times']
