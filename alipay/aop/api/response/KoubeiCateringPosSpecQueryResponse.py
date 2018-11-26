#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SpecEntity import SpecEntity


class KoubeiCateringPosSpecQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosSpecQueryResponse, self).__init__()
        self._specs = None

    @property
    def specs(self):
        return self._specs

    @specs.setter
    def specs(self, value):
        if isinstance(value, list):
            self._specs = list()
            for i in value:
                if isinstance(i, SpecEntity):
                    self._specs.append(i)
                else:
                    self._specs.append(SpecEntity.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosSpecQueryResponse, self).parse_response_content(response_content)
        if 'specs' in response:
            self.specs = response['specs']
