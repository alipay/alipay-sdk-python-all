#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorVoucherCancelModel(object):

    def __init__(self):
        self._biz_info_ext = None
        self._city_code = None
        self._operate_time = None
        self._ticket_no = None
        self._trade_no = None

    @property
    def biz_info_ext(self):
        return self._biz_info_ext

    @biz_info_ext.setter
    def biz_info_ext(self, value):
        self._biz_info_ext = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info_ext:
            if hasattr(self.biz_info_ext, 'to_alipay_dict'):
                params['biz_info_ext'] = self.biz_info_ext.to_alipay_dict()
            else:
                params['biz_info_ext'] = self.biz_info_ext
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.ticket_no:
            if hasattr(self.ticket_no, 'to_alipay_dict'):
                params['ticket_no'] = self.ticket_no.to_alipay_dict()
            else:
                params['ticket_no'] = self.ticket_no
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
        o = AlipayCommerceCityfacilitatorVoucherCancelModel()
        if 'biz_info_ext' in d:
            o.biz_info_ext = d['biz_info_ext']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'ticket_no' in d:
            o.ticket_no = d['ticket_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


