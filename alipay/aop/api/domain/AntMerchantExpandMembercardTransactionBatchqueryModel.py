#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandMembercardTransactionBatchqueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._end_time = None
        self._member_product_id = None
        self._page_num = None
        self._page_size = None
        self._start_time = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        if isinstance(value, list):
            self._biz_type = list()
            for i in value:
                self._biz_type.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def member_product_id(self):
        return self._member_product_id

    @member_product_id.setter
    def member_product_id(self, value):
        self._member_product_id = value
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
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if isinstance(self.biz_type, list):
                for i in range(0, len(self.biz_type)):
                    element = self.biz_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_type[i] = element.to_alipay_dict()
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.member_product_id:
            if hasattr(self.member_product_id, 'to_alipay_dict'):
                params['member_product_id'] = self.member_product_id.to_alipay_dict()
            else:
                params['member_product_id'] = self.member_product_id
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
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = AntMerchantExpandMembercardTransactionBatchqueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'member_product_id' in d:
            o.member_product_id = d['member_product_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


