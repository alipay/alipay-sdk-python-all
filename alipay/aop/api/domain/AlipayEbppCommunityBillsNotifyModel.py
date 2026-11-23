#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RemoteExternalBillDetail import RemoteExternalBillDetail


class AlipayEbppCommunityBillsNotifyModel(object):

    def __init__(self):
        self._amount = None
        self._bill_list = None
        self._bill_type = None
        self._community_short_name = None
        self._end_date = None
        self._open_id = None
        self._out_room_id = None
        self._start_date = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, RemoteExternalBillDetail):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(RemoteExternalBillDetail.from_alipay_dict(i))
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_room_id(self):
        return self._out_room_id

    @out_room_id.setter
    def out_room_id(self, value):
        self._out_room_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_list:
            if isinstance(self.bill_list, list):
                for i in range(0, len(self.bill_list)):
                    element = self.bill_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_list, 'to_alipay_dict'):
                params['bill_list'] = self.bill_list.to_alipay_dict()
            else:
                params['bill_list'] = self.bill_list
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_room_id:
            if hasattr(self.out_room_id, 'to_alipay_dict'):
                params['out_room_id'] = self.out_room_id.to_alipay_dict()
            else:
                params['out_room_id'] = self.out_room_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityBillsNotifyModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_list' in d:
            o.bill_list = d['bill_list']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_room_id' in d:
            o.out_room_id = d['out_room_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


