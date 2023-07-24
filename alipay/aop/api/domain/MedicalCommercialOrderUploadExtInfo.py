#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalCommercialOrderUploadAmountDetail import MedicalCommercialOrderUploadAmountDetail
from alipay.aop.api.domain.MedicalCommercialOrderUploadAmountDetail import MedicalCommercialOrderUploadAmountDetail


class MedicalCommercialOrderUploadExtInfo(object):

    def __init__(self):
        self._expense_details = None
        self._medical_examination_user = None
        self._mrch_pid = None
        self._refund_amount = None
        self._refund_note = None
        self._report_url = None
        self._store_address = None
        self._store_name = None
        self._write_off_details = None

    @property
    def expense_details(self):
        return self._expense_details

    @expense_details.setter
    def expense_details(self, value):
        if isinstance(value, list):
            self._expense_details = list()
            for i in value:
                if isinstance(i, MedicalCommercialOrderUploadAmountDetail):
                    self._expense_details.append(i)
                else:
                    self._expense_details.append(MedicalCommercialOrderUploadAmountDetail.from_alipay_dict(i))
    @property
    def medical_examination_user(self):
        return self._medical_examination_user

    @medical_examination_user.setter
    def medical_examination_user(self, value):
        self._medical_examination_user = value
    @property
    def mrch_pid(self):
        return self._mrch_pid

    @mrch_pid.setter
    def mrch_pid(self, value):
        self._mrch_pid = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_note(self):
        return self._refund_note

    @refund_note.setter
    def refund_note(self, value):
        self._refund_note = value
    @property
    def report_url(self):
        return self._report_url

    @report_url.setter
    def report_url(self, value):
        self._report_url = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def write_off_details(self):
        return self._write_off_details

    @write_off_details.setter
    def write_off_details(self, value):
        if isinstance(value, list):
            self._write_off_details = list()
            for i in value:
                if isinstance(i, MedicalCommercialOrderUploadAmountDetail):
                    self._write_off_details.append(i)
                else:
                    self._write_off_details.append(MedicalCommercialOrderUploadAmountDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.expense_details:
            if isinstance(self.expense_details, list):
                for i in range(0, len(self.expense_details)):
                    element = self.expense_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expense_details[i] = element.to_alipay_dict()
            if hasattr(self.expense_details, 'to_alipay_dict'):
                params['expense_details'] = self.expense_details.to_alipay_dict()
            else:
                params['expense_details'] = self.expense_details
        if self.medical_examination_user:
            if hasattr(self.medical_examination_user, 'to_alipay_dict'):
                params['medical_examination_user'] = self.medical_examination_user.to_alipay_dict()
            else:
                params['medical_examination_user'] = self.medical_examination_user
        if self.mrch_pid:
            if hasattr(self.mrch_pid, 'to_alipay_dict'):
                params['mrch_pid'] = self.mrch_pid.to_alipay_dict()
            else:
                params['mrch_pid'] = self.mrch_pid
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_note:
            if hasattr(self.refund_note, 'to_alipay_dict'):
                params['refund_note'] = self.refund_note.to_alipay_dict()
            else:
                params['refund_note'] = self.refund_note
        if self.report_url:
            if hasattr(self.report_url, 'to_alipay_dict'):
                params['report_url'] = self.report_url.to_alipay_dict()
            else:
                params['report_url'] = self.report_url
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.write_off_details:
            if isinstance(self.write_off_details, list):
                for i in range(0, len(self.write_off_details)):
                    element = self.write_off_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.write_off_details[i] = element.to_alipay_dict()
            if hasattr(self.write_off_details, 'to_alipay_dict'):
                params['write_off_details'] = self.write_off_details.to_alipay_dict()
            else:
                params['write_off_details'] = self.write_off_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalCommercialOrderUploadExtInfo()
        if 'expense_details' in d:
            o.expense_details = d['expense_details']
        if 'medical_examination_user' in d:
            o.medical_examination_user = d['medical_examination_user']
        if 'mrch_pid' in d:
            o.mrch_pid = d['mrch_pid']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_note' in d:
            o.refund_note = d['refund_note']
        if 'report_url' in d:
            o.report_url = d['report_url']
        if 'store_address' in d:
            o.store_address = d['store_address']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'write_off_details' in d:
            o.write_off_details = d['write_off_details']
        return o


