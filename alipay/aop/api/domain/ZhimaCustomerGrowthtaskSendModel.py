#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerGrowthtaskSendModel(object):

    def __init__(self):
        self._biz_date = None
        self._biz_inc_value = None
        self._cert_no = None
        self._cert_type = None
        self._open_id = None
        self._out_biz_no = None
        self._outer_id = None
        self._push_record_id = None
        self._user_id = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_inc_value(self):
        return self._biz_inc_value

    @biz_inc_value.setter
    def biz_inc_value(self, value):
        self._biz_inc_value = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, value):
        self._outer_id = value
    @property
    def push_record_id(self):
        return self._push_record_id

    @push_record_id.setter
    def push_record_id(self, value):
        self._push_record_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_inc_value:
            if hasattr(self.biz_inc_value, 'to_alipay_dict'):
                params['biz_inc_value'] = self.biz_inc_value.to_alipay_dict()
            else:
                params['biz_inc_value'] = self.biz_inc_value
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.outer_id:
            if hasattr(self.outer_id, 'to_alipay_dict'):
                params['outer_id'] = self.outer_id.to_alipay_dict()
            else:
                params['outer_id'] = self.outer_id
        if self.push_record_id:
            if hasattr(self.push_record_id, 'to_alipay_dict'):
                params['push_record_id'] = self.push_record_id.to_alipay_dict()
            else:
                params['push_record_id'] = self.push_record_id
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
        o = ZhimaCustomerGrowthtaskSendModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_inc_value' in d:
            o.biz_inc_value = d['biz_inc_value']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'outer_id' in d:
            o.outer_id = d['outer_id']
        if 'push_record_id' in d:
            o.push_record_id = d['push_record_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


