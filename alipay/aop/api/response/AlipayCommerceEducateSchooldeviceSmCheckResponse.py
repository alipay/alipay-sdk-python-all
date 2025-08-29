#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSchooldeviceSmCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSchooldeviceSmCheckResponse, self).__init__()
        self._sm_cn_name = None
        self._sm_mcc_name = None
        self._sm_new_mcc_ame = None

    @property
    def sm_cn_name(self):
        return self._sm_cn_name

    @sm_cn_name.setter
    def sm_cn_name(self, value):
        self._sm_cn_name = value
    @property
    def sm_mcc_name(self):
        return self._sm_mcc_name

    @sm_mcc_name.setter
    def sm_mcc_name(self, value):
        self._sm_mcc_name = value
    @property
    def sm_new_mcc_ame(self):
        return self._sm_new_mcc_ame

    @sm_new_mcc_ame.setter
    def sm_new_mcc_ame(self, value):
        self._sm_new_mcc_ame = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSchooldeviceSmCheckResponse, self).parse_response_content(response_content)
        if 'sm_cn_name' in response:
            self.sm_cn_name = response['sm_cn_name']
        if 'sm_mcc_name' in response:
            self.sm_mcc_name = response['sm_mcc_name']
        if 'sm_new_mcc_ame' in response:
            self.sm_new_mcc_ame = response['sm_new_mcc_ame']
