#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeGuarletterCompensateApplyModel(object):

    def __init__(self):
        self._apply_user_cert_no = None
        self._apply_user_name = None
        self._apply_user_phone = None
        self._beneficiary_bank_card_no = None
        self._beneficiary_bank_name = None
        self._file_list = None
        self._guar_letter_order_no = None
        self._reason = None
        self._request_id = None
        self._scheme_ar_no = None

    @property
    def apply_user_cert_no(self):
        return self._apply_user_cert_no

    @apply_user_cert_no.setter
    def apply_user_cert_no(self, value):
        self._apply_user_cert_no = value
    @property
    def apply_user_name(self):
        return self._apply_user_name

    @apply_user_name.setter
    def apply_user_name(self, value):
        self._apply_user_name = value
    @property
    def apply_user_phone(self):
        return self._apply_user_phone

    @apply_user_phone.setter
    def apply_user_phone(self, value):
        self._apply_user_phone = value
    @property
    def beneficiary_bank_card_no(self):
        return self._beneficiary_bank_card_no

    @beneficiary_bank_card_no.setter
    def beneficiary_bank_card_no(self, value):
        self._beneficiary_bank_card_no = value
    @property
    def beneficiary_bank_name(self):
        return self._beneficiary_bank_name

    @beneficiary_bank_name.setter
    def beneficiary_bank_name(self, value):
        self._beneficiary_bank_name = value
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        self._file_list = value
    @property
    def guar_letter_order_no(self):
        return self._guar_letter_order_no

    @guar_letter_order_no.setter
    def guar_letter_order_no(self, value):
        self._guar_letter_order_no = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scheme_ar_no(self):
        return self._scheme_ar_no

    @scheme_ar_no.setter
    def scheme_ar_no(self, value):
        self._scheme_ar_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_user_cert_no:
            if hasattr(self.apply_user_cert_no, 'to_alipay_dict'):
                params['apply_user_cert_no'] = self.apply_user_cert_no.to_alipay_dict()
            else:
                params['apply_user_cert_no'] = self.apply_user_cert_no
        if self.apply_user_name:
            if hasattr(self.apply_user_name, 'to_alipay_dict'):
                params['apply_user_name'] = self.apply_user_name.to_alipay_dict()
            else:
                params['apply_user_name'] = self.apply_user_name
        if self.apply_user_phone:
            if hasattr(self.apply_user_phone, 'to_alipay_dict'):
                params['apply_user_phone'] = self.apply_user_phone.to_alipay_dict()
            else:
                params['apply_user_phone'] = self.apply_user_phone
        if self.beneficiary_bank_card_no:
            if hasattr(self.beneficiary_bank_card_no, 'to_alipay_dict'):
                params['beneficiary_bank_card_no'] = self.beneficiary_bank_card_no.to_alipay_dict()
            else:
                params['beneficiary_bank_card_no'] = self.beneficiary_bank_card_no
        if self.beneficiary_bank_name:
            if hasattr(self.beneficiary_bank_name, 'to_alipay_dict'):
                params['beneficiary_bank_name'] = self.beneficiary_bank_name.to_alipay_dict()
            else:
                params['beneficiary_bank_name'] = self.beneficiary_bank_name
        if self.file_list:
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        if self.guar_letter_order_no:
            if hasattr(self.guar_letter_order_no, 'to_alipay_dict'):
                params['guar_letter_order_no'] = self.guar_letter_order_no.to_alipay_dict()
            else:
                params['guar_letter_order_no'] = self.guar_letter_order_no
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scheme_ar_no:
            if hasattr(self.scheme_ar_no, 'to_alipay_dict'):
                params['scheme_ar_no'] = self.scheme_ar_no.to_alipay_dict()
            else:
                params['scheme_ar_no'] = self.scheme_ar_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeGuarletterCompensateApplyModel()
        if 'apply_user_cert_no' in d:
            o.apply_user_cert_no = d['apply_user_cert_no']
        if 'apply_user_name' in d:
            o.apply_user_name = d['apply_user_name']
        if 'apply_user_phone' in d:
            o.apply_user_phone = d['apply_user_phone']
        if 'beneficiary_bank_card_no' in d:
            o.beneficiary_bank_card_no = d['beneficiary_bank_card_no']
        if 'beneficiary_bank_name' in d:
            o.beneficiary_bank_name = d['beneficiary_bank_name']
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'guar_letter_order_no' in d:
            o.guar_letter_order_no = d['guar_letter_order_no']
        if 'reason' in d:
            o.reason = d['reason']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scheme_ar_no' in d:
            o.scheme_ar_no = d['scheme_ar_no']
        return o


