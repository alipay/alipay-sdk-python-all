#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserSportsplayGobillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSportsplayGobillQueryResponse, self).__init__()
        self._biz_time = None
        self._complete = None
        self._forward_step_count = None
        self._go_bill_id = None
        self._go_step_count = None
        self._path_id = None
        self._path_name = None
        self._path_record_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def complete(self):
        return self._complete

    @complete.setter
    def complete(self, value):
        self._complete = value
    @property
    def forward_step_count(self):
        return self._forward_step_count

    @forward_step_count.setter
    def forward_step_count(self, value):
        self._forward_step_count = value
    @property
    def go_bill_id(self):
        return self._go_bill_id

    @go_bill_id.setter
    def go_bill_id(self, value):
        self._go_bill_id = value
    @property
    def go_step_count(self):
        return self._go_step_count

    @go_step_count.setter
    def go_step_count(self, value):
        self._go_step_count = value
    @property
    def path_id(self):
        return self._path_id

    @path_id.setter
    def path_id(self, value):
        self._path_id = value
    @property
    def path_name(self):
        return self._path_name

    @path_name.setter
    def path_name(self, value):
        self._path_name = value
    @property
    def path_record_id(self):
        return self._path_record_id

    @path_record_id.setter
    def path_record_id(self, value):
        self._path_record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserSportsplayGobillQueryResponse, self).parse_response_content(response_content)
        if 'biz_time' in response:
            self.biz_time = response['biz_time']
        if 'complete' in response:
            self.complete = response['complete']
        if 'forward_step_count' in response:
            self.forward_step_count = response['forward_step_count']
        if 'go_bill_id' in response:
            self.go_bill_id = response['go_bill_id']
        if 'go_step_count' in response:
            self.go_step_count = response['go_step_count']
        if 'path_id' in response:
            self.path_id = response['path_id']
        if 'path_name' in response:
            self.path_name = response['path_name']
        if 'path_record_id' in response:
            self.path_record_id = response['path_record_id']
