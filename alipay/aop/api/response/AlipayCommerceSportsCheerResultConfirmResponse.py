#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceSportsCheerResultConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsCheerResultConfirmResponse, self).__init__()
        self._game_serial_number = None

    @property
    def game_serial_number(self):
        return self._game_serial_number

    @game_serial_number.setter
    def game_serial_number(self, value):
        self._game_serial_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsCheerResultConfirmResponse, self).parse_response_content(response_content)
        if 'game_serial_number' in response:
            self.game_serial_number = response['game_serial_number']
