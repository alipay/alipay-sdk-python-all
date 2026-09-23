#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalItemUpcexistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalItemUpcexistQueryResponse, self).__init__()
        self._upc_list = None

    @property
    def upc_list(self):
        return self._upc_list

    @upc_list.setter
    def upc_list(self, value):
        if isinstance(value, list):
            self._upc_list = list()
            for i in value:
                self._upc_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalItemUpcexistQueryResponse, self).parse_response_content(response_content)
        if 'upc_list' in response:
            self.upc_list = response['upc_list']
