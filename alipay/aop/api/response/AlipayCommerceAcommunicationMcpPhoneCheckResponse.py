#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MobileInfo import MobileInfo


class AlipayCommerceAcommunicationMcpPhoneCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationMcpPhoneCheckResponse, self).__init__()
        self._alipay_user_id = None
        self._mobile_info = None
        self._open_id = None
        self._part_mobile_name = None
        self._verify_type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def mobile_info(self):
        return self._mobile_info

    @mobile_info.setter
    def mobile_info(self, value):
        if isinstance(value, MobileInfo):
            self._mobile_info = value
        else:
            self._mobile_info = MobileInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def part_mobile_name(self):
        return self._part_mobile_name

    @part_mobile_name.setter
    def part_mobile_name(self, value):
        self._part_mobile_name = value
    @property
    def verify_type(self):
        return self._verify_type

    @verify_type.setter
    def verify_type(self, value):
        self._verify_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationMcpPhoneCheckResponse, self).parse_response_content(response_content)
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'mobile_info' in response:
            self.mobile_info = response['mobile_info']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'part_mobile_name' in response:
            self.part_mobile_name = response['part_mobile_name']
        if 'verify_type' in response:
            self.verify_type = response['verify_type']
