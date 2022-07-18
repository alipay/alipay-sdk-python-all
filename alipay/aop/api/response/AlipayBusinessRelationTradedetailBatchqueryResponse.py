#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessRelationShopTradeDetailInfo import BusinessRelationShopTradeDetailInfo


class AlipayBusinessRelationTradedetailBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationTradedetailBatchqueryResponse, self).__init__()
        self._real_shop_id = None
        self._real_shop_no = None
        self._shop_confirm_status = None
        self._shop_name = None
        self._shop_trade_data_detail_infos = None
        self._total_num = None

    @property
    def real_shop_id(self):
        return self._real_shop_id

    @real_shop_id.setter
    def real_shop_id(self, value):
        self._real_shop_id = value
    @property
    def real_shop_no(self):
        return self._real_shop_no

    @real_shop_no.setter
    def real_shop_no(self, value):
        self._real_shop_no = value
    @property
    def shop_confirm_status(self):
        return self._shop_confirm_status

    @shop_confirm_status.setter
    def shop_confirm_status(self, value):
        self._shop_confirm_status = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_trade_data_detail_infos(self):
        return self._shop_trade_data_detail_infos

    @shop_trade_data_detail_infos.setter
    def shop_trade_data_detail_infos(self, value):
        if isinstance(value, list):
            self._shop_trade_data_detail_infos = list()
            for i in value:
                if isinstance(i, BusinessRelationShopTradeDetailInfo):
                    self._shop_trade_data_detail_infos.append(i)
                else:
                    self._shop_trade_data_detail_infos.append(BusinessRelationShopTradeDetailInfo.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationTradedetailBatchqueryResponse, self).parse_response_content(response_content)
        if 'real_shop_id' in response:
            self.real_shop_id = response['real_shop_id']
        if 'real_shop_no' in response:
            self.real_shop_no = response['real_shop_no']
        if 'shop_confirm_status' in response:
            self.shop_confirm_status = response['shop_confirm_status']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'shop_trade_data_detail_infos' in response:
            self.shop_trade_data_detail_infos = response['shop_trade_data_detail_infos']
        if 'total_num' in response:
            self.total_num = response['total_num']
