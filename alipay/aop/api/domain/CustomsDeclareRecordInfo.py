#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomsDeclareRecordInfo(object):

    def __init__(self):
        self._alipay_declare_no = None
        self._amount = None
        self._customs_place = None
        self._customs_result_code = None
        self._customs_result_info = None
        self._customs_result_return_time = None
        self._is_split = None
        self._last_modified_time = None
        self._memo = None
        self._merchant_customs_code = None
        self._merchant_customs_name = None
        self._out_request_no = None
        self._status = None
        self._sub_out_biz_no = None
        self._trade_no = None

    @property
    def alipay_declare_no(self):
        return self._alipay_declare_no

    @alipay_declare_no.setter
    def alipay_declare_no(self, value):
        self._alipay_declare_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def customs_place(self):
        return self._customs_place

    @customs_place.setter
    def customs_place(self, value):
        self._customs_place = value
    @property
    def customs_result_code(self):
        return self._customs_result_code

    @customs_result_code.setter
    def customs_result_code(self, value):
        self._customs_result_code = value
    @property
    def customs_result_info(self):
        return self._customs_result_info

    @customs_result_info.setter
    def customs_result_info(self, value):
        self._customs_result_info = value
    @property
    def customs_result_return_time(self):
        return self._customs_result_return_time

    @customs_result_return_time.setter
    def customs_result_return_time(self, value):
        self._customs_result_return_time = value
    @property
    def is_split(self):
        return self._is_split

    @is_split.setter
    def is_split(self, value):
        self._is_split = value
    @property
    def last_modified_time(self):
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, value):
        self._last_modified_time = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_customs_code(self):
        return self._merchant_customs_code

    @merchant_customs_code.setter
    def merchant_customs_code(self, value):
        self._merchant_customs_code = value
    @property
    def merchant_customs_name(self):
        return self._merchant_customs_name

    @merchant_customs_name.setter
    def merchant_customs_name(self, value):
        self._merchant_customs_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_out_biz_no(self):
        return self._sub_out_biz_no

    @sub_out_biz_no.setter
    def sub_out_biz_no(self, value):
        self._sub_out_biz_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_declare_no:
            if hasattr(self.alipay_declare_no, 'to_alipay_dict'):
                params['alipay_declare_no'] = self.alipay_declare_no.to_alipay_dict()
            else:
                params['alipay_declare_no'] = self.alipay_declare_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.customs_place:
            if hasattr(self.customs_place, 'to_alipay_dict'):
                params['customs_place'] = self.customs_place.to_alipay_dict()
            else:
                params['customs_place'] = self.customs_place
        if self.customs_result_code:
            if hasattr(self.customs_result_code, 'to_alipay_dict'):
                params['customs_result_code'] = self.customs_result_code.to_alipay_dict()
            else:
                params['customs_result_code'] = self.customs_result_code
        if self.customs_result_info:
            if hasattr(self.customs_result_info, 'to_alipay_dict'):
                params['customs_result_info'] = self.customs_result_info.to_alipay_dict()
            else:
                params['customs_result_info'] = self.customs_result_info
        if self.customs_result_return_time:
            if hasattr(self.customs_result_return_time, 'to_alipay_dict'):
                params['customs_result_return_time'] = self.customs_result_return_time.to_alipay_dict()
            else:
                params['customs_result_return_time'] = self.customs_result_return_time
        if self.is_split:
            if hasattr(self.is_split, 'to_alipay_dict'):
                params['is_split'] = self.is_split.to_alipay_dict()
            else:
                params['is_split'] = self.is_split
        if self.last_modified_time:
            if hasattr(self.last_modified_time, 'to_alipay_dict'):
                params['last_modified_time'] = self.last_modified_time.to_alipay_dict()
            else:
                params['last_modified_time'] = self.last_modified_time
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_customs_code:
            if hasattr(self.merchant_customs_code, 'to_alipay_dict'):
                params['merchant_customs_code'] = self.merchant_customs_code.to_alipay_dict()
            else:
                params['merchant_customs_code'] = self.merchant_customs_code
        if self.merchant_customs_name:
            if hasattr(self.merchant_customs_name, 'to_alipay_dict'):
                params['merchant_customs_name'] = self.merchant_customs_name.to_alipay_dict()
            else:
                params['merchant_customs_name'] = self.merchant_customs_name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_out_biz_no:
            if hasattr(self.sub_out_biz_no, 'to_alipay_dict'):
                params['sub_out_biz_no'] = self.sub_out_biz_no.to_alipay_dict()
            else:
                params['sub_out_biz_no'] = self.sub_out_biz_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomsDeclareRecordInfo()
        if 'alipay_declare_no' in d:
            o.alipay_declare_no = d['alipay_declare_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'customs_place' in d:
            o.customs_place = d['customs_place']
        if 'customs_result_code' in d:
            o.customs_result_code = d['customs_result_code']
        if 'customs_result_info' in d:
            o.customs_result_info = d['customs_result_info']
        if 'customs_result_return_time' in d:
            o.customs_result_return_time = d['customs_result_return_time']
        if 'is_split' in d:
            o.is_split = d['is_split']
        if 'last_modified_time' in d:
            o.last_modified_time = d['last_modified_time']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_customs_code' in d:
            o.merchant_customs_code = d['merchant_customs_code']
        if 'merchant_customs_name' in d:
            o.merchant_customs_name = d['merchant_customs_name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'status' in d:
            o.status = d['status']
        if 'sub_out_biz_no' in d:
            o.sub_out_biz_no = d['sub_out_biz_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


