#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopTaskDeliveryInfo import ShopTaskDeliveryInfo


class AlipayOpenSpNordermaterialsapplyTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyTaskQueryResponse, self).__init__()
        self._has_monthly_trade = None
        self._has_weekly_trade = None
        self._monthly_trade_cnt = None
        self._poi_mid = None
        self._shop_task_delivery_info_list = None
        self._shop_task_id = None
        self._shop_task_status = None
        self._weekly_trade_cnt = None

    @property
    def has_monthly_trade(self):
        return self._has_monthly_trade

    @has_monthly_trade.setter
    def has_monthly_trade(self, value):
        self._has_monthly_trade = value
    @property
    def has_weekly_trade(self):
        return self._has_weekly_trade

    @has_weekly_trade.setter
    def has_weekly_trade(self, value):
        self._has_weekly_trade = value
    @property
    def monthly_trade_cnt(self):
        return self._monthly_trade_cnt

    @monthly_trade_cnt.setter
    def monthly_trade_cnt(self, value):
        self._monthly_trade_cnt = value
    @property
    def poi_mid(self):
        return self._poi_mid

    @poi_mid.setter
    def poi_mid(self, value):
        self._poi_mid = value
    @property
    def shop_task_delivery_info_list(self):
        return self._shop_task_delivery_info_list

    @shop_task_delivery_info_list.setter
    def shop_task_delivery_info_list(self, value):
        if isinstance(value, list):
            self._shop_task_delivery_info_list = list()
            for i in value:
                if isinstance(i, ShopTaskDeliveryInfo):
                    self._shop_task_delivery_info_list.append(i)
                else:
                    self._shop_task_delivery_info_list.append(ShopTaskDeliveryInfo.from_alipay_dict(i))
    @property
    def shop_task_id(self):
        return self._shop_task_id

    @shop_task_id.setter
    def shop_task_id(self, value):
        self._shop_task_id = value
    @property
    def shop_task_status(self):
        return self._shop_task_status

    @shop_task_status.setter
    def shop_task_status(self, value):
        self._shop_task_status = value
    @property
    def weekly_trade_cnt(self):
        return self._weekly_trade_cnt

    @weekly_trade_cnt.setter
    def weekly_trade_cnt(self, value):
        self._weekly_trade_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyTaskQueryResponse, self).parse_response_content(response_content)
        if 'has_monthly_trade' in response:
            self.has_monthly_trade = response['has_monthly_trade']
        if 'has_weekly_trade' in response:
            self.has_weekly_trade = response['has_weekly_trade']
        if 'monthly_trade_cnt' in response:
            self.monthly_trade_cnt = response['monthly_trade_cnt']
        if 'poi_mid' in response:
            self.poi_mid = response['poi_mid']
        if 'shop_task_delivery_info_list' in response:
            self.shop_task_delivery_info_list = response['shop_task_delivery_info_list']
        if 'shop_task_id' in response:
            self.shop_task_id = response['shop_task_id']
        if 'shop_task_status' in response:
            self.shop_task_status = response['shop_task_status']
        if 'weekly_trade_cnt' in response:
            self.weekly_trade_cnt = response['weekly_trade_cnt']
