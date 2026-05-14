#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderVoucherReceiveInfo(object):

    def __init__(self):
        self._activity_id = None
        self._customize_send_time = None
        self._out_biz_no = None
        self._voucher_code = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def customize_send_time(self):
        return self._customize_send_time

    @customize_send_time.setter
    def customize_send_time(self, value):
        self._customize_send_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def voucher_code(self):
        return self._voucher_code

    @voucher_code.setter
    def voucher_code(self, value):
        self._voucher_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.customize_send_time:
            if hasattr(self.customize_send_time, 'to_alipay_dict'):
                params['customize_send_time'] = self.customize_send_time.to_alipay_dict()
            else:
                params['customize_send_time'] = self.customize_send_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.voucher_code:
            if hasattr(self.voucher_code, 'to_alipay_dict'):
                params['voucher_code'] = self.voucher_code.to_alipay_dict()
            else:
                params['voucher_code'] = self.voucher_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVoucherReceiveInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'customize_send_time' in d:
            o.customize_send_time = d['customize_send_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'voucher_code' in d:
            o.voucher_code = d['voucher_code']
        return o


