#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundAccountBillQueryModel(object):

    def __init__(self):
        self._account_scene_code = None
        self._alipay_user_id = None
        self._bill_begin_time = None
        self._bill_end_time = None
        self._ext_info = None
        self._merchant_user_id = None
        self._page_num = None
        self._page_size = None

    @property
    def account_scene_code(self):
        return self._account_scene_code

    @account_scene_code.setter
    def account_scene_code(self, value):
        self._account_scene_code = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def bill_begin_time(self):
        return self._bill_begin_time

    @bill_begin_time.setter
    def bill_begin_time(self, value):
        self._bill_begin_time = value
    @property
    def bill_end_time(self):
        return self._bill_end_time

    @bill_end_time.setter
    def bill_end_time(self, value):
        self._bill_end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.account_scene_code:
            if hasattr(self.account_scene_code, 'to_alipay_dict'):
                params['account_scene_code'] = self.account_scene_code.to_alipay_dict()
            else:
                params['account_scene_code'] = self.account_scene_code
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.bill_begin_time:
            if hasattr(self.bill_begin_time, 'to_alipay_dict'):
                params['bill_begin_time'] = self.bill_begin_time.to_alipay_dict()
            else:
                params['bill_begin_time'] = self.bill_begin_time
        if self.bill_end_time:
            if hasattr(self.bill_end_time, 'to_alipay_dict'):
                params['bill_end_time'] = self.bill_end_time.to_alipay_dict()
            else:
                params['bill_end_time'] = self.bill_end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundAccountBillQueryModel()
        if 'account_scene_code' in d:
            o.account_scene_code = d['account_scene_code']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'bill_begin_time' in d:
            o.bill_begin_time = d['bill_begin_time']
        if 'bill_end_time' in d:
            o.bill_end_time = d['bill_end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


