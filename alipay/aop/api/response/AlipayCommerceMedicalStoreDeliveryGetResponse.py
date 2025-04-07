#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryVO import DeliveryVO


class AlipayCommerceMedicalStoreDeliveryGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalStoreDeliveryGetResponse, self).__init__()
        self._delivery_list = None
        self._store_code = None

    @property
    def delivery_list(self):
        return self._delivery_list

    @delivery_list.setter
    def delivery_list(self, value):
        if isinstance(value, list):
            self._delivery_list = list()
            for i in value:
                if isinstance(i, DeliveryVO):
                    self._delivery_list.append(i)
                else:
                    self._delivery_list.append(DeliveryVO.from_alipay_dict(i))
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalStoreDeliveryGetResponse, self).parse_response_content(response_content)
        if 'delivery_list' in response:
            self.delivery_list = response['delivery_list']
        if 'store_code' in response:
            self.store_code = response['store_code']
