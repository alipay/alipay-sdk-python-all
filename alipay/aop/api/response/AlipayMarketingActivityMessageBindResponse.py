#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingActivityMessageBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityMessageBindResponse, self).__init__()
        self._activity_id = None
        self._merchant_id = None
        self._notify_appid = None
        self._update_time = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def notify_appid(self):
        return self._notify_appid

    @notify_appid.setter
    def notify_appid(self, value):
        self._notify_appid = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityMessageBindResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'notify_appid' in response:
            self.notify_appid = response['notify_appid']
        if 'update_time' in response:
            self.update_time = response['update_time']
