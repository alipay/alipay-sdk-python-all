#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderServicePackageVO import OrderServicePackageVO


class AlipayCommerceMedicalServicepackageOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServicepackageOrderQueryResponse, self).__init__()
        self._order_service_package_vo_list = None

    @property
    def order_service_package_vo_list(self):
        return self._order_service_package_vo_list

    @order_service_package_vo_list.setter
    def order_service_package_vo_list(self, value):
        if isinstance(value, list):
            self._order_service_package_vo_list = list()
            for i in value:
                if isinstance(i, OrderServicePackageVO):
                    self._order_service_package_vo_list.append(i)
                else:
                    self._order_service_package_vo_list.append(OrderServicePackageVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServicepackageOrderQueryResponse, self).parse_response_content(response_content)
        if 'order_service_package_vo_list' in response:
            self.order_service_package_vo_list = response['order_service_package_vo_list']
