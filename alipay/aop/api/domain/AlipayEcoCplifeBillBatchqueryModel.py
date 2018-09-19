#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCplifeBillBatchqueryModel(object):

    def __init__(self):
        self._acct_period = None
        self._batch_id = None
        self._bill_status = None
        self._community_id = None
        self._cost_type = None
        self._out_room_id = None
        self._page_num = None
        self._page_size = None
        self._release_day = None

    @property
    def acct_period(self):
        return self._acct_period

    @acct_period.setter
    def acct_period(self, value):
        self._acct_period = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def cost_type(self):
        return self._cost_type

    @cost_type.setter
    def cost_type(self, value):
        self._cost_type = value
    @property
    def out_room_id(self):
        return self._out_room_id

    @out_room_id.setter
    def out_room_id(self, value):
        self._out_room_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def release_day(self):
        return self._release_day

    @release_day.setter
    def release_day(self, value):
        self._release_day = value


    def to_alipay_dict(self):
        params = dict()
        if self.acct_period:
            if hasattr(self.acct_period, 'to_alipay_dict'):
                params['acct_period'] = self.acct_period.to_alipay_dict()
            else:
                params['acct_period'] = self.acct_period
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.bill_status:
            if hasattr(self.bill_status, 'to_alipay_dict'):
                params['bill_status'] = self.bill_status.to_alipay_dict()
            else:
                params['bill_status'] = self.bill_status
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.cost_type:
            if hasattr(self.cost_type, 'to_alipay_dict'):
                params['cost_type'] = self.cost_type.to_alipay_dict()
            else:
                params['cost_type'] = self.cost_type
        if self.out_room_id:
            if hasattr(self.out_room_id, 'to_alipay_dict'):
                params['out_room_id'] = self.out_room_id.to_alipay_dict()
            else:
                params['out_room_id'] = self.out_room_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.release_day:
            if hasattr(self.release_day, 'to_alipay_dict'):
                params['release_day'] = self.release_day.to_alipay_dict()
            else:
                params['release_day'] = self.release_day
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeBillBatchqueryModel()
        if 'acct_period' in d:
            o.acct_period = d['acct_period']
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'bill_status' in d:
            o.bill_status = d['bill_status']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'cost_type' in d:
            o.cost_type = d['cost_type']
        if 'out_room_id' in d:
            o.out_room_id = d['out_room_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'release_day' in d:
            o.release_day = d['release_day']
        return o


