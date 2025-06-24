#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalRegisterCancelorderNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterCancelorderNotifyResponse, self).__init__()
        self._cancel_msg = None

    @property
    def cancel_msg(self):
        return self._cancel_msg

    @cancel_msg.setter
    def cancel_msg(self, value):
        self._cancel_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterCancelorderNotifyResponse, self).parse_response_content(response_content)
        if 'cancel_msg' in response:
            self.cancel_msg = response['cancel_msg']
