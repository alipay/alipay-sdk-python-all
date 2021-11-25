#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityDisplayInfo import ActivityDisplayInfo
from alipay.aop.api.domain.ActivitySendRule import ActivitySendRule
from alipay.aop.api.domain.ActivityUseRule import ActivityUseRule


class AlipayMarketingActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityQueryResponse, self).__init__()
        self._activity_display_info = None
        self._activity_id = None
        self._activity_name = None
        self._activity_send_rule = None
        self._activity_status = None
        self._activity_use_rule = None
        self._belong_merchant_id = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._voucher_type = None

    @property
    def activity_display_info(self):
        return self._activity_display_info

    @activity_display_info.setter
    def activity_display_info(self, value):
        if isinstance(value, ActivityDisplayInfo):
            self._activity_display_info = value
        else:
            self._activity_display_info = ActivityDisplayInfo.from_alipay_dict(value)
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_send_rule(self):
        return self._activity_send_rule

    @activity_send_rule.setter
    def activity_send_rule(self, value):
        if isinstance(value, ActivitySendRule):
            self._activity_send_rule = value
        else:
            self._activity_send_rule = ActivitySendRule.from_alipay_dict(value)
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def activity_use_rule(self):
        return self._activity_use_rule

    @activity_use_rule.setter
    def activity_use_rule(self, value):
        if isinstance(value, ActivityUseRule):
            self._activity_use_rule = value
        else:
            self._activity_use_rule = ActivityUseRule.from_alipay_dict(value)
    @property
    def belong_merchant_id(self):
        return self._belong_merchant_id

    @belong_merchant_id.setter
    def belong_merchant_id(self, value):
        self._belong_merchant_id = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityQueryResponse, self).parse_response_content(response_content)
        if 'activity_display_info' in response:
            self.activity_display_info = response['activity_display_info']
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'activity_send_rule' in response:
            self.activity_send_rule = response['activity_send_rule']
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'activity_use_rule' in response:
            self.activity_use_rule = response['activity_use_rule']
        if 'belong_merchant_id' in response:
            self.belong_merchant_id = response['belong_merchant_id']
        if 'publish_end_time' in response:
            self.publish_end_time = response['publish_end_time']
        if 'publish_start_time' in response:
            self.publish_start_time = response['publish_start_time']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
