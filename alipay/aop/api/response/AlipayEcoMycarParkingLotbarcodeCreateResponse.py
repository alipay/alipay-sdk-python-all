#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingLotbarcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingLotbarcodeCreateResponse, self).__init__()
        self._qrcode_url = None
        self._status = None

    @property
    def qrcode_url(self):
        return self._qrcode_url

    @qrcode_url.setter
    def qrcode_url(self, value):
        self._qrcode_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingLotbarcodeCreateResponse, self).parse_response_content(response_content)
        if 'qrcode_url' in response:
            self.qrcode_url = response['qrcode_url']
        if 'status' in response:
            self.status = response['status']
