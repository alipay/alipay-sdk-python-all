#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderCollaborateDeviceUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateDeviceUnbindResponse, self).__init__()
        self._device_sn = None
        self._out_biz_no = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateDeviceUnbindResponse, self).parse_response_content(response_content)
        if 'device_sn' in response:
            self.device_sn = response['device_sn']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
