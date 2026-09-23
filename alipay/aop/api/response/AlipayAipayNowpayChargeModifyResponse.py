#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayNowpayChargeModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayNowpayChargeModifyResponse, self).__init__()
        self._capability_status = None
        self._changed = None
        self._reason_message = None
        self._status_version = None

    @property
    def capability_status(self):
        return self._capability_status

    @capability_status.setter
    def capability_status(self, value):
        self._capability_status = value
    @property
    def changed(self):
        return self._changed

    @changed.setter
    def changed(self, value):
        self._changed = value
    @property
    def reason_message(self):
        return self._reason_message

    @reason_message.setter
    def reason_message(self, value):
        self._reason_message = value
    @property
    def status_version(self):
        return self._status_version

    @status_version.setter
    def status_version(self, value):
        self._status_version = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayNowpayChargeModifyResponse, self).parse_response_content(response_content)
        if 'capability_status' in response:
            self.capability_status = response['capability_status']
        if 'changed' in response:
            self.changed = response['changed']
        if 'reason_message' in response:
            self.reason_message = response['reason_message']
        if 'status_version' in response:
            self.status_version = response['status_version']
