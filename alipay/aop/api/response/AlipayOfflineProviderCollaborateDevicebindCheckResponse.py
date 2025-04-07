#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderCollaborateDevicebindCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateDevicebindCheckResponse, self).__init__()
        self._device_remark = None
        self._in_white_list = None
        self._legal_person_is_allow_sign = None

    @property
    def device_remark(self):
        return self._device_remark

    @device_remark.setter
    def device_remark(self, value):
        self._device_remark = value
    @property
    def in_white_list(self):
        return self._in_white_list

    @in_white_list.setter
    def in_white_list(self, value):
        self._in_white_list = value
    @property
    def legal_person_is_allow_sign(self):
        return self._legal_person_is_allow_sign

    @legal_person_is_allow_sign.setter
    def legal_person_is_allow_sign(self, value):
        self._legal_person_is_allow_sign = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateDevicebindCheckResponse, self).parse_response_content(response_content)
        if 'device_remark' in response:
            self.device_remark = response['device_remark']
        if 'in_white_list' in response:
            self.in_white_list = response['in_white_list']
        if 'legal_person_is_allow_sign' in response:
            self.legal_person_is_allow_sign = response['legal_person_is_allow_sign']
