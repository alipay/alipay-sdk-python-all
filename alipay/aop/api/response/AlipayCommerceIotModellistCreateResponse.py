#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotModellistCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotModellistCreateResponse, self).__init__()
        self._duplicated_model_ids = None

    @property
    def duplicated_model_ids(self):
        return self._duplicated_model_ids

    @duplicated_model_ids.setter
    def duplicated_model_ids(self, value):
        if isinstance(value, list):
            self._duplicated_model_ids = list()
            for i in value:
                self._duplicated_model_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotModellistCreateResponse, self).parse_response_content(response_content)
        if 'duplicated_model_ids' in response:
            self.duplicated_model_ids = response['duplicated_model_ids']
