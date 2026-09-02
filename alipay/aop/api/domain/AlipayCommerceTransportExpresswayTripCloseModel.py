#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportExpresswayTripCloseModel(object):

    def __init__(self):
        self._biz_agreement_no = None
        self._open_id = None
        self._out_trip_id = None
        self._reverse_reason = None
        self._user_id = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trip_id(self):
        return self._out_trip_id

    @out_trip_id.setter
    def out_trip_id(self, value):
        self._out_trip_id = value
    @property
    def reverse_reason(self):
        return self._reverse_reason

    @reverse_reason.setter
    def reverse_reason(self, value):
        self._reverse_reason = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_trip_id:
            if hasattr(self.out_trip_id, 'to_alipay_dict'):
                params['out_trip_id'] = self.out_trip_id.to_alipay_dict()
            else:
                params['out_trip_id'] = self.out_trip_id
        if self.reverse_reason:
            if hasattr(self.reverse_reason, 'to_alipay_dict'):
                params['reverse_reason'] = self.reverse_reason.to_alipay_dict()
            else:
                params['reverse_reason'] = self.reverse_reason
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
        o = AlipayCommerceTransportExpresswayTripCloseModel()
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_trip_id' in d:
            o.out_trip_id = d['out_trip_id']
        if 'reverse_reason' in d:
            o.reverse_reason = d['reverse_reason']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


