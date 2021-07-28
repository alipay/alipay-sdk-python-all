#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestAccountTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestAccountTransferResponse, self).__init__()
        self._biz_time = None
        self._current_energy = None
        self._transfer_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def current_energy(self):
        return self._current_energy

    @current_energy.setter
    def current_energy(self, value):
        self._current_energy = value
    @property
    def transfer_id(self):
        return self._transfer_id

    @transfer_id.setter
    def transfer_id(self, value):
        self._transfer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestAccountTransferResponse, self).parse_response_content(response_content)
        if 'biz_time' in response:
            self.biz_time = response['biz_time']
        if 'current_energy' in response:
            self.current_energy = response['current_energy']
        if 'transfer_id' in response:
            self.transfer_id = response['transfer_id']
