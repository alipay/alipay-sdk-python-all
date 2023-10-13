#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PassportInfoDTO import PassportInfoDTO


class AnttechOceanbasePassportinfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassportinfoBatchqueryResponse, self).__init__()
        self._passport_infos = None

    @property
    def passport_infos(self):
        return self._passport_infos

    @passport_infos.setter
    def passport_infos(self, value):
        if isinstance(value, list):
            self._passport_infos = list()
            for i in value:
                if isinstance(i, PassportInfoDTO):
                    self._passport_infos.append(i)
                else:
                    self._passport_infos.append(PassportInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassportinfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'passport_infos' in response:
            self.passport_infos = response['passport_infos']
