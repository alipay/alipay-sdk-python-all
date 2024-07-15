#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneChannelsaleVoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneChannelsaleVoucherQueryResponse, self).__init__()
        self._effect_end_time = None
        self._effect_start_time = None
        self._policy_no = None
        self._status = None
        self._voucher_url = None

    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voucher_url(self):
        return self._voucher_url

    @voucher_url.setter
    def voucher_url(self, value):
        self._voucher_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneChannelsaleVoucherQueryResponse, self).parse_response_content(response_content)
        if 'effect_end_time' in response:
            self.effect_end_time = response['effect_end_time']
        if 'effect_start_time' in response:
            self.effect_start_time = response['effect_start_time']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'status' in response:
            self.status = response['status']
        if 'voucher_url' in response:
            self.voucher_url = response['voucher_url']
