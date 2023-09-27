#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseAntifloodBarrierGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseAntifloodBarrierGetResponse, self).__init__()
        self._ban_duration = None
        self._gmt_create = None
        self._gmt_modified = None
        self._request_limit = None
        self._time_window = None

    @property
    def ban_duration(self):
        return self._ban_duration

    @ban_duration.setter
    def ban_duration(self, value):
        self._ban_duration = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def request_limit(self):
        return self._request_limit

    @request_limit.setter
    def request_limit(self, value):
        self._request_limit = value
    @property
    def time_window(self):
        return self._time_window

    @time_window.setter
    def time_window(self, value):
        self._time_window = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseAntifloodBarrierGetResponse, self).parse_response_content(response_content)
        if 'ban_duration' in response:
            self.ban_duration = response['ban_duration']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'request_limit' in response:
            self.request_limit = response['request_limit']
        if 'time_window' in response:
            self.time_window = response['time_window']
