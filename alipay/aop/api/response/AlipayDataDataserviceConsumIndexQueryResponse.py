#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndexDetail import IndexDetail


class AlipayDataDataserviceConsumIndexQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceConsumIndexQueryResponse, self).__init__()
        self._index_detail = None

    @property
    def index_detail(self):
        return self._index_detail

    @index_detail.setter
    def index_detail(self, value):
        if isinstance(value, list):
            self._index_detail = list()
            for i in value:
                if isinstance(i, IndexDetail):
                    self._index_detail.append(i)
                else:
                    self._index_detail.append(IndexDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceConsumIndexQueryResponse, self).parse_response_content(response_content)
        if 'index_detail' in response:
            self.index_detail = response['index_detail']
