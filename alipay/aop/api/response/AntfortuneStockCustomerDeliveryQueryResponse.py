#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryPositionVO import DeliveryPositionVO


class AntfortuneStockCustomerDeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockCustomerDeliveryQueryResponse, self).__init__()
        self._agreement_no = None
        self._delivery_position = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def delivery_position(self):
        return self._delivery_position

    @delivery_position.setter
    def delivery_position(self, value):
        if isinstance(value, list):
            self._delivery_position = list()
            for i in value:
                if isinstance(i, DeliveryPositionVO):
                    self._delivery_position.append(i)
                else:
                    self._delivery_position.append(DeliveryPositionVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockCustomerDeliveryQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'delivery_position' in response:
            self.delivery_position = response['delivery_position']
