#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EbikeChargeQrCodeResult import EbikeChargeQrCodeResult


class AlipayCommerceTransportIndustryQrcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIndustryQrcodeCreateResponse, self).__init__()
        self._qr_code_result_list = None

    @property
    def qr_code_result_list(self):
        return self._qr_code_result_list

    @qr_code_result_list.setter
    def qr_code_result_list(self, value):
        if isinstance(value, list):
            self._qr_code_result_list = list()
            for i in value:
                if isinstance(i, EbikeChargeQrCodeResult):
                    self._qr_code_result_list.append(i)
                else:
                    self._qr_code_result_list.append(EbikeChargeQrCodeResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIndustryQrcodeCreateResponse, self).parse_response_content(response_content)
        if 'qr_code_result_list' in response:
            self.qr_code_result_list = response['qr_code_result_list']
