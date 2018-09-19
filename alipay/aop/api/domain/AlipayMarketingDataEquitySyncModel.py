#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EquityInfo import EquityInfo


class AlipayMarketingDataEquitySyncModel(object):

    def __init__(self):
        self._biz_time = None
        self._equity_code = None
        self._equity_from = None
        self._equity_id = None
        self._equity_info = None
        self._original_biz_no = None
        self._original_biz_type = None
        self._out_biz_no = None
        self._user_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def equity_code(self):
        return self._equity_code

    @equity_code.setter
    def equity_code(self, value):
        self._equity_code = value
    @property
    def equity_from(self):
        return self._equity_from

    @equity_from.setter
    def equity_from(self, value):
        self._equity_from = value
    @property
    def equity_id(self):
        return self._equity_id

    @equity_id.setter
    def equity_id(self, value):
        self._equity_id = value
    @property
    def equity_info(self):
        return self._equity_info

    @equity_info.setter
    def equity_info(self, value):
        if isinstance(value, EquityInfo):
            self._equity_info = value
        else:
            self._equity_info = EquityInfo.from_alipay_dict(value)
    @property
    def original_biz_no(self):
        return self._original_biz_no

    @original_biz_no.setter
    def original_biz_no(self, value):
        self._original_biz_no = value
    @property
    def original_biz_type(self):
        return self._original_biz_type

    @original_biz_type.setter
    def original_biz_type(self, value):
        self._original_biz_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.equity_code:
            if hasattr(self.equity_code, 'to_alipay_dict'):
                params['equity_code'] = self.equity_code.to_alipay_dict()
            else:
                params['equity_code'] = self.equity_code
        if self.equity_from:
            if hasattr(self.equity_from, 'to_alipay_dict'):
                params['equity_from'] = self.equity_from.to_alipay_dict()
            else:
                params['equity_from'] = self.equity_from
        if self.equity_id:
            if hasattr(self.equity_id, 'to_alipay_dict'):
                params['equity_id'] = self.equity_id.to_alipay_dict()
            else:
                params['equity_id'] = self.equity_id
        if self.equity_info:
            if hasattr(self.equity_info, 'to_alipay_dict'):
                params['equity_info'] = self.equity_info.to_alipay_dict()
            else:
                params['equity_info'] = self.equity_info
        if self.original_biz_no:
            if hasattr(self.original_biz_no, 'to_alipay_dict'):
                params['original_biz_no'] = self.original_biz_no.to_alipay_dict()
            else:
                params['original_biz_no'] = self.original_biz_no
        if self.original_biz_type:
            if hasattr(self.original_biz_type, 'to_alipay_dict'):
                params['original_biz_type'] = self.original_biz_type.to_alipay_dict()
            else:
                params['original_biz_type'] = self.original_biz_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayMarketingDataEquitySyncModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'equity_code' in d:
            o.equity_code = d['equity_code']
        if 'equity_from' in d:
            o.equity_from = d['equity_from']
        if 'equity_id' in d:
            o.equity_id = d['equity_id']
        if 'equity_info' in d:
            o.equity_info = d['equity_info']
        if 'original_biz_no' in d:
            o.original_biz_no = d['original_biz_no']
        if 'original_biz_type' in d:
            o.original_biz_type = d['original_biz_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


