#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceInfo import DeviceInfo


class KoubeiMerchantKbdeviceDevicesBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantKbdeviceDevicesBatchqueryResponse, self).__init__()
        self._device_info_list = None

    @property
    def device_info_list(self):
        return self._device_info_list

    @device_info_list.setter
    def device_info_list(self, value):
        if isinstance(value, list):
            self._device_info_list = list()
            for i in value:
                if isinstance(i, DeviceInfo):
                    self._device_info_list.append(i)
                else:
                    self._device_info_list.append(DeviceInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantKbdeviceDevicesBatchqueryResponse, self).parse_response_content(response_content)
        if 'device_info_list' in response:
            self.device_info_list = response['device_info_list']
