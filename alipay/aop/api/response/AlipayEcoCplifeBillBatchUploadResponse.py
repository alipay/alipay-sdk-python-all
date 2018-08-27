#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCplifeBillBatchUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeBillBatchUploadResponse, self).__init__()
        self._batch_id = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeBillBatchUploadResponse, self).parse_response_content(response_content)
        if 'batch_id' in response:
            self.batch_id = response['batch_id']
