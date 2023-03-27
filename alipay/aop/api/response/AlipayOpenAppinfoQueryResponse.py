#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppinfoQueryResponse, self).__init__()
        self._open_id_config = None

    @property
    def open_id_config(self):
        return self._open_id_config

    @open_id_config.setter
    def open_id_config(self, value):
        self._open_id_config = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppinfoQueryResponse, self).parse_response_content(response_content)
        if 'open_id_config' in response:
            self.open_id_config = response['open_id_config']
