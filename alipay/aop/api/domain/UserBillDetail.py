#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserBillDetail(object):

    def __init__(self):
        self._alipay_login_id = None
        self._alipay_uid = None
        self._amount_before_tax = None
        self._id_cert_no = None
        self._mobile = None
        self._open_id = None
        self._real_name = None
        self._user_bill_no = None

    @property
    def alipay_login_id(self):
        return self._alipay_login_id

    @alipay_login_id.setter
    def alipay_login_id(self, value):
        self._alipay_login_id = value
    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def amount_before_tax(self):
        return self._amount_before_tax

    @amount_before_tax.setter
    def amount_before_tax(self, value):
        self._amount_before_tax = value
    @property
    def id_cert_no(self):
        return self._id_cert_no

    @id_cert_no.setter
    def id_cert_no(self, value):
        self._id_cert_no = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def user_bill_no(self):
        return self._user_bill_no

    @user_bill_no.setter
    def user_bill_no(self, value):
        self._user_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_login_id:
            if hasattr(self.alipay_login_id, 'to_alipay_dict'):
                params['alipay_login_id'] = self.alipay_login_id.to_alipay_dict()
            else:
                params['alipay_login_id'] = self.alipay_login_id
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.amount_before_tax:
            if hasattr(self.amount_before_tax, 'to_alipay_dict'):
                params['amount_before_tax'] = self.amount_before_tax.to_alipay_dict()
            else:
                params['amount_before_tax'] = self.amount_before_tax
        if self.id_cert_no:
            if hasattr(self.id_cert_no, 'to_alipay_dict'):
                params['id_cert_no'] = self.id_cert_no.to_alipay_dict()
            else:
                params['id_cert_no'] = self.id_cert_no
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
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
        o = UserBillDetail()
        if 'alipay_login_id' in d:
            o.alipay_login_id = d['alipay_login_id']
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'amount_before_tax' in d:
            o.amount_before_tax = d['amount_before_tax']
        if 'id_cert_no' in d:
            o.id_cert_no = d['id_cert_no']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'user_bill_no' in d:
            o.user_bill_no = d['user_bill_no']
        return o


