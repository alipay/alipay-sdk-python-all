#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NotaryResultDTO import NotaryResultDTO


class AlipayBossProdAntlegalchainNotaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlegalchainNotaryQueryResponse, self).__init__()
        self._notaries = None

    @property
    def notaries(self):
        return self._notaries

    @notaries.setter
    def notaries(self, value):
        if isinstance(value, list):
            self._notaries = list()
            for i in value:
                if isinstance(i, NotaryResultDTO):
                    self._notaries.append(i)
                else:
                    self._notaries.append(NotaryResultDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlegalchainNotaryQueryResponse, self).parse_response_content(response_content)
        if 'notaries' in response:
            self.notaries = response['notaries']
