#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TipIotDeepeyeSnackRecognizePageResVo import TipIotDeepeyeSnackRecognizePageResVo


class AlipayMsaasMediarecogAivisionrecgAiuseinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAivisionrecgAiuseinfoQueryResponse, self).__init__()
        self._current = None
        self._data_list = None
        self._size = None
        self._total = None

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, TipIotDeepeyeSnackRecognizePageResVo):
                    self._data_list.append(i)
                else:
                    self._data_list.append(TipIotDeepeyeSnackRecognizePageResVo.from_alipay_dict(i))
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAivisionrecgAiuseinfoQueryResponse, self).parse_response_content(response_content)
        if 'current' in response:
            self.current = response['current']
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'size' in response:
            self.size = response['size']
        if 'total' in response:
            self.total = response['total']
