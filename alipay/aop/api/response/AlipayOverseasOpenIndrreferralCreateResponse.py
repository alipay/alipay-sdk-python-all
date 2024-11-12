#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndrISVResult import IndrISVResult


class AlipayOverseasOpenIndrreferralCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenIndrreferralCreateResponse, self).__init__()
        self._expired_time = None
        self._jump_link = None
        self._referral_code = None
        self._result = None

    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def jump_link(self):
        return self._jump_link

    @jump_link.setter
    def jump_link(self, value):
        self._jump_link = value
    @property
    def referral_code(self):
        return self._referral_code

    @referral_code.setter
    def referral_code(self, value):
        self._referral_code = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, IndrISVResult):
            self._result = value
        else:
            self._result = IndrISVResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenIndrreferralCreateResponse, self).parse_response_content(response_content)
        if 'expired_time' in response:
            self.expired_time = response['expired_time']
        if 'jump_link' in response:
            self.jump_link = response['jump_link']
        if 'referral_code' in response:
            self.referral_code = response['referral_code']
        if 'result' in response:
            self.result = response['result']
