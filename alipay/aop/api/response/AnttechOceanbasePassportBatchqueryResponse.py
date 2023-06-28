#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PassportDetailDTO import PassportDetailDTO


class AnttechOceanbasePassportBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassportBatchqueryResponse, self).__init__()
        self._passport_details = None

    @property
    def passport_details(self):
        return self._passport_details

    @passport_details.setter
    def passport_details(self, value):
        if isinstance(value, list):
            self._passport_details = list()
            for i in value:
                if isinstance(i, PassportDetailDTO):
                    self._passport_details.append(i)
                else:
                    self._passport_details.append(PassportDetailDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassportBatchqueryResponse, self).parse_response_content(response_content)
        if 'passport_details' in response:
            self.passport_details = response['passport_details']
