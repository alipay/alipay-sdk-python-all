#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserElectronicidUserbarcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserElectronicidUserbarcodeCreateResponse, self).__init__()
        self._barcode = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserElectronicidUserbarcodeCreateResponse, self).parse_response_content(response_content)
        if 'barcode' in response:
            self.barcode = response['barcode']
