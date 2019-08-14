#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserElectronicidOutermerchantbarcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserElectronicidOutermerchantbarcodeCreateResponse, self).__init__()
        self._barcode = None
        self._image_url = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserElectronicidOutermerchantbarcodeCreateResponse, self).parse_response_content(response_content)
        if 'barcode' in response:
            self.barcode = response['barcode']
        if 'image_url' in response:
            self.image_url = response['image_url']
