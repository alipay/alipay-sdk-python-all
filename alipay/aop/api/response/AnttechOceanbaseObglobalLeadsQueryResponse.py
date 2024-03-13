#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LeadsDTO import LeadsDTO


class AnttechOceanbaseObglobalLeadsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalLeadsQueryResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, LeadsDTO):
            self._result = value
        else:
            self._result = LeadsDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalLeadsQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
