#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceItaskProcessDetailSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceItaskProcessDetailSyncResponse, self).__init__()
        self._alipay_process_id = None

    @property
    def alipay_process_id(self):
        return self._alipay_process_id

    @alipay_process_id.setter
    def alipay_process_id(self, value):
        self._alipay_process_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceItaskProcessDetailSyncResponse, self).parse_response_content(response_content)
        if 'alipay_process_id' in response:
            self.alipay_process_id = response['alipay_process_id']
