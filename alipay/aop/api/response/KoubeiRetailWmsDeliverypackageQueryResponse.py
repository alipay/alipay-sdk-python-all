#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryPackageVO import DeliveryPackageVO


class KoubeiRetailWmsDeliverypackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsDeliverypackageQueryResponse, self).__init__()
        self._delivery_package_vo_list = None

    @property
    def delivery_package_vo_list(self):
        return self._delivery_package_vo_list

    @delivery_package_vo_list.setter
    def delivery_package_vo_list(self, value):
        if isinstance(value, list):
            self._delivery_package_vo_list = list()
            for i in value:
                if isinstance(i, DeliveryPackageVO):
                    self._delivery_package_vo_list.append(i)
                else:
                    self._delivery_package_vo_list.append(DeliveryPackageVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsDeliverypackageQueryResponse, self).parse_response_content(response_content)
        if 'delivery_package_vo_list' in response:
            self.delivery_package_vo_list = response['delivery_package_vo_list']
