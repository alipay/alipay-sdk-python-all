#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HuaweiMPBuyerDTO import HuaweiMPBuyerDTO


class AnttechOceanbaseEntityroleHuaweimpBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseEntityroleHuaweimpBatchqueryResponse, self).__init__()
        self._huawei_buyer_info_list = None

    @property
    def huawei_buyer_info_list(self):
        return self._huawei_buyer_info_list

    @huawei_buyer_info_list.setter
    def huawei_buyer_info_list(self, value):
        if isinstance(value, list):
            self._huawei_buyer_info_list = list()
            for i in value:
                if isinstance(i, HuaweiMPBuyerDTO):
                    self._huawei_buyer_info_list.append(i)
                else:
                    self._huawei_buyer_info_list.append(HuaweiMPBuyerDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseEntityroleHuaweimpBatchqueryResponse, self).parse_response_content(response_content)
        if 'huawei_buyer_info_list' in response:
            self.huawei_buyer_info_list = response['huawei_buyer_info_list']
