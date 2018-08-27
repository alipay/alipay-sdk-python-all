#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExproductconfResponse import ExproductconfResponse


class AlipayEbppProductSearchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppProductSearchResponse, self).__init__()
        self._exproductconfs = None

    @property
    def exproductconfs(self):
        return self._exproductconfs

    @exproductconfs.setter
    def exproductconfs(self, value):
        if isinstance(value, list):
            self._exproductconfs = list()
            for i in value:
                if isinstance(i, ExproductconfResponse):
                    self._exproductconfs.append(i)
                else:
                    self._exproductconfs.append(ExproductconfResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppProductSearchResponse, self).parse_response_content(response_content)
        if 'exproductconfs' in response:
            self.exproductconfs = response['exproductconfs']
