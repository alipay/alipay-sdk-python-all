#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarMaintainDataUpdateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarMaintainDataUpdateResponse, self).__init__()
        self._info = None

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarMaintainDataUpdateResponse, self).parse_response_content(response_content)
        if 'info' in response:
            self.info = response['info']
