#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataBillAccountbookereceiptQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_type = None
        self._file_id = None
        self._secure = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_type(self):
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, value):
        self._agreement_type = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def secure(self):
        return self._secure

    @secure.setter
    def secure(self, value):
        self._secure = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_type:
            if hasattr(self.agreement_type, 'to_alipay_dict'):
                params['agreement_type'] = self.agreement_type.to_alipay_dict()
            else:
                params['agreement_type'] = self.agreement_type
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.secure:
            if hasattr(self.secure, 'to_alipay_dict'):
                params['secure'] = self.secure.to_alipay_dict()
            else:
                params['secure'] = self.secure
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataBillAccountbookereceiptQueryModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_type' in d:
            o.agreement_type = d['agreement_type']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'secure' in d:
            o.secure = d['secure']
        return o


