#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BoardIndex import BoardIndex


class AlipayMerchantQipanBoardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanBoardQueryResponse, self).__init__()
        self._index_list = None

    @property
    def index_list(self):
        return self._index_list

    @index_list.setter
    def index_list(self, value):
        if isinstance(value, list):
            self._index_list = list()
            for i in value:
                if isinstance(i, BoardIndex):
                    self._index_list.append(i)
                else:
                    self._index_list.append(BoardIndex.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanBoardQueryResponse, self).parse_response_content(response_content)
        if 'index_list' in response:
            self.index_list = response['index_list']
