#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserBillTaxDetail(object):

    def __init__(self):
        self._alipay_uid = None
        self._amount_tax = None
        self._bill_city_tax = None
        self._bill_edu_tax = None
        self._bill_iit_tax = None
        self._bill_local_edu_tax = None
        self._bill_vat_tax = None
        self._open_id = None
        self._tax_fail_reason = None
        self._tax_status = None
        self._user_bill_no = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def amount_tax(self):
        return self._amount_tax

    @amount_tax.setter
    def amount_tax(self, value):
        self._amount_tax = value
    @property
    def bill_city_tax(self):
        return self._bill_city_tax

    @bill_city_tax.setter
    def bill_city_tax(self, value):
        self._bill_city_tax = value
    @property
    def bill_edu_tax(self):
        return self._bill_edu_tax

    @bill_edu_tax.setter
    def bill_edu_tax(self, value):
        self._bill_edu_tax = value
    @property
    def bill_iit_tax(self):
        return self._bill_iit_tax

    @bill_iit_tax.setter
    def bill_iit_tax(self, value):
        self._bill_iit_tax = value
    @property
    def bill_local_edu_tax(self):
        return self._bill_local_edu_tax

    @bill_local_edu_tax.setter
    def bill_local_edu_tax(self, value):
        self._bill_local_edu_tax = value
    @property
    def bill_vat_tax(self):
        return self._bill_vat_tax

    @bill_vat_tax.setter
    def bill_vat_tax(self, value):
        self._bill_vat_tax = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def tax_fail_reason(self):
        return self._tax_fail_reason

    @tax_fail_reason.setter
    def tax_fail_reason(self, value):
        self._tax_fail_reason = value
    @property
    def tax_status(self):
        return self._tax_status

    @tax_status.setter
    def tax_status(self, value):
        self._tax_status = value
    @property
    def user_bill_no(self):
        return self._user_bill_no

    @user_bill_no.setter
    def user_bill_no(self, value):
        self._user_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.amount_tax:
            if hasattr(self.amount_tax, 'to_alipay_dict'):
                params['amount_tax'] = self.amount_tax.to_alipay_dict()
            else:
                params['amount_tax'] = self.amount_tax
        if self.bill_city_tax:
            if hasattr(self.bill_city_tax, 'to_alipay_dict'):
                params['bill_city_tax'] = self.bill_city_tax.to_alipay_dict()
            else:
                params['bill_city_tax'] = self.bill_city_tax
        if self.bill_edu_tax:
            if hasattr(self.bill_edu_tax, 'to_alipay_dict'):
                params['bill_edu_tax'] = self.bill_edu_tax.to_alipay_dict()
            else:
                params['bill_edu_tax'] = self.bill_edu_tax
        if self.bill_iit_tax:
            if hasattr(self.bill_iit_tax, 'to_alipay_dict'):
                params['bill_iit_tax'] = self.bill_iit_tax.to_alipay_dict()
            else:
                params['bill_iit_tax'] = self.bill_iit_tax
        if self.bill_local_edu_tax:
            if hasattr(self.bill_local_edu_tax, 'to_alipay_dict'):
                params['bill_local_edu_tax'] = self.bill_local_edu_tax.to_alipay_dict()
            else:
                params['bill_local_edu_tax'] = self.bill_local_edu_tax
        if self.bill_vat_tax:
            if hasattr(self.bill_vat_tax, 'to_alipay_dict'):
                params['bill_vat_tax'] = self.bill_vat_tax.to_alipay_dict()
            else:
                params['bill_vat_tax'] = self.bill_vat_tax
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.tax_fail_reason:
            if hasattr(self.tax_fail_reason, 'to_alipay_dict'):
                params['tax_fail_reason'] = self.tax_fail_reason.to_alipay_dict()
            else:
                params['tax_fail_reason'] = self.tax_fail_reason
        if self.tax_status:
            if hasattr(self.tax_status, 'to_alipay_dict'):
                params['tax_status'] = self.tax_status.to_alipay_dict()
            else:
                params['tax_status'] = self.tax_status
        if self.user_bill_no:
            if hasattr(self.user_bill_no, 'to_alipay_dict'):
                params['user_bill_no'] = self.user_bill_no.to_alipay_dict()
            else:
                params['user_bill_no'] = self.user_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserBillTaxDetail()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'amount_tax' in d:
            o.amount_tax = d['amount_tax']
        if 'bill_city_tax' in d:
            o.bill_city_tax = d['bill_city_tax']
        if 'bill_edu_tax' in d:
            o.bill_edu_tax = d['bill_edu_tax']
        if 'bill_iit_tax' in d:
            o.bill_iit_tax = d['bill_iit_tax']
        if 'bill_local_edu_tax' in d:
            o.bill_local_edu_tax = d['bill_local_edu_tax']
        if 'bill_vat_tax' in d:
            o.bill_vat_tax = d['bill_vat_tax']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'tax_fail_reason' in d:
            o.tax_fail_reason = d['tax_fail_reason']
        if 'tax_status' in d:
            o.tax_status = d['tax_status']
        if 'user_bill_no' in d:
            o.user_bill_no = d['user_bill_no']
        return o


