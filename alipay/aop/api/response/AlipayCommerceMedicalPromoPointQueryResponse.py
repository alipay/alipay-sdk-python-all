#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalPromoPointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPromoPointQueryResponse, self).__init__()
        self._num = None

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPromoPointQueryResponse, self).parse_response_content(response_content)
        if 'num' in response:
            self.num = response['num']
