#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmServicerecordCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmServicerecordCreateResponse, self).__init__()
        self._service_record_id = None

    @property
    def service_record_id(self):
        return self._service_record_id

    @service_record_id.setter
    def service_record_id(self, value):
        self._service_record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmServicerecordCreateResponse, self).parse_response_content(response_content)
        if 'service_record_id' in response:
            self.service_record_id = response['service_record_id']
