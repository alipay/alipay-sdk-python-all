#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantActivityVoucherInfo import MerchantActivityVoucherInfo


class KoubeiMarketingCampaignItemMerchantactivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignItemMerchantactivityQueryResponse, self).__init__()
        self._activity_id = None
        self._camp_id = None
        self._count_limit = None
        self._count_limit_per_day = None
        self._count_limit_per_user = None
        self._count_limit_per_user_per_day = None
        self._crowd = None
        self._deduct_amount = None
        self._external_unique_id = None
        self._gmt_end = None
        self._gmt_start = None
        self._item_ids = None
        self._memo = None
        self._min_cost = None
        self._obtain_manually = None
        self._voucher_info = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def count_limit(self):
        return self._count_limit

    @count_limit.setter
    def count_limit(self, value):
        self._count_limit = value
    @property
    def count_limit_per_day(self):
        return self._count_limit_per_day

    @count_limit_per_day.setter
    def count_limit_per_day(self, value):
        self._count_limit_per_day = value
    @property
    def count_limit_per_user(self):
        return self._count_limit_per_user

    @count_limit_per_user.setter
    def count_limit_per_user(self, value):
        self._count_limit_per_user = value
    @property
    def count_limit_per_user_per_day(self):
        return self._count_limit_per_user_per_day

    @count_limit_per_user_per_day.setter
    def count_limit_per_user_per_day(self, value):
        self._count_limit_per_user_per_day = value
    @property
    def crowd(self):
        return self._crowd

    @crowd.setter
    def crowd(self, value):
        self._crowd = value
    @property
    def deduct_amount(self):
        return self._deduct_amount

    @deduct_amount.setter
    def deduct_amount(self, value):
        self._deduct_amount = value
    @property
    def external_unique_id(self):
        return self._external_unique_id

    @external_unique_id.setter
    def external_unique_id(self, value):
        self._external_unique_id = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def min_cost(self):
        return self._min_cost

    @min_cost.setter
    def min_cost(self, value):
        self._min_cost = value
    @property
    def obtain_manually(self):
        return self._obtain_manually

    @obtain_manually.setter
    def obtain_manually(self, value):
        self._obtain_manually = value
    @property
    def voucher_info(self):
        return self._voucher_info

    @voucher_info.setter
    def voucher_info(self, value):
        if isinstance(value, MerchantActivityVoucherInfo):
            self._voucher_info = value
        else:
            self._voucher_info = MerchantActivityVoucherInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignItemMerchantactivityQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
        if 'count_limit' in response:
            self.count_limit = response['count_limit']
        if 'count_limit_per_day' in response:
            self.count_limit_per_day = response['count_limit_per_day']
        if 'count_limit_per_user' in response:
            self.count_limit_per_user = response['count_limit_per_user']
        if 'count_limit_per_user_per_day' in response:
            self.count_limit_per_user_per_day = response['count_limit_per_user_per_day']
        if 'crowd' in response:
            self.crowd = response['crowd']
        if 'deduct_amount' in response:
            self.deduct_amount = response['deduct_amount']
        if 'external_unique_id' in response:
            self.external_unique_id = response['external_unique_id']
        if 'gmt_end' in response:
            self.gmt_end = response['gmt_end']
        if 'gmt_start' in response:
            self.gmt_start = response['gmt_start']
        if 'item_ids' in response:
            self.item_ids = response['item_ids']
        if 'memo' in response:
            self.memo = response['memo']
        if 'min_cost' in response:
            self.min_cost = response['min_cost']
        if 'obtain_manually' in response:
            self.obtain_manually = response['obtain_manually']
        if 'voucher_info' in response:
            self.voucher_info = response['voucher_info']
