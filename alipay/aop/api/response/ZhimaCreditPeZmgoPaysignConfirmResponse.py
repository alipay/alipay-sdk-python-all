#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoPaysignConfirmResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoPaysignConfirmResponse, self).__init__()
        self._agreement_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoPaysignConfirmResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
