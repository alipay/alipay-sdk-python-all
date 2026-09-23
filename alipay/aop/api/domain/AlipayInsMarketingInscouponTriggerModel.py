#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KeyValueDTO import KeyValueDTO
from alipay.aop.api.domain.InsCouponInfo import InsCouponInfo


class AlipayInsMarketingInscouponTriggerModel(object):

    def __init__(self):
        self._ext_params = None
        self._ins_coupon = None
        self._open_id = None
        self._out_biz_no = None
        self._trigger_time = None
        self._trigger_type = None
        self._user_id = None

    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        if isinstance(value, list):
            self._ext_params = list()
            for i in value:
                if isinstance(i, KeyValueDTO):
                    self._ext_params.append(i)
                else:
                    self._ext_params.append(KeyValueDTO.from_alipay_dict(i))
    @property
    def ins_coupon(self):
        return self._ins_coupon

    @ins_coupon.setter
    def ins_coupon(self, value):
        if isinstance(value, InsCouponInfo):
            self._ins_coupon = value
        else:
            self._ins_coupon = InsCouponInfo.from_alipay_dict(value)
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
    def trigger_time(self):
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, value):
        self._trigger_time = value
    @property
    def trigger_type(self):
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, value):
        self._trigger_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_params:
            if isinstance(self.ext_params, list):
                for i in range(0, len(self.ext_params)):
                    element = self.ext_params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_params[i] = element.to_alipay_dict()
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.ins_coupon:
            if hasattr(self.ins_coupon, 'to_alipay_dict'):
                params['ins_coupon'] = self.ins_coupon.to_alipay_dict()
            else:
                params['ins_coupon'] = self.ins_coupon
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
        if self.trigger_time:
            if hasattr(self.trigger_time, 'to_alipay_dict'):
                params['trigger_time'] = self.trigger_time.to_alipay_dict()
            else:
                params['trigger_time'] = self.trigger_time
        if self.trigger_type:
            if hasattr(self.trigger_type, 'to_alipay_dict'):
                params['trigger_type'] = self.trigger_type.to_alipay_dict()
            else:
                params['trigger_type'] = self.trigger_type
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
        o = AlipayInsMarketingInscouponTriggerModel()
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'ins_coupon' in d:
            o.ins_coupon = d['ins_coupon']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trigger_time' in d:
            o.trigger_time = d['trigger_time']
        if 'trigger_type' in d:
            o.trigger_type = d['trigger_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


