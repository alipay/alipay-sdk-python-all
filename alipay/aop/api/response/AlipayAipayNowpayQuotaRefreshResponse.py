#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayNowpayQuotaRefreshResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayNowpayQuotaRefreshResponse, self).__init__()
        self._consume_order_id = None
        self._consume_reason = None
        self._consume_status = None
        self._consumed = None
        self._quota_unit = None
        self._reason_code = None
        self._remaining = None
        self._update_time = None

    @property
    def consume_order_id(self):
        return self._consume_order_id

    @consume_order_id.setter
    def consume_order_id(self, value):
        self._consume_order_id = value
    @property
    def consume_reason(self):
        return self._consume_reason

    @consume_reason.setter
    def consume_reason(self, value):
        self._consume_reason = value
    @property
    def consume_status(self):
        return self._consume_status

    @consume_status.setter
    def consume_status(self, value):
        self._consume_status = value
    @property
    def consumed(self):
        return self._consumed

    @consumed.setter
    def consumed(self, value):
        self._consumed = value
    @property
    def quota_unit(self):
        return self._quota_unit

    @quota_unit.setter
    def quota_unit(self, value):
        self._quota_unit = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def remaining(self):
        return self._remaining

    @remaining.setter
    def remaining(self, value):
        self._remaining = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayNowpayQuotaRefreshResponse, self).parse_response_content(response_content)
        if 'consume_order_id' in response:
            self.consume_order_id = response['consume_order_id']
        if 'consume_reason' in response:
            self.consume_reason = response['consume_reason']
        if 'consume_status' in response:
            self.consume_status = response['consume_status']
        if 'consumed' in response:
            self.consumed = response['consumed']
        if 'quota_unit' in response:
            self.quota_unit = response['quota_unit']
        if 'reason_code' in response:
            self.reason_code = response['reason_code']
        if 'remaining' in response:
            self.remaining = response['remaining']
        if 'update_time' in response:
            self.update_time = response['update_time']
