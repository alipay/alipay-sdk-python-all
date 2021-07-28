#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmpeDeviceTypeInfo import AmpeDeviceTypeInfo


class AlipayOpenMiniAmpeDevicetypeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeDevicetypeBatchqueryResponse, self).__init__()
        self._device_type_list = None

    @property
    def device_type_list(self):
        return self._device_type_list

    @device_type_list.setter
    def device_type_list(self, value):
        if isinstance(value, list):
            self._device_type_list = list()
            for i in value:
                if isinstance(i, AmpeDeviceTypeInfo):
                    self._device_type_list.append(i)
                else:
                    self._device_type_list.append(AmpeDeviceTypeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeDevicetypeBatchqueryResponse, self).parse_response_content(response_content)
        if 'device_type_list' in response:
            self.device_type_list = response['device_type_list']
