#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheThirteen import RainyComplexTypesTheThirteen


class AlipayDataDataserviceTreeapitwelveRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceTreeapitwelveRainystestQueryResponse, self).__init__()
        self._res_ref = None

    @property
    def res_ref(self):
        return self._res_ref

    @res_ref.setter
    def res_ref(self, value):
        if isinstance(value, RainyComplexTypesTheThirteen):
            self._res_ref = value
        else:
            self._res_ref = RainyComplexTypesTheThirteen.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceTreeapitwelveRainystestQueryResponse, self).parse_response_content(response_content)
        if 'res_ref' in response:
            self.res_ref = response['res_ref']
