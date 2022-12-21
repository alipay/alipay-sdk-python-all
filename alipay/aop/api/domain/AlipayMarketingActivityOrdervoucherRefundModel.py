#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherRefundDetailInfo import VoucherRefundDetailInfo


class AlipayMarketingActivityOrdervoucherRefundModel(object):

    def __init__(self):
        self._activity_id = None
        self._biz_dt = None
        self._merchant_access_mode = None
        self._out_biz_no = None
        self._total_fee = None
        self._voucher_code = None
        self._voucher_refund_detail_info = None

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
    def merchant_access_mode(self):
        return self._merchant_access_mode

    @merchant_access_mode.setter
    def merchant_access_mode(self, value):
        self._merchant_access_mode = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value
    @property
    def voucher_code(self):
        return self._voucher_code

    @voucher_code.setter
    def voucher_code(self, value):
        self._voucher_code = value
    @property
    def voucher_refund_detail_info(self):
        return self._voucher_refund_detail_info

    @voucher_refund_detail_info.setter
    def voucher_refund_detail_info(self, value):
        if isinstance(value, VoucherRefundDetailInfo):
            self._voucher_refund_detail_info = value
        else:
            self._voucher_refund_detail_info = VoucherRefundDetailInfo.from_alipay_dict(value)


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
        if self.merchant_access_mode:
            if hasattr(self.merchant_access_mode, 'to_alipay_dict'):
                params['merchant_access_mode'] = self.merchant_access_mode.to_alipay_dict()
            else:
                params['merchant_access_mode'] = self.merchant_access_mode
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.total_fee:
            if hasattr(self.total_fee, 'to_alipay_dict'):
                params['total_fee'] = self.total_fee.to_alipay_dict()
            else:
                params['total_fee'] = self.total_fee
        if self.voucher_code:
            if hasattr(self.voucher_code, 'to_alipay_dict'):
                params['voucher_code'] = self.voucher_code.to_alipay_dict()
            else:
                params['voucher_code'] = self.voucher_code
        if self.voucher_refund_detail_info:
            if hasattr(self.voucher_refund_detail_info, 'to_alipay_dict'):
                params['voucher_refund_detail_info'] = self.voucher_refund_detail_info.to_alipay_dict()
            else:
                params['voucher_refund_detail_info'] = self.voucher_refund_detail_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityOrdervoucherRefundModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'merchant_access_mode' in d:
            o.merchant_access_mode = d['merchant_access_mode']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'total_fee' in d:
            o.total_fee = d['total_fee']
        if 'voucher_code' in d:
            o.voucher_code = d['voucher_code']
        if 'voucher_refund_detail_info' in d:
            o.voucher_refund_detail_info = d['voucher_refund_detail_info']
        return o


