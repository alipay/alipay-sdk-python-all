#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FoodDispenserCellInfo import FoodDispenserCellInfo


class KoubeiMerchantKbdeviceDispenserQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantKbdeviceDispenserQueryResponse, self).__init__()
        self._availability = None
        self._cell_info_list = None
        self._device_id = None

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, value):
        self._availability = value
    @property
    def cell_info_list(self):
        return self._cell_info_list

    @cell_info_list.setter
    def cell_info_list(self, value):
        if isinstance(value, list):
            self._cell_info_list = list()
            for i in value:
                if isinstance(i, FoodDispenserCellInfo):
                    self._cell_info_list.append(i)
                else:
                    self._cell_info_list.append(FoodDispenserCellInfo.from_alipay_dict(i))
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantKbdeviceDispenserQueryResponse, self).parse_response_content(response_content)
        if 'availability' in response:
            self.availability = response['availability']
        if 'cell_info_list' in response:
            self.cell_info_list = response['cell_info_list']
        if 'device_id' in response:
            self.device_id = response['device_id']
