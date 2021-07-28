#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NetFlowDeviceOfferInfoResponse import NetFlowDeviceOfferInfoResponse


class AlipayCommerceIotNetflowInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotNetflowInfoQueryResponse, self).__init__()
        self._net_flow_device_offer_info_response = None

    @property
    def net_flow_device_offer_info_response(self):
        return self._net_flow_device_offer_info_response

    @net_flow_device_offer_info_response.setter
    def net_flow_device_offer_info_response(self, value):
        if isinstance(value, NetFlowDeviceOfferInfoResponse):
            self._net_flow_device_offer_info_response = value
        else:
            self._net_flow_device_offer_info_response = NetFlowDeviceOfferInfoResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotNetflowInfoQueryResponse, self).parse_response_content(response_content)
        if 'net_flow_device_offer_info_response' in response:
            self.net_flow_device_offer_info_response = response['net_flow_device_offer_info_response']
