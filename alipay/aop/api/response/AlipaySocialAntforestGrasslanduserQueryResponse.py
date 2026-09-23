#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestGrasslanduserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestGrasslanduserQueryResponse, self).__init__()
        self._open_status = None
        self._total_grassland_cert_num = None

    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def total_grassland_cert_num(self):
        return self._total_grassland_cert_num

    @total_grassland_cert_num.setter
    def total_grassland_cert_num(self, value):
        self._total_grassland_cert_num = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestGrasslanduserQueryResponse, self).parse_response_content(response_content)
        if 'open_status' in response:
            self.open_status = response['open_status']
        if 'total_grassland_cert_num' in response:
            self.total_grassland_cert_num = response['total_grassland_cert_num']
