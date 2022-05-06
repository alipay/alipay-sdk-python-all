#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantMrchsurplmorderSyncModel(object):

    def __init__(self):
        self._amount = None
        self._biz_id = None
        self._detail_flag = None
        self._item_list = None
        self._lm_order_id = None
        self._main_flag = None
        self._main_lm_order_id = None
        self._modified_time = None
        self._order_status = None
        self._pre_order_status = None
        self._request_id = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def detail_flag(self):
        return self._detail_flag

    @detail_flag.setter
    def detail_flag(self, value):
        self._detail_flag = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        self._item_list = value
    @property
    def lm_order_id(self):
        return self._lm_order_id

    @lm_order_id.setter
    def lm_order_id(self, value):
        self._lm_order_id = value
    @property
    def main_flag(self):
        return self._main_flag

    @main_flag.setter
    def main_flag(self, value):
        self._main_flag = value
    @property
    def main_lm_order_id(self):
        return self._main_lm_order_id

    @main_lm_order_id.setter
    def main_lm_order_id(self, value):
        self._main_lm_order_id = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pre_order_status(self):
        return self._pre_order_status

    @pre_order_status.setter
    def pre_order_status(self, value):
        self._pre_order_status = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
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
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.detail_flag:
            if hasattr(self.detail_flag, 'to_alipay_dict'):
                params['detail_flag'] = self.detail_flag.to_alipay_dict()
            else:
                params['detail_flag'] = self.detail_flag
        if self.item_list:
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.lm_order_id:
            if hasattr(self.lm_order_id, 'to_alipay_dict'):
                params['lm_order_id'] = self.lm_order_id.to_alipay_dict()
            else:
                params['lm_order_id'] = self.lm_order_id
        if self.main_flag:
            if hasattr(self.main_flag, 'to_alipay_dict'):
                params['main_flag'] = self.main_flag.to_alipay_dict()
            else:
                params['main_flag'] = self.main_flag
        if self.main_lm_order_id:
            if hasattr(self.main_lm_order_id, 'to_alipay_dict'):
                params['main_lm_order_id'] = self.main_lm_order_id.to_alipay_dict()
            else:
                params['main_lm_order_id'] = self.main_lm_order_id
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pre_order_status:
            if hasattr(self.pre_order_status, 'to_alipay_dict'):
                params['pre_order_status'] = self.pre_order_status.to_alipay_dict()
            else:
                params['pre_order_status'] = self.pre_order_status
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
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
        o = AlipayMerchantMrchsurplmorderSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'detail_flag' in d:
            o.detail_flag = d['detail_flag']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'lm_order_id' in d:
            o.lm_order_id = d['lm_order_id']
        if 'main_flag' in d:
            o.main_flag = d['main_flag']
        if 'main_lm_order_id' in d:
            o.main_lm_order_id = d['main_lm_order_id']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pre_order_status' in d:
            o.pre_order_status = d['pre_order_status']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


