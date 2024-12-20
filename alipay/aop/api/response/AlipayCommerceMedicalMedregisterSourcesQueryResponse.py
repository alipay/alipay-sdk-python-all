#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SourceVO import SourceVO


class AlipayCommerceMedicalMedregisterSourcesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedregisterSourcesQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, SourceVO):
                    self._data.append(i)
                else:
                    self._data.append(SourceVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedregisterSourcesQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
