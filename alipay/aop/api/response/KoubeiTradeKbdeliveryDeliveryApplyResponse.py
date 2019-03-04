#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LogisticsExternalInfo import LogisticsExternalInfo


class KoubeiTradeKbdeliveryDeliveryApplyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeKbdeliveryDeliveryApplyResponse, self).__init__()
        self._attach = None
        self._gmt_create = None
        self._logistics_external_info = None
        self._logistics_order_no = None

    @property
    def attach(self):
        return self._attach

    @attach.setter
    def attach(self, value):
        self._attach = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def logistics_external_info(self):
        return self._logistics_external_info

    @logistics_external_info.setter
    def logistics_external_info(self, value):
        if isinstance(value, LogisticsExternalInfo):
            self._logistics_external_info = value
        else:
            self._logistics_external_info = LogisticsExternalInfo.from_alipay_dict(value)
    @property
    def logistics_order_no(self):
        return self._logistics_order_no

    @logistics_order_no.setter
    def logistics_order_no(self, value):
        self._logistics_order_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeKbdeliveryDeliveryApplyResponse, self).parse_response_content(response_content)
        if 'attach' in response:
            self.attach = response['attach']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'logistics_external_info' in response:
            self.logistics_external_info = response['logistics_external_info']
        if 'logistics_order_no' in response:
            self.logistics_order_no = response['logistics_order_no']
