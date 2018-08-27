#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoServiceCouponVerifyModel(object):

    def __init__(self):
        self._biz_data = None
        self._coupon_id = None
        self._event = None
        self._event_date = None
        self._out_biz_no = None
        self._sp_coupon_id = None
        self._user_id = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def coupon_id(self):
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self._coupon_id = value
    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value
    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, value):
        self._event_date = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sp_coupon_id(self):
        return self._sp_coupon_id

    @sp_coupon_id.setter
    def sp_coupon_id(self, value):
        self._sp_coupon_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.coupon_id:
            if hasattr(self.coupon_id, 'to_alipay_dict'):
                params['coupon_id'] = self.coupon_id.to_alipay_dict()
            else:
                params['coupon_id'] = self.coupon_id
        if self.event:
            if hasattr(self.event, 'to_alipay_dict'):
                params['event'] = self.event.to_alipay_dict()
            else:
                params['event'] = self.event
        if self.event_date:
            if hasattr(self.event_date, 'to_alipay_dict'):
                params['event_date'] = self.event_date.to_alipay_dict()
            else:
                params['event_date'] = self.event_date
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sp_coupon_id:
            if hasattr(self.sp_coupon_id, 'to_alipay_dict'):
                params['sp_coupon_id'] = self.sp_coupon_id.to_alipay_dict()
            else:
                params['sp_coupon_id'] = self.sp_coupon_id
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
        o = AlipayInsAutoServiceCouponVerifyModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'coupon_id' in d:
            o.coupon_id = d['coupon_id']
        if 'event' in d:
            o.event = d['event']
        if 'event_date' in d:
            o.event_date = d['event_date']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sp_coupon_id' in d:
            o.sp_coupon_id = d['sp_coupon_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


