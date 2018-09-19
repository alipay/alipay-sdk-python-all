#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtitemDetailInfo import ExtitemDetailInfo


class KoubeiRetailExtitemShopextitemQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailExtitemShopextitemQueryResponse, self).__init__()
        self._extitem_detail_list = None
        self._total_count = None

    @property
    def extitem_detail_list(self):
        return self._extitem_detail_list

    @extitem_detail_list.setter
    def extitem_detail_list(self, value):
        if isinstance(value, list):
            self._extitem_detail_list = list()
            for i in value:
                if isinstance(i, ExtitemDetailInfo):
                    self._extitem_detail_list.append(i)
                else:
                    self._extitem_detail_list.append(ExtitemDetailInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailExtitemShopextitemQueryResponse, self).parse_response_content(response_content)
        if 'extitem_detail_list' in response:
            self.extitem_detail_list = response['extitem_detail_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
