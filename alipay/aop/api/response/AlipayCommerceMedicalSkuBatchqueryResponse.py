#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemSkuInfoDTO import ItemSkuInfoDTO


class AlipayCommerceMedicalSkuBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalSkuBatchqueryResponse, self).__init__()
        self._sku_info_list = None

    @property
    def sku_info_list(self):
        return self._sku_info_list

    @sku_info_list.setter
    def sku_info_list(self, value):
        if isinstance(value, list):
            self._sku_info_list = list()
            for i in value:
                if isinstance(i, ItemSkuInfoDTO):
                    self._sku_info_list.append(i)
                else:
                    self._sku_info_list.append(ItemSkuInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalSkuBatchqueryResponse, self).parse_response_content(response_content)
        if 'sku_info_list' in response:
            self.sku_info_list = response['sku_info_list']
