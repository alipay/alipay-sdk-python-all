#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SpiResult import SpiResult


class AlipayIserviceCcmServiceInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmServiceInitializeResponse, self).__init__()
        self._spi_ids = None

    @property
    def spi_ids(self):
        return self._spi_ids

    @spi_ids.setter
    def spi_ids(self, value):
        if isinstance(value, list):
            self._spi_ids = list()
            for i in value:
                if isinstance(i, SpiResult):
                    self._spi_ids.append(i)
                else:
                    self._spi_ids.append(SpiResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmServiceInitializeResponse, self).parse_response_content(response_content)
        if 'spi_ids' in response:
            self.spi_ids = response['spi_ids']
