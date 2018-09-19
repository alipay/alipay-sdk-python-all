#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayYebLqdDataResult import AlipayYebLqdDataResult


class AlipayDataDataserviceYuebaolqdDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceYuebaolqdDetailQueryResponse, self).__init__()
        self._yeb_ldq_data = None

    @property
    def yeb_ldq_data(self):
        return self._yeb_ldq_data

    @yeb_ldq_data.setter
    def yeb_ldq_data(self, value):
        if isinstance(value, list):
            self._yeb_ldq_data = list()
            for i in value:
                if isinstance(i, AlipayYebLqdDataResult):
                    self._yeb_ldq_data.append(i)
                else:
                    self._yeb_ldq_data.append(AlipayYebLqdDataResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceYuebaolqdDetailQueryResponse, self).parse_response_content(response_content)
        if 'yeb_ldq_data' in response:
            self.yeb_ldq_data = response['yeb_ldq_data']
