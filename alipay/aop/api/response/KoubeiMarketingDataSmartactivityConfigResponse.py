#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingDataSmartactivityConfigResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataSmartactivityConfigResponse, self).__init__()
        self._activity_type = None
        self._activity_valid_days = None
        self._config_code = None
        self._crowd_group = None
        self._ext_info = None
        self._item_id = None
        self._item_name = None
        self._min_consume = None
        self._min_cost = None
        self._pro_type = None
        self._voucher_type = None
        self._voucher_valid_days = None
        self._worth_value = None

    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def activity_valid_days(self):
        return self._activity_valid_days

    @activity_valid_days.setter
    def activity_valid_days(self, value):
        self._activity_valid_days = value
    @property
    def config_code(self):
        return self._config_code

    @config_code.setter
    def config_code(self, value):
        self._config_code = value
    @property
    def crowd_group(self):
        return self._crowd_group

    @crowd_group.setter
    def crowd_group(self, value):
        self._crowd_group = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def min_consume(self):
        return self._min_consume

    @min_consume.setter
    def min_consume(self, value):
        self._min_consume = value
    @property
    def min_cost(self):
        return self._min_cost

    @min_cost.setter
    def min_cost(self, value):
        self._min_cost = value
    @property
    def pro_type(self):
        return self._pro_type

    @pro_type.setter
    def pro_type(self, value):
        self._pro_type = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def voucher_valid_days(self):
        return self._voucher_valid_days

    @voucher_valid_days.setter
    def voucher_valid_days(self, value):
        self._voucher_valid_days = value
    @property
    def worth_value(self):
        return self._worth_value

    @worth_value.setter
    def worth_value(self, value):
        self._worth_value = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataSmartactivityConfigResponse, self).parse_response_content(response_content)
        if 'activity_type' in response:
            self.activity_type = response['activity_type']
        if 'activity_valid_days' in response:
            self.activity_valid_days = response['activity_valid_days']
        if 'config_code' in response:
            self.config_code = response['config_code']
        if 'crowd_group' in response:
            self.crowd_group = response['crowd_group']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'item_name' in response:
            self.item_name = response['item_name']
        if 'min_consume' in response:
            self.min_consume = response['min_consume']
        if 'min_cost' in response:
            self.min_cost = response['min_cost']
        if 'pro_type' in response:
            self.pro_type = response['pro_type']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
        if 'voucher_valid_days' in response:
            self.voucher_valid_days = response['voucher_valid_days']
        if 'worth_value' in response:
            self.worth_value = response['worth_value']
