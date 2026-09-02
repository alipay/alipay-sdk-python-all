#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SupplyItemDTO import SupplyItemDTO


class AlipayOfflineProviderIndflowSupplyConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderIndflowSupplyConsultResponse, self).__init__()
        self._out_pos_id = None
        self._supplies = None
        self._supply_count = None

    @property
    def out_pos_id(self):
        return self._out_pos_id

    @out_pos_id.setter
    def out_pos_id(self, value):
        self._out_pos_id = value
    @property
    def supplies(self):
        return self._supplies

    @supplies.setter
    def supplies(self, value):
        if isinstance(value, list):
            self._supplies = list()
            for i in value:
                if isinstance(i, SupplyItemDTO):
                    self._supplies.append(i)
                else:
                    self._supplies.append(SupplyItemDTO.from_alipay_dict(i))
    @property
    def supply_count(self):
        return self._supply_count

    @supply_count.setter
    def supply_count(self, value):
        self._supply_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderIndflowSupplyConsultResponse, self).parse_response_content(response_content)
        if 'out_pos_id' in response:
            self.out_pos_id = response['out_pos_id']
        if 'supplies' in response:
            self.supplies = response['supplies']
        if 'supply_count' in response:
            self.supply_count = response['supply_count']
