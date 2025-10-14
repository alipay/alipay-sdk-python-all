#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgreementFile(object):

    def __init__(self):
        self._agreement_no = None
        self._contract_no = None
        self._file_id = None
        self._sign_status = None
        self._sign_time = None
        self._type = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgreementFile()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'type' in d:
            o.type = d['type']
        return o


