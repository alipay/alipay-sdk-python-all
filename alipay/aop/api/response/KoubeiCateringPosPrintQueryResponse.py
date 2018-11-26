#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrintModel import PrintModel


class KoubeiCateringPosPrintQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosPrintQueryResponse, self).__init__()
        self._print_model_list = None

    @property
    def print_model_list(self):
        return self._print_model_list

    @print_model_list.setter
    def print_model_list(self, value):
        if isinstance(value, list):
            self._print_model_list = list()
            for i in value:
                if isinstance(i, PrintModel):
                    self._print_model_list.append(i)
                else:
                    self._print_model_list.append(PrintModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosPrintQueryResponse, self).parse_response_content(response_content)
        if 'print_model_list' in response:
            self.print_model_list = response['print_model_list']
