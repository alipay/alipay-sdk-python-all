#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityThirdpartybillCreateModel(object):

    def __init__(self):
        self._alipay_uid = None
        self._amount = None
        self._bill_detail_url = None
        self._bill_end_time = None
        self._bill_start_time = None
        self._biz_no = None
        self._community_room_id = None
        self._open_id = None
        self._out_community_id = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_detail_url(self):
        return self._bill_detail_url

    @bill_detail_url.setter
    def bill_detail_url(self, value):
        self._bill_detail_url = value
    @property
    def bill_end_time(self):
        return self._bill_end_time

    @bill_end_time.setter
    def bill_end_time(self, value):
        self._bill_end_time = value
    @property
    def bill_start_time(self):
        return self._bill_start_time

    @bill_start_time.setter
    def bill_start_time(self, value):
        self._bill_start_time = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def community_room_id(self):
        return self._community_room_id

    @community_room_id.setter
    def community_room_id(self, value):
        self._community_room_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_community_id(self):
        return self._out_community_id

    @out_community_id.setter
    def out_community_id(self, value):
        self._out_community_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_detail_url:
            if hasattr(self.bill_detail_url, 'to_alipay_dict'):
                params['bill_detail_url'] = self.bill_detail_url.to_alipay_dict()
            else:
                params['bill_detail_url'] = self.bill_detail_url
        if self.bill_end_time:
            if hasattr(self.bill_end_time, 'to_alipay_dict'):
                params['bill_end_time'] = self.bill_end_time.to_alipay_dict()
            else:
                params['bill_end_time'] = self.bill_end_time
        if self.bill_start_time:
            if hasattr(self.bill_start_time, 'to_alipay_dict'):
                params['bill_start_time'] = self.bill_start_time.to_alipay_dict()
            else:
                params['bill_start_time'] = self.bill_start_time
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.community_room_id:
            if hasattr(self.community_room_id, 'to_alipay_dict'):
                params['community_room_id'] = self.community_room_id.to_alipay_dict()
            else:
                params['community_room_id'] = self.community_room_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_community_id:
            if hasattr(self.out_community_id, 'to_alipay_dict'):
                params['out_community_id'] = self.out_community_id.to_alipay_dict()
            else:
                params['out_community_id'] = self.out_community_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityThirdpartybillCreateModel()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_detail_url' in d:
            o.bill_detail_url = d['bill_detail_url']
        if 'bill_end_time' in d:
            o.bill_end_time = d['bill_end_time']
        if 'bill_start_time' in d:
            o.bill_start_time = d['bill_start_time']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'community_room_id' in d:
            o.community_room_id = d['community_room_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_community_id' in d:
            o.out_community_id = d['out_community_id']
        return o


