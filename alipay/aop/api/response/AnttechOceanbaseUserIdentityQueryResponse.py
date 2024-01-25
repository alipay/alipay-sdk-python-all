#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OBCompanyDTO import OBCompanyDTO
from alipay.aop.api.domain.OBPersonalDTO import OBPersonalDTO


class AnttechOceanbaseUserIdentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseUserIdentityQueryResponse, self).__init__()
        self._company = None
        self._personal = None

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        if isinstance(value, OBCompanyDTO):
            self._company = value
        else:
            self._company = OBCompanyDTO.from_alipay_dict(value)
    @property
    def personal(self):
        return self._personal

    @personal.setter
    def personal(self, value):
        if isinstance(value, OBPersonalDTO):
            self._personal = value
        else:
            self._personal = OBPersonalDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseUserIdentityQueryResponse, self).parse_response_content(response_content)
        if 'company' in response:
            self.company = response['company']
        if 'personal' in response:
            self.personal = response['personal']
