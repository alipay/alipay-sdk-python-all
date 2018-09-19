#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCdpAdvertiseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCdpAdvertiseQueryResponse, self).__init__()
        self._action_url = None
        self._ad_code = None
        self._ad_rules = None
        self._behavior = None
        self._biz_ext_info = None
        self._content = None
        self._content_type = None
        self._end_time = None
        self._height = None
        self._start_time = None
        self._status = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def ad_code(self):
        return self._ad_code

    @ad_code.setter
    def ad_code(self, value):
        self._ad_code = value
    @property
    def ad_rules(self):
        return self._ad_rules

    @ad_rules.setter
    def ad_rules(self, value):
        self._ad_rules = value
    @property
    def behavior(self):
        return self._behavior

    @behavior.setter
    def behavior(self, value):
        self._behavior = value
    @property
    def biz_ext_info(self):
        return self._biz_ext_info

    @biz_ext_info.setter
    def biz_ext_info(self, value):
        self._biz_ext_info = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
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
        response = super(AlipayMarketingCdpAdvertiseQueryResponse, self).parse_response_content(response_content)
        if 'action_url' in response:
            self.action_url = response['action_url']
        if 'ad_code' in response:
            self.ad_code = response['ad_code']
        if 'ad_rules' in response:
            self.ad_rules = response['ad_rules']
        if 'behavior' in response:
            self.behavior = response['behavior']
        if 'biz_ext_info' in response:
            self.biz_ext_info = response['biz_ext_info']
        if 'content' in response:
            self.content = response['content']
        if 'content_type' in response:
            self.content_type = response['content_type']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'height' in response:
            self.height = response['height']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
