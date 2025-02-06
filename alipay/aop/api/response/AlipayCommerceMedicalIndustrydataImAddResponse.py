#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIndustrydataImAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataImAddResponse, self).__init__()
        self._alipay_chat_id = None

    @property
    def alipay_chat_id(self):
        return self._alipay_chat_id

    @alipay_chat_id.setter
    def alipay_chat_id(self, value):
        self._alipay_chat_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataImAddResponse, self).parse_response_content(response_content)
        if 'alipay_chat_id' in response:
            self.alipay_chat_id = response['alipay_chat_id']
