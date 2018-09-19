#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProducerVO import ProducerVO


class KoubeiRetailWmsProducerQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsProducerQueryResponse, self).__init__()
        self._producers = None
        self._total_count = None

    @property
    def producers(self):
        return self._producers

    @producers.setter
    def producers(self, value):
        if isinstance(value, list):
            self._producers = list()
            for i in value:
                if isinstance(i, ProducerVO):
                    self._producers.append(i)
                else:
                    self._producers.append(ProducerVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsProducerQueryResponse, self).parse_response_content(response_content)
        if 'producers' in response:
            self.producers = response['producers']
        if 'total_count' in response:
            self.total_count = response['total_count']
