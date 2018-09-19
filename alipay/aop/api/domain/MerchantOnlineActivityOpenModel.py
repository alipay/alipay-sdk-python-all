#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantActivityVoucherInfo import MerchantActivityVoucherInfo


class MerchantOnlineActivityOpenModel(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.count_limit:
            if hasattr(self.count_limit, 'to_alipay_dict'):
                params['count_limit'] = self.count_limit.to_alipay_dict()
            else:
                params['count_limit'] = self.count_limit
        if self.count_limit_per_day:
            if hasattr(self.count_limit_per_day, 'to_alipay_dict'):
                params['count_limit_per_day'] = self.count_limit_per_day.to_alipay_dict()
            else:
                params['count_limit_per_day'] = self.count_limit_per_day
        if self.count_limit_per_user:
            if hasattr(self.count_limit_per_user, 'to_alipay_dict'):
                params['count_limit_per_user'] = self.count_limit_per_user.to_alipay_dict()
            else:
                params['count_limit_per_user'] = self.count_limit_per_user
        if self.count_limit_per_user_per_day:
            if hasattr(self.count_limit_per_user_per_day, 'to_alipay_dict'):
                params['count_limit_per_user_per_day'] = self.count_limit_per_user_per_day.to_alipay_dict()
            else:
                params['count_limit_per_user_per_day'] = self.count_limit_per_user_per_day
        if self.crowd:
            if hasattr(self.crowd, 'to_alipay_dict'):
                params['crowd'] = self.crowd.to_alipay_dict()
            else:
                params['crowd'] = self.crowd
        if self.deduct_amount:
            if hasattr(self.deduct_amount, 'to_alipay_dict'):
                params['deduct_amount'] = self.deduct_amount.to_alipay_dict()
            else:
                params['deduct_amount'] = self.deduct_amount
        if self.external_unique_id:
            if hasattr(self.external_unique_id, 'to_alipay_dict'):
                params['external_unique_id'] = self.external_unique_id.to_alipay_dict()
            else:
                params['external_unique_id'] = self.external_unique_id
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.item_ids:
            if isinstance(self.item_ids, list):
                for i in range(0, len(self.item_ids)):
                    element = self.item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.min_cost:
            if hasattr(self.min_cost, 'to_alipay_dict'):
                params['min_cost'] = self.min_cost.to_alipay_dict()
            else:
                params['min_cost'] = self.min_cost
        if self.obtain_manually:
            if hasattr(self.obtain_manually, 'to_alipay_dict'):
                params['obtain_manually'] = self.obtain_manually.to_alipay_dict()
            else:
                params['obtain_manually'] = self.obtain_manually
        if self.voucher_info:
            if hasattr(self.voucher_info, 'to_alipay_dict'):
                params['voucher_info'] = self.voucher_info.to_alipay_dict()
            else:
                params['voucher_info'] = self.voucher_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantOnlineActivityOpenModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'count_limit' in d:
            o.count_limit = d['count_limit']
        if 'count_limit_per_day' in d:
            o.count_limit_per_day = d['count_limit_per_day']
        if 'count_limit_per_user' in d:
            o.count_limit_per_user = d['count_limit_per_user']
        if 'count_limit_per_user_per_day' in d:
            o.count_limit_per_user_per_day = d['count_limit_per_user_per_day']
        if 'crowd' in d:
            o.crowd = d['crowd']
        if 'deduct_amount' in d:
            o.deduct_amount = d['deduct_amount']
        if 'external_unique_id' in d:
            o.external_unique_id = d['external_unique_id']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        if 'memo' in d:
            o.memo = d['memo']
        if 'min_cost' in d:
            o.min_cost = d['min_cost']
        if 'obtain_manually' in d:
            o.obtain_manually = d['obtain_manually']
        if 'voucher_info' in d:
            o.voucher_info = d['voucher_info']
        return o


