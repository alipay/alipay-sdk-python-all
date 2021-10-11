#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIotdeviceMaintenanceModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIotdeviceMaintenanceModifyResponse, self).__init__()
        self._biz_order_id = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIotdeviceMaintenanceModifyResponse, self).parse_response_content(response_content)
        if 'biz_order_id' in response:
            self.biz_order_id = response['biz_order_id']
