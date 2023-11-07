#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemPackageInstance import ItemPackageInstance


class AlipayCloudCloudbaseResourcepackageItempackageinstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageItempackageinstanceQueryResponse, self).__init__()
        self._item_package_instances = None

    @property
    def item_package_instances(self):
        return self._item_package_instances

    @item_package_instances.setter
    def item_package_instances(self, value):
        if isinstance(value, list):
            self._item_package_instances = list()
            for i in value:
                if isinstance(i, ItemPackageInstance):
                    self._item_package_instances.append(i)
                else:
                    self._item_package_instances.append(ItemPackageInstance.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageItempackageinstanceQueryResponse, self).parse_response_content(response_content)
        if 'item_package_instances' in response:
            self.item_package_instances = response['item_package_instances']
