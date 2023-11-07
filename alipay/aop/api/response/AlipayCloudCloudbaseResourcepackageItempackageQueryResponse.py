#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemPackage import ItemPackage


class AlipayCloudCloudbaseResourcepackageItempackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageItempackageQueryResponse, self).__init__()
        self._item_package_list = None

    @property
    def item_package_list(self):
        return self._item_package_list

    @item_package_list.setter
    def item_package_list(self, value):
        if isinstance(value, list):
            self._item_package_list = list()
            for i in value:
                if isinstance(i, ItemPackage):
                    self._item_package_list.append(i)
                else:
                    self._item_package_list.append(ItemPackage.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageItempackageQueryResponse, self).parse_response_content(response_content)
        if 'item_package_list' in response:
            self.item_package_list = response['item_package_list']
