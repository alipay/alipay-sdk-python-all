#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndirectAuthOrderFailedReason import IndirectAuthOrderFailedReason


class AlipayMerchantIndirectAuthorderQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectAuthorderQuerystatusResponse, self).__init__()
        self._order_no = None
        self._order_status = None
        self._qr_code = None
        self._verify_list = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def verify_list(self):
        return self._verify_list

    @verify_list.setter
    def verify_list(self, value):
        if isinstance(value, list):
            self._verify_list = list()
            for i in value:
                if isinstance(i, IndirectAuthOrderFailedReason):
                    self._verify_list.append(i)
                else:
                    self._verify_list.append(IndirectAuthOrderFailedReason.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectAuthorderQuerystatusResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
        if 'verify_list' in response:
            self.verify_list = response['verify_list']
