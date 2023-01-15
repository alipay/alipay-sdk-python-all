#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportChargerChargerbindinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerChargerbindinfoSyncResponse, self).__init__()
        self._equip_id = None
        self._fail_reason = None
        self._result_status = None

    @property
    def equip_id(self):
        return self._equip_id

    @equip_id.setter
    def equip_id(self, value):
        self._equip_id = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerChargerbindinfoSyncResponse, self).parse_response_content(response_content)
        if 'equip_id' in response:
            self.equip_id = response['equip_id']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'result_status' in response:
            self.result_status = response['result_status']
