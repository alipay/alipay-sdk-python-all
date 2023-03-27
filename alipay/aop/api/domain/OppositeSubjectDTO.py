#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OppositeSubjectDTO(object):

    def __init__(self):
        self._memo = None
        self._opposite_contact_addr = None
        self._opposite_contact_email = None
        self._opposite_contact_name = None
        self._opposite_contact_phone = None
        self._opposite_subject_name = None
        self._opposite_uscc = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def opposite_contact_addr(self):
        return self._opposite_contact_addr

    @opposite_contact_addr.setter
    def opposite_contact_addr(self, value):
        self._opposite_contact_addr = value
    @property
    def opposite_contact_email(self):
        return self._opposite_contact_email

    @opposite_contact_email.setter
    def opposite_contact_email(self, value):
        self._opposite_contact_email = value
    @property
    def opposite_contact_name(self):
        return self._opposite_contact_name

    @opposite_contact_name.setter
    def opposite_contact_name(self, value):
        self._opposite_contact_name = value
    @property
    def opposite_contact_phone(self):
        return self._opposite_contact_phone

    @opposite_contact_phone.setter
    def opposite_contact_phone(self, value):
        self._opposite_contact_phone = value
    @property
    def opposite_subject_name(self):
        return self._opposite_subject_name

    @opposite_subject_name.setter
    def opposite_subject_name(self, value):
        self._opposite_subject_name = value
    @property
    def opposite_uscc(self):
        return self._opposite_uscc

    @opposite_uscc.setter
    def opposite_uscc(self, value):
        self._opposite_uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.opposite_contact_addr:
            if hasattr(self.opposite_contact_addr, 'to_alipay_dict'):
                params['opposite_contact_addr'] = self.opposite_contact_addr.to_alipay_dict()
            else:
                params['opposite_contact_addr'] = self.opposite_contact_addr
        if self.opposite_contact_email:
            if hasattr(self.opposite_contact_email, 'to_alipay_dict'):
                params['opposite_contact_email'] = self.opposite_contact_email.to_alipay_dict()
            else:
                params['opposite_contact_email'] = self.opposite_contact_email
        if self.opposite_contact_name:
            if hasattr(self.opposite_contact_name, 'to_alipay_dict'):
                params['opposite_contact_name'] = self.opposite_contact_name.to_alipay_dict()
            else:
                params['opposite_contact_name'] = self.opposite_contact_name
        if self.opposite_contact_phone:
            if hasattr(self.opposite_contact_phone, 'to_alipay_dict'):
                params['opposite_contact_phone'] = self.opposite_contact_phone.to_alipay_dict()
            else:
                params['opposite_contact_phone'] = self.opposite_contact_phone
        if self.opposite_subject_name:
            if hasattr(self.opposite_subject_name, 'to_alipay_dict'):
                params['opposite_subject_name'] = self.opposite_subject_name.to_alipay_dict()
            else:
                params['opposite_subject_name'] = self.opposite_subject_name
        if self.opposite_uscc:
            if hasattr(self.opposite_uscc, 'to_alipay_dict'):
                params['opposite_uscc'] = self.opposite_uscc.to_alipay_dict()
            else:
                params['opposite_uscc'] = self.opposite_uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OppositeSubjectDTO()
        if 'memo' in d:
            o.memo = d['memo']
        if 'opposite_contact_addr' in d:
            o.opposite_contact_addr = d['opposite_contact_addr']
        if 'opposite_contact_email' in d:
            o.opposite_contact_email = d['opposite_contact_email']
        if 'opposite_contact_name' in d:
            o.opposite_contact_name = d['opposite_contact_name']
        if 'opposite_contact_phone' in d:
            o.opposite_contact_phone = d['opposite_contact_phone']
        if 'opposite_subject_name' in d:
            o.opposite_subject_name = d['opposite_subject_name']
        if 'opposite_uscc' in d:
            o.opposite_uscc = d['opposite_uscc']
        return o


