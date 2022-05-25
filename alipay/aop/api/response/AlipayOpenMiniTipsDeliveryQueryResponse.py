#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniTipsDeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTipsDeliveryQueryResponse, self).__init__()
        self._delivery_content = None
        self._delivery_id = None
        self._delivery_name = None
        self._end_time = None
        self._fail_reason = None
        self._match_type = None
        self._match_url = None
        self._start_time = None
        self._status = None

    @property
    def delivery_content(self):
        return self._delivery_content

    @delivery_content.setter
    def delivery_content(self, value):
        self._delivery_content = value
    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def delivery_name(self):
        return self._delivery_name

    @delivery_name.setter
    def delivery_name(self, value):
        self._delivery_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def match_type(self):
        return self._match_type

    @match_type.setter
    def match_type(self, value):
        self._match_type = value
    @property
    def match_url(self):
        return self._match_url

    @match_url.setter
    def match_url(self, value):
        self._match_url = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTipsDeliveryQueryResponse, self).parse_response_content(response_content)
        if 'delivery_content' in response:
            self.delivery_content = response['delivery_content']
        if 'delivery_id' in response:
            self.delivery_id = response['delivery_id']
        if 'delivery_name' in response:
            self.delivery_name = response['delivery_name']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'match_type' in response:
            self.match_type = response['match_type']
        if 'match_url' in response:
            self.match_url = response['match_url']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
