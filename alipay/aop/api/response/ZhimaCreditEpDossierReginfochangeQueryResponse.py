#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpReginfoChangeDataInfo import EpReginfoChangeDataInfo


class ZhimaCreditEpDossierReginfochangeQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierReginfochangeQueryResponse, self).__init__()
        self._data = None
        self._data_found = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, EpReginfoChangeDataInfo):
            self._data = value
        else:
            self._data = EpReginfoChangeDataInfo.from_alipay_dict(value)
    @property
    def data_found(self):
        return self._data_found

    @data_found.setter
    def data_found(self, value):
        self._data_found = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierReginfochangeQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'data_found' in response:
            self.data_found = response['data_found']
