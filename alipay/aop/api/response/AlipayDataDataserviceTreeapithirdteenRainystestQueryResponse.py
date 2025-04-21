#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheThirteen import RainyComplexTypesTheThirteen


class AlipayDataDataserviceTreeapithirdteenRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceTreeapithirdteenRainystestQueryResponse, self).__init__()
        self._res_strong_ref = None

    @property
    def res_strong_ref(self):
        return self._res_strong_ref

    @res_strong_ref.setter
    def res_strong_ref(self, value):
        if isinstance(value, RainyComplexTypesTheThirteen):
            self._res_strong_ref = value
        else:
            self._res_strong_ref = RainyComplexTypesTheThirteen.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceTreeapithirdteenRainystestQueryResponse, self).parse_response_content(response_content)
        if 'res_strong_ref' in response:
            self.res_strong_ref = response['res_strong_ref']
