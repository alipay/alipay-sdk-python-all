#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessRelationTradeInfo import BusinessRelationTradeInfo
from alipay.aop.api.domain.BusinessRelationShopTradeInfo import BusinessRelationShopTradeInfo


class AlipayBusinessRelationTradedataBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationTradedataBatchqueryResponse, self).__init__()
        self._mall_trade_data_info = None
        self._shop_trade_data_infos = None
        self._total_num = None

    @property
    def mall_trade_data_info(self):
        return self._mall_trade_data_info

    @mall_trade_data_info.setter
    def mall_trade_data_info(self, value):
        if isinstance(value, BusinessRelationTradeInfo):
            self._mall_trade_data_info = value
        else:
            self._mall_trade_data_info = BusinessRelationTradeInfo.from_alipay_dict(value)
    @property
    def shop_trade_data_infos(self):
        return self._shop_trade_data_infos

    @shop_trade_data_infos.setter
    def shop_trade_data_infos(self, value):
        if isinstance(value, list):
            self._shop_trade_data_infos = list()
            for i in value:
                if isinstance(i, BusinessRelationShopTradeInfo):
                    self._shop_trade_data_infos.append(i)
                else:
                    self._shop_trade_data_infos.append(BusinessRelationShopTradeInfo.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationTradedataBatchqueryResponse, self).parse_response_content(response_content)
        if 'mall_trade_data_info' in response:
            self.mall_trade_data_info = response['mall_trade_data_info']
        if 'shop_trade_data_infos' in response:
            self.shop_trade_data_infos = response['shop_trade_data_infos']
        if 'total_num' in response:
            self.total_num = response['total_num']
