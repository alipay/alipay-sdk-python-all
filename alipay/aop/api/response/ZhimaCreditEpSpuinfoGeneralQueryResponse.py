#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpSpuGeneralInfoResult import EpSpuGeneralInfoResult


class ZhimaCreditEpSpuinfoGeneralQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpSpuinfoGeneralQueryResponse, self).__init__()
        self._company_key = None
        self._data = None

    @property
    def company_key(self):
        return self._company_key

    @company_key.setter
    def company_key(self, value):
        self._company_key = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, EpSpuGeneralInfoResult):
            self._data = value
        else:
            self._data = EpSpuGeneralInfoResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpSpuinfoGeneralQueryResponse, self).parse_response_content(response_content)
        if 'company_key' in response:
            self.company_key = response['company_key']
        if 'data' in response:
            self.data = response['data']
