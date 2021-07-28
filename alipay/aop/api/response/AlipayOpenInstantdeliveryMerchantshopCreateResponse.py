#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LogisticsShopStatusDTO import LogisticsShopStatusDTO


class AlipayOpenInstantdeliveryMerchantshopCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenInstantdeliveryMerchantshopCreateResponse, self).__init__()
        self._logistics_shop_status = None

    @property
    def logistics_shop_status(self):
        return self._logistics_shop_status

    @logistics_shop_status.setter
    def logistics_shop_status(self, value):
        if isinstance(value, list):
            self._logistics_shop_status = list()
            for i in value:
                if isinstance(i, LogisticsShopStatusDTO):
                    self._logistics_shop_status.append(i)
                else:
                    self._logistics_shop_status.append(LogisticsShopStatusDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenInstantdeliveryMerchantshopCreateResponse, self).parse_response_content(response_content)
        if 'logistics_shop_status' in response:
            self.logistics_shop_status = response['logistics_shop_status']
