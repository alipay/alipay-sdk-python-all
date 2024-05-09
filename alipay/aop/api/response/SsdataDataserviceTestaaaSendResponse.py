#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DumTestFFAA import DumTestFFAA


class SsdataDataserviceTestaaaSendResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceTestaaaSendResponse, self).__init__()
        self._return_a = None

    @property
    def return_a(self):
        return self._return_a

    @return_a.setter
    def return_a(self, value):
        if isinstance(value, DumTestFFAA):
            self._return_a = value
        else:
            self._return_a = DumTestFFAA.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceTestaaaSendResponse, self).parse_response_content(response_content)
        if 'return_a' in response:
            self.return_a = response['return_a']
