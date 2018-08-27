#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QRcode import QRcode


class AlipayEcoMycarParkingCardbarcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingCardbarcodeCreateResponse, self).__init__()
        self._qrcodes = None

    @property
    def qrcodes(self):
        return self._qrcodes

    @qrcodes.setter
    def qrcodes(self, value):
        if isinstance(value, list):
            self._qrcodes = list()
            for i in value:
                if isinstance(i, QRcode):
                    self._qrcodes.append(i)
                else:
                    self._qrcodes.append(QRcode.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingCardbarcodeCreateResponse, self).parse_response_content(response_content)
        if 'qrcodes' in response:
            self.qrcodes = response['qrcodes']
