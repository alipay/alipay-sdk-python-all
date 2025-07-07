#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMedmsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedmsgSendResponse, self).__init__()
        self._msg_id = None
        self._template_code = None

    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedmsgSendResponse, self).parse_response_content(response_content)
        if 'msg_id' in response:
            self.msg_id = response['msg_id']
        if 'template_code' in response:
            self.template_code = response['template_code']
