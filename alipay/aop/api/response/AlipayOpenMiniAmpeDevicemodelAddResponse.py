#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAmpeDevicemodelAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeDevicemodelAddResponse, self).__init__()
        self._device_model_id = None

    @property
    def device_model_id(self):
        return self._device_model_id

    @device_model_id.setter
    def device_model_id(self, value):
        self._device_model_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeDevicemodelAddResponse, self).parse_response_content(response_content)
        if 'device_model_id' in response:
            self.device_model_id = response['device_model_id']
