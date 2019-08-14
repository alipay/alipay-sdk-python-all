#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantWeikeBillModifyModel(object):

    def __init__(self):
        self._actual_service_charge = None
        self._alipay_trans_serial_no = None
        self._bill_month = None
        self._bill_no = None
        self._bill_version = None
        self._current_actual_service_charge = None
        self._current_expect_service_charge = None
        self._current_user_task_count = None
        self._expect_service_charge = None
        self._expect_tax = None
        self._gmt_modified = None
        self._gmt_pay = None
        self._out_biz_no = None
        self._paid_charge_tax_include = None
        self._paid_service_charge = None
        self._service_charge_serial_no = None
        self._to_pay_service_charge = None
        self._weike_user_id = None

    @property
    def actual_service_charge(self):
        return self._actual_service_charge

    @actual_service_charge.setter
    def actual_service_charge(self, value):
        self._actual_service_charge = value
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
    def current_actual_service_charge(self):
        return self._current_actual_service_charge

    @current_actual_service_charge.setter
    def current_actual_service_charge(self, value):
        self._current_actual_service_charge = value
    @property
    def current_expect_service_charge(self):
        return self._current_expect_service_charge

    @current_expect_service_charge.setter
    def current_expect_service_charge(self, value):
        self._current_expect_service_charge = value
    @property
    def current_user_task_count(self):
        return self._current_user_task_count

    @current_user_task_count.setter
    def current_user_task_count(self, value):
        self._current_user_task_count = value
    @property
    def expect_service_charge(self):
        return self._expect_service_charge

    @expect_service_charge.setter
    def expect_service_charge(self, value):
        self._expect_service_charge = value
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
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def paid_charge_tax_include(self):
        return self._paid_charge_tax_include

    @paid_charge_tax_include.setter
    def paid_charge_tax_include(self, value):
        self._paid_charge_tax_include = value
    @property
    def paid_service_charge(self):
        return self._paid_service_charge

    @paid_service_charge.setter
    def paid_service_charge(self, value):
        self._paid_service_charge = value
    @property
    def service_charge_serial_no(self):
        return self._service_charge_serial_no

    @service_charge_serial_no.setter
    def service_charge_serial_no(self, value):
        self._service_charge_serial_no = value
    @property
    def to_pay_service_charge(self):
        return self._to_pay_service_charge

    @to_pay_service_charge.setter
    def to_pay_service_charge(self, value):
        self._to_pay_service_charge = value
    @property
    def weike_user_id(self):
        return self._weike_user_id

    @weike_user_id.setter
    def weike_user_id(self, value):
        self._weike_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_service_charge:
            if hasattr(self.actual_service_charge, 'to_alipay_dict'):
                params['actual_service_charge'] = self.actual_service_charge.to_alipay_dict()
            else:
                params['actual_service_charge'] = self.actual_service_charge
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
        if self.current_actual_service_charge:
            if hasattr(self.current_actual_service_charge, 'to_alipay_dict'):
                params['current_actual_service_charge'] = self.current_actual_service_charge.to_alipay_dict()
            else:
                params['current_actual_service_charge'] = self.current_actual_service_charge
        if self.current_expect_service_charge:
            if hasattr(self.current_expect_service_charge, 'to_alipay_dict'):
                params['current_expect_service_charge'] = self.current_expect_service_charge.to_alipay_dict()
            else:
                params['current_expect_service_charge'] = self.current_expect_service_charge
        if self.current_user_task_count:
            if hasattr(self.current_user_task_count, 'to_alipay_dict'):
                params['current_user_task_count'] = self.current_user_task_count.to_alipay_dict()
            else:
                params['current_user_task_count'] = self.current_user_task_count
        if self.expect_service_charge:
            if hasattr(self.expect_service_charge, 'to_alipay_dict'):
                params['expect_service_charge'] = self.expect_service_charge.to_alipay_dict()
            else:
                params['expect_service_charge'] = self.expect_service_charge
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
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.paid_charge_tax_include:
            if hasattr(self.paid_charge_tax_include, 'to_alipay_dict'):
                params['paid_charge_tax_include'] = self.paid_charge_tax_include.to_alipay_dict()
            else:
                params['paid_charge_tax_include'] = self.paid_charge_tax_include
        if self.paid_service_charge:
            if hasattr(self.paid_service_charge, 'to_alipay_dict'):
                params['paid_service_charge'] = self.paid_service_charge.to_alipay_dict()
            else:
                params['paid_service_charge'] = self.paid_service_charge
        if self.service_charge_serial_no:
            if hasattr(self.service_charge_serial_no, 'to_alipay_dict'):
                params['service_charge_serial_no'] = self.service_charge_serial_no.to_alipay_dict()
            else:
                params['service_charge_serial_no'] = self.service_charge_serial_no
        if self.to_pay_service_charge:
            if hasattr(self.to_pay_service_charge, 'to_alipay_dict'):
                params['to_pay_service_charge'] = self.to_pay_service_charge.to_alipay_dict()
            else:
                params['to_pay_service_charge'] = self.to_pay_service_charge
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
        o = AlipayMerchantWeikeBillModifyModel()
        if 'actual_service_charge' in d:
            o.actual_service_charge = d['actual_service_charge']
        if 'alipay_trans_serial_no' in d:
            o.alipay_trans_serial_no = d['alipay_trans_serial_no']
        if 'bill_month' in d:
            o.bill_month = d['bill_month']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_version' in d:
            o.bill_version = d['bill_version']
        if 'current_actual_service_charge' in d:
            o.current_actual_service_charge = d['current_actual_service_charge']
        if 'current_expect_service_charge' in d:
            o.current_expect_service_charge = d['current_expect_service_charge']
        if 'current_user_task_count' in d:
            o.current_user_task_count = d['current_user_task_count']
        if 'expect_service_charge' in d:
            o.expect_service_charge = d['expect_service_charge']
        if 'expect_tax' in d:
            o.expect_tax = d['expect_tax']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'paid_charge_tax_include' in d:
            o.paid_charge_tax_include = d['paid_charge_tax_include']
        if 'paid_service_charge' in d:
            o.paid_service_charge = d['paid_service_charge']
        if 'service_charge_serial_no' in d:
            o.service_charge_serial_no = d['service_charge_serial_no']
        if 'to_pay_service_charge' in d:
            o.to_pay_service_charge = d['to_pay_service_charge']
        if 'weike_user_id' in d:
            o.weike_user_id = d['weike_user_id']
        return o


