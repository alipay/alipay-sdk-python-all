#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MorphoAppItem import MorphoAppItem
from alipay.aop.api.domain.MorphoPaginator import MorphoPaginator


class AlipayOpenMiniMorphoApplistBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMorphoApplistBatchqueryResponse, self).__init__()
        self._data_list = None
        self._paginator = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, MorphoAppItem):
                    self._data_list.append(i)
                else:
                    self._data_list.append(MorphoAppItem.from_alipay_dict(i))
    @property
    def paginator(self):
        return self._paginator

    @paginator.setter
    def paginator(self, value):
        if isinstance(value, MorphoPaginator):
            self._paginator = value
        else:
            self._paginator = MorphoPaginator.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMorphoApplistBatchqueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'paginator' in response:
            self.paginator = response['paginator']
