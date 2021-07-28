#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivityOrdervoucherInvalidModel(object):

    def __init__(self):
        self._activity_id = None
        self._biz_dt = None
        self._out_biz_no = None
        self._voucher_code = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def biz_dt(self):
        return self._biz_dt

    @biz_dt.setter
    def biz_dt(self, value):
        self._biz_dt = value
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
        if self.biz_dt:
            if hasattr(self.biz_dt, 'to_alipay_dict'):
                params['biz_dt'] = self.biz_dt.to_alipay_dict()
            else:
                params['biz_dt'] = self.biz_dt
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
        o = AlipayMarketingActivityOrdervoucherInvalidModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'voucher_code' in d:
            o.voucher_code = d['voucher_code']
        return o


