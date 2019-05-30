#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserVo import UserVo


class MybankCreditLoantradeBillListQueryModel(object):

    def __init__(self):
        self._bill_status_list = None
        self._end_date = None
        self._out_request_no = None
        self._page_num = None
        self._page_size = None
        self._product_code = None
        self._start_date = None
        self._user = None

    @property
    def bill_status_list(self):
        return self._bill_status_list

    @bill_status_list.setter
    def bill_status_list(self, value):
        self._bill_status_list = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
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
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, UserVo):
            self._user = value
        else:
            self._user = UserVo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_status_list:
            if hasattr(self.bill_status_list, 'to_alipay_dict'):
                params['bill_status_list'] = self.bill_status_list.to_alipay_dict()
            else:
                params['bill_status_list'] = self.bill_status_list
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
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
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeBillListQueryModel()
        if 'bill_status_list' in d:
            o.bill_status_list = d['bill_status_list']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'user' in d:
            o.user = d['user']
        return o


