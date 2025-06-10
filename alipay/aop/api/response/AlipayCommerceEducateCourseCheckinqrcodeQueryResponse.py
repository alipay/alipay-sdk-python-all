#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCourseCheckinqrcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCourseCheckinqrcodeQueryResponse, self).__init__()
        self._automatic_refresh = None
        self._end_time = None
        self._manual_close = None
        self._next_refresh_time = None
        self._qr_code_url = None

    @property
    def automatic_refresh(self):
        return self._automatic_refresh

    @automatic_refresh.setter
    def automatic_refresh(self, value):
        self._automatic_refresh = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def manual_close(self):
        return self._manual_close

    @manual_close.setter
    def manual_close(self, value):
        self._manual_close = value
    @property
    def next_refresh_time(self):
        return self._next_refresh_time

    @next_refresh_time.setter
    def next_refresh_time(self, value):
        self._next_refresh_time = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCourseCheckinqrcodeQueryResponse, self).parse_response_content(response_content)
        if 'automatic_refresh' in response:
            self.automatic_refresh = response['automatic_refresh']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'manual_close' in response:
            self.manual_close = response['manual_close']
        if 'next_refresh_time' in response:
            self.next_refresh_time = response['next_refresh_time']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
