#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetVoucherprodChargeSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetVoucherprodChargeSendResponse, self).__init__()
        self._asset_instance_id = None
        self._order_no = None

    @property
    def asset_instance_id(self):
        return self._asset_instance_id

    @asset_instance_id.setter
    def asset_instance_id(self, value):
        self._asset_instance_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetVoucherprodChargeSendResponse, self).parse_response_content(response_content)
        if 'asset_instance_id' in response:
            self.asset_instance_id = response['asset_instance_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
