#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceContent import DeviceContent


class AlipayMarketingShowwindowContentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingShowwindowContentQueryResponse, self).__init__()
        self._device_content_list = None

    @property
    def device_content_list(self):
        return self._device_content_list

    @device_content_list.setter
    def device_content_list(self, value):
        if isinstance(value, list):
            self._device_content_list = list()
            for i in value:
                if isinstance(i, DeviceContent):
                    self._device_content_list.append(i)
                else:
                    self._device_content_list.append(DeviceContent.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingShowwindowContentQueryResponse, self).parse_response_content(response_content)
        if 'device_content_list' in response:
            self.device_content_list = response['device_content_list']
