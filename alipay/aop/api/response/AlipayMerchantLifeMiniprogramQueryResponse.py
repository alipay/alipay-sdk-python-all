#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniprogramExtra import MiniprogramExtra


class AlipayMerchantLifeMiniprogramQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantLifeMiniprogramQueryResponse, self).__init__()
        self._extra = None
        self._public_id = None

    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, value):
        if isinstance(value, MiniprogramExtra):
            self._extra = value
        else:
            self._extra = MiniprogramExtra.from_alipay_dict(value)
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantLifeMiniprogramQueryResponse, self).parse_response_content(response_content)
        if 'extra' in response:
            self.extra = response['extra']
        if 'public_id' in response:
            self.public_id = response['public_id']
