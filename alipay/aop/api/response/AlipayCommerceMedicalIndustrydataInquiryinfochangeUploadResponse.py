#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIndustrydataInquiryinfochangeUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataInquiryinfochangeUploadResponse, self).__init__()
        self._order_status = None

    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataInquiryinfochangeUploadResponse, self).parse_response_content(response_content)
        if 'order_status' in response:
            self.order_status = response['order_status']
