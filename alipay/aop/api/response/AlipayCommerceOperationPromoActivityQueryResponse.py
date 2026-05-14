#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NfcDeviceActivityInfo import NfcDeviceActivityInfo


class AlipayCommerceOperationPromoActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoActivityQueryResponse, self).__init__()
        self._device_act_info_list = None
        self._out_merchant_no = None

    @property
    def device_act_info_list(self):
        return self._device_act_info_list

    @device_act_info_list.setter
    def device_act_info_list(self, value):
        if isinstance(value, list):
            self._device_act_info_list = list()
            for i in value:
                if isinstance(i, NfcDeviceActivityInfo):
                    self._device_act_info_list.append(i)
                else:
                    self._device_act_info_list.append(NfcDeviceActivityInfo.from_alipay_dict(i))
    @property
    def out_merchant_no(self):
        return self._out_merchant_no

    @out_merchant_no.setter
    def out_merchant_no(self, value):
        self._out_merchant_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoActivityQueryResponse, self).parse_response_content(response_content)
        if 'device_act_info_list' in response:
            self.device_act_info_list = response['device_act_info_list']
        if 'out_merchant_no' in response:
            self.out_merchant_no = response['out_merchant_no']
