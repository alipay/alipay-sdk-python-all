#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoCarSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoCarSaveResponse, self).__init__()
        self._car_no = None

    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoCarSaveResponse, self).parse_response_content(response_content)
        if 'car_no' in response:
            self.car_no = response['car_no']
