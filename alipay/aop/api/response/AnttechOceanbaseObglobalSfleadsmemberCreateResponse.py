#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SaleForceLeadsMemberCreateDTO import SaleForceLeadsMemberCreateDTO


class AnttechOceanbaseObglobalSfleadsmemberCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalSfleadsmemberCreateResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, SaleForceLeadsMemberCreateDTO):
            self._result = value
        else:
            self._result = SaleForceLeadsMemberCreateDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalSfleadsmemberCreateResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
