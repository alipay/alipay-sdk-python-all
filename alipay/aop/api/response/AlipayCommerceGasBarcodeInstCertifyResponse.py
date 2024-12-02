#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceGasBarcodeInstCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceGasBarcodeInstCertifyResponse, self).__init__()
        self._barcode = None
        self._member_no = None
        self._sn = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def member_no(self):
        return self._member_no

    @member_no.setter
    def member_no(self, value):
        self._member_no = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceGasBarcodeInstCertifyResponse, self).parse_response_content(response_content)
        if 'barcode' in response:
            self.barcode = response['barcode']
        if 'member_no' in response:
            self.member_no = response['member_no']
        if 'sn' in response:
            self.sn = response['sn']
