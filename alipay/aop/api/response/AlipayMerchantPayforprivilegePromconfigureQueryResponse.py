#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantPayforprivilegePromconfigureQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPayforprivilegePromconfigureQueryResponse, self).__init__()
        self._enabled_shop_list = None
        self._exclude_item_ids = None
        self._support_item_ids = None

    @property
    def enabled_shop_list(self):
        return self._enabled_shop_list

    @enabled_shop_list.setter
    def enabled_shop_list(self, value):
        if isinstance(value, list):
            self._enabled_shop_list = list()
            for i in value:
                self._enabled_shop_list.append(i)
    @property
    def exclude_item_ids(self):
        return self._exclude_item_ids

    @exclude_item_ids.setter
    def exclude_item_ids(self, value):
        if isinstance(value, list):
            self._exclude_item_ids = list()
            for i in value:
                self._exclude_item_ids.append(i)
    @property
    def support_item_ids(self):
        return self._support_item_ids

    @support_item_ids.setter
    def support_item_ids(self, value):
        if isinstance(value, list):
            self._support_item_ids = list()
            for i in value:
                self._support_item_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPayforprivilegePromconfigureQueryResponse, self).parse_response_content(response_content)
        if 'enabled_shop_list' in response:
            self.enabled_shop_list = response['enabled_shop_list']
        if 'exclude_item_ids' in response:
            self.exclude_item_ids = response['exclude_item_ids']
        if 'support_item_ids' in response:
            self.support_item_ids = response['support_item_ids']
