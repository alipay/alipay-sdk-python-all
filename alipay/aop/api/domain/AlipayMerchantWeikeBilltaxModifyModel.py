#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantWeikeBilltaxModifyModel(object):

    def __init__(self):
        self._actual_tax = None
        self._alipay_trans_serial_no = None
        self._bill_month = None
        self._bill_no = None
        self._bill_version = None
        self._expect_tax = None
        self._gmt_modified = None
        self._out_biz_no = None
        self._tax_rebate = None
        self._tax_rebate_gmt_pay = None
        self._tax_rebate_serial_no = None
        self._weike_user_id = None

    @property
    def actual_tax(self):
        return self._actual_tax

    @actual_tax.setter
    def actual_tax(self, value):
        self._actual_tax = value
    @property
    def alipay_trans_serial_no(self):
        return self._alipay_trans_serial_no

    @alipay_trans_serial_no.setter
    def alipay_trans_serial_no(self, value):
        self._alipay_trans_serial_no = value
    @property
    def bill_month(self):
        return self._bill_month

    @bill_month.setter
    def bill_month(self, value):
        self._bill_month = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_version(self):
        return self._bill_version

    @bill_version.setter
    def bill_version(self, value):
        self._bill_version = value
    @property
    def expect_tax(self):
        return self._expect_tax

    @expect_tax.setter
    def expect_tax(self, value):
        self._expect_tax = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def tax_rebate(self):
        return self._tax_rebate

    @tax_rebate.setter
    def tax_rebate(self, value):
        self._tax_rebate = value
    @property
    def tax_rebate_gmt_pay(self):
        return self._tax_rebate_gmt_pay

    @tax_rebate_gmt_pay.setter
    def tax_rebate_gmt_pay(self, value):
        self._tax_rebate_gmt_pay = value
    @property
    def tax_rebate_serial_no(self):
        return self._tax_rebate_serial_no

    @tax_rebate_serial_no.setter
    def tax_rebate_serial_no(self, value):
        self._tax_rebate_serial_no = value
    @property
    def weike_user_id(self):
        return self._weike_user_id

    @weike_user_id.setter
    def weike_user_id(self, value):
        self._weike_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_tax:
            if hasattr(self.actual_tax, 'to_alipay_dict'):
                params['actual_tax'] = self.actual_tax.to_alipay_dict()
            else:
                params['actual_tax'] = self.actual_tax
        if self.alipay_trans_serial_no:
            if hasattr(self.alipay_trans_serial_no, 'to_alipay_dict'):
                params['alipay_trans_serial_no'] = self.alipay_trans_serial_no.to_alipay_dict()
            else:
                params['alipay_trans_serial_no'] = self.alipay_trans_serial_no
        if self.bill_month:
            if hasattr(self.bill_month, 'to_alipay_dict'):
                params['bill_month'] = self.bill_month.to_alipay_dict()
            else:
                params['bill_month'] = self.bill_month
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_version:
            if hasattr(self.bill_version, 'to_alipay_dict'):
                params['bill_version'] = self.bill_version.to_alipay_dict()
            else:
                params['bill_version'] = self.bill_version
        if self.expect_tax:
            if hasattr(self.expect_tax, 'to_alipay_dict'):
                params['expect_tax'] = self.expect_tax.to_alipay_dict()
            else:
                params['expect_tax'] = self.expect_tax
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.tax_rebate:
            if hasattr(self.tax_rebate, 'to_alipay_dict'):
                params['tax_rebate'] = self.tax_rebate.to_alipay_dict()
            else:
                params['tax_rebate'] = self.tax_rebate
        if self.tax_rebate_gmt_pay:
            if hasattr(self.tax_rebate_gmt_pay, 'to_alipay_dict'):
                params['tax_rebate_gmt_pay'] = self.tax_rebate_gmt_pay.to_alipay_dict()
            else:
                params['tax_rebate_gmt_pay'] = self.tax_rebate_gmt_pay
        if self.tax_rebate_serial_no:
            if hasattr(self.tax_rebate_serial_no, 'to_alipay_dict'):
                params['tax_rebate_serial_no'] = self.tax_rebate_serial_no.to_alipay_dict()
            else:
                params['tax_rebate_serial_no'] = self.tax_rebate_serial_no
        if self.weike_user_id:
            if hasattr(self.weike_user_id, 'to_alipay_dict'):
                params['weike_user_id'] = self.weike_user_id.to_alipay_dict()
            else:
                params['weike_user_id'] = self.weike_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantWeikeBilltaxModifyModel()
        if 'actual_tax' in d:
            o.actual_tax = d['actual_tax']
        if 'alipay_trans_serial_no' in d:
            o.alipay_trans_serial_no = d['alipay_trans_serial_no']
        if 'bill_month' in d:
            o.bill_month = d['bill_month']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_version' in d:
            o.bill_version = d['bill_version']
        if 'expect_tax' in d:
            o.expect_tax = d['expect_tax']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'tax_rebate' in d:
            o.tax_rebate = d['tax_rebate']
        if 'tax_rebate_gmt_pay' in d:
            o.tax_rebate_gmt_pay = d['tax_rebate_gmt_pay']
        if 'tax_rebate_serial_no' in d:
            o.tax_rebate_serial_no = d['tax_rebate_serial_no']
        if 'weike_user_id' in d:
            o.weike_user_id = d['weike_user_id']
        return o


