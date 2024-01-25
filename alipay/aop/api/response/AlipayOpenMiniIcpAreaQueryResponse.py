#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IcpProvinceAreaItemList import IcpProvinceAreaItemList


class AlipayOpenMiniIcpAreaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIcpAreaQueryResponse, self).__init__()
        self._area_items = None

    @property
    def area_items(self):
        return self._area_items

    @area_items.setter
    def area_items(self, value):
        if isinstance(value, list):
            self._area_items = list()
            for i in value:
                if isinstance(i, IcpProvinceAreaItemList):
                    self._area_items.append(i)
                else:
                    self._area_items.append(IcpProvinceAreaItemList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIcpAreaQueryResponse, self).parse_response_content(response_content)
        if 'area_items' in response:
            self.area_items = response['area_items']
