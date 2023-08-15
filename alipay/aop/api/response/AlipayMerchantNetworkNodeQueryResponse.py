#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantNetworkNodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantNetworkNodeQueryResponse, self).__init__()
        self._biz_info = None
        self._merchant_node_id = None
        self._merchant_node_name = None
        self._node_biz_type = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def merchant_node_id(self):
        return self._merchant_node_id

    @merchant_node_id.setter
    def merchant_node_id(self, value):
        self._merchant_node_id = value
    @property
    def merchant_node_name(self):
        return self._merchant_node_name

    @merchant_node_name.setter
    def merchant_node_name(self, value):
        self._merchant_node_name = value
    @property
    def node_biz_type(self):
        return self._node_biz_type

    @node_biz_type.setter
    def node_biz_type(self, value):
        self._node_biz_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantNetworkNodeQueryResponse, self).parse_response_content(response_content)
        if 'biz_info' in response:
            self.biz_info = response['biz_info']
        if 'merchant_node_id' in response:
            self.merchant_node_id = response['merchant_node_id']
        if 'merchant_node_name' in response:
            self.merchant_node_name = response['merchant_node_name']
        if 'node_biz_type' in response:
            self.node_biz_type = response['node_biz_type']
