#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StreamMessage import StreamMessage


class AlipayCommerceMedicalLargermodelSseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelSseQueryResponse, self).__init__()
        self._data = None
        self._succes = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, StreamMessage):
            self._data = value
        else:
            self._data = StreamMessage.from_alipay_dict(value)
    @property
    def succes(self):
        return self._succes

    @succes.setter
    def succes(self, value):
        self._succes = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalLargermodelSseQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'succes' in response:
            self.succes = response['succes']
