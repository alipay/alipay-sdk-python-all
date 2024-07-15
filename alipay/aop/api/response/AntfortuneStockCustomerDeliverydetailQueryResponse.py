#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryDetailPositionVO import DeliveryDetailPositionVO


class AntfortuneStockCustomerDeliverydetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockCustomerDeliverydetailQueryResponse, self).__init__()
        self._agreement_no = None
        self._delivery_detail_position = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def delivery_detail_position(self):
        return self._delivery_detail_position

    @delivery_detail_position.setter
    def delivery_detail_position(self, value):
        if isinstance(value, DeliveryDetailPositionVO):
            self._delivery_detail_position = value
        else:
            self._delivery_detail_position = DeliveryDetailPositionVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockCustomerDeliverydetailQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'delivery_detail_position' in response:
            self.delivery_detail_position = response['delivery_detail_position']
