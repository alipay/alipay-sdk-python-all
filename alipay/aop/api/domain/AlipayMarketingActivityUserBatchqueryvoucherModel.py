#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivityUserBatchqueryvoucherModel(object):

    def __init__(self):
        self._activity_id = None
        self._belong_merchant_id = None
        self._page_num = None
        self._page_size = None
        self._sender_merchant_id = None
        self._user_id = None
        self._voucher_status = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def belong_merchant_id(self):
        return self._belong_merchant_id

    @belong_merchant_id.setter
    def belong_merchant_id(self, value):
        self._belong_merchant_id = value
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
    def sender_merchant_id(self):
        return self._sender_merchant_id

    @sender_merchant_id.setter
    def sender_merchant_id(self, value):
        self._sender_merchant_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.belong_merchant_id:
            if hasattr(self.belong_merchant_id, 'to_alipay_dict'):
                params['belong_merchant_id'] = self.belong_merchant_id.to_alipay_dict()
            else:
                params['belong_merchant_id'] = self.belong_merchant_id
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
        if self.sender_merchant_id:
            if hasattr(self.sender_merchant_id, 'to_alipay_dict'):
                params['sender_merchant_id'] = self.sender_merchant_id.to_alipay_dict()
            else:
                params['sender_merchant_id'] = self.sender_merchant_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityUserBatchqueryvoucherModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'belong_merchant_id' in d:
            o.belong_merchant_id = d['belong_merchant_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sender_merchant_id' in d:
            o.sender_merchant_id = d['sender_merchant_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        return o


