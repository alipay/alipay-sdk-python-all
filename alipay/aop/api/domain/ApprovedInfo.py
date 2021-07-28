#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApprovedInfo(object):

    def __init__(self):
        self._application_no = None
        self._approval_letter_url = None
        self._imm_code = None
        self._imm_fullname = None
        self._imm_position = None
        self._note = None
        self._payment_confirm_url = None
        self._receipt_url = None
        self._remark = None
        self._status = None
        self._status_date_time = None
        self._tm_6_url = None
        self._tm_88_url = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value
    @property
    def approval_letter_url(self):
        return self._approval_letter_url

    @approval_letter_url.setter
    def approval_letter_url(self, value):
        self._approval_letter_url = value
    @property
    def imm_code(self):
        return self._imm_code

    @imm_code.setter
    def imm_code(self, value):
        self._imm_code = value
    @property
    def imm_fullname(self):
        return self._imm_fullname

    @imm_fullname.setter
    def imm_fullname(self, value):
        self._imm_fullname = value
    @property
    def imm_position(self):
        return self._imm_position

    @imm_position.setter
    def imm_position(self, value):
        self._imm_position = value
    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value
    @property
    def payment_confirm_url(self):
        return self._payment_confirm_url

    @payment_confirm_url.setter
    def payment_confirm_url(self, value):
        self._payment_confirm_url = value
    @property
    def receipt_url(self):
        return self._receipt_url

    @receipt_url.setter
    def receipt_url(self, value):
        self._receipt_url = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_date_time(self):
        return self._status_date_time

    @status_date_time.setter
    def status_date_time(self, value):
        self._status_date_time = value
    @property
    def tm_6_url(self):
        return self._tm_6_url

    @tm_6_url.setter
    def tm_6_url(self, value):
        self._tm_6_url = value
    @property
    def tm_88_url(self):
        return self._tm_88_url

    @tm_88_url.setter
    def tm_88_url(self, value):
        self._tm_88_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_no:
            if hasattr(self.application_no, 'to_alipay_dict'):
                params['application_no'] = self.application_no.to_alipay_dict()
            else:
                params['application_no'] = self.application_no
        if self.approval_letter_url:
            if hasattr(self.approval_letter_url, 'to_alipay_dict'):
                params['approval_letter_url'] = self.approval_letter_url.to_alipay_dict()
            else:
                params['approval_letter_url'] = self.approval_letter_url
        if self.imm_code:
            if hasattr(self.imm_code, 'to_alipay_dict'):
                params['imm_code'] = self.imm_code.to_alipay_dict()
            else:
                params['imm_code'] = self.imm_code
        if self.imm_fullname:
            if hasattr(self.imm_fullname, 'to_alipay_dict'):
                params['imm_fullname'] = self.imm_fullname.to_alipay_dict()
            else:
                params['imm_fullname'] = self.imm_fullname
        if self.imm_position:
            if hasattr(self.imm_position, 'to_alipay_dict'):
                params['imm_position'] = self.imm_position.to_alipay_dict()
            else:
                params['imm_position'] = self.imm_position
        if self.note:
            if hasattr(self.note, 'to_alipay_dict'):
                params['note'] = self.note.to_alipay_dict()
            else:
                params['note'] = self.note
        if self.payment_confirm_url:
            if hasattr(self.payment_confirm_url, 'to_alipay_dict'):
                params['payment_confirm_url'] = self.payment_confirm_url.to_alipay_dict()
            else:
                params['payment_confirm_url'] = self.payment_confirm_url
        if self.receipt_url:
            if hasattr(self.receipt_url, 'to_alipay_dict'):
                params['receipt_url'] = self.receipt_url.to_alipay_dict()
            else:
                params['receipt_url'] = self.receipt_url
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_date_time:
            if hasattr(self.status_date_time, 'to_alipay_dict'):
                params['status_date_time'] = self.status_date_time.to_alipay_dict()
            else:
                params['status_date_time'] = self.status_date_time
        if self.tm_6_url:
            if hasattr(self.tm_6_url, 'to_alipay_dict'):
                params['tm_6_url'] = self.tm_6_url.to_alipay_dict()
            else:
                params['tm_6_url'] = self.tm_6_url
        if self.tm_88_url:
            if hasattr(self.tm_88_url, 'to_alipay_dict'):
                params['tm_88_url'] = self.tm_88_url.to_alipay_dict()
            else:
                params['tm_88_url'] = self.tm_88_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApprovedInfo()
        if 'application_no' in d:
            o.application_no = d['application_no']
        if 'approval_letter_url' in d:
            o.approval_letter_url = d['approval_letter_url']
        if 'imm_code' in d:
            o.imm_code = d['imm_code']
        if 'imm_fullname' in d:
            o.imm_fullname = d['imm_fullname']
        if 'imm_position' in d:
            o.imm_position = d['imm_position']
        if 'note' in d:
            o.note = d['note']
        if 'payment_confirm_url' in d:
            o.payment_confirm_url = d['payment_confirm_url']
        if 'receipt_url' in d:
            o.receipt_url = d['receipt_url']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        if 'status_date_time' in d:
            o.status_date_time = d['status_date_time']
        if 'tm_6_url' in d:
            o.tm_6_url = d['tm_6_url']
        if 'tm_88_url' in d:
            o.tm_88_url = d['tm_88_url']
        return o


