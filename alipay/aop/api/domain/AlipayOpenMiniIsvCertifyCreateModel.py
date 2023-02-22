#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniIsvCertifyCreateModel(object):

    def __init__(self):
        self._alipay_account = None
        self._cert_name = None
        self._cert_no = None
        self._contact_name = None
        self._contact_phone = None
        self._is_individual = None
        self._legal_personal_name = None
        self._license_pic = None
        self._order_no = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def is_individual(self):
        return self._is_individual

    @is_individual.setter
    def is_individual(self, value):
        self._is_individual = value
    @property
    def legal_personal_name(self):
        return self._legal_personal_name

    @legal_personal_name.setter
    def legal_personal_name(self, value):
        self._legal_personal_name = value
    @property
    def license_pic(self):
        return self._license_pic

    @license_pic.setter
    def license_pic(self, value):
        self._license_pic = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.is_individual:
            if hasattr(self.is_individual, 'to_alipay_dict'):
                params['is_individual'] = self.is_individual.to_alipay_dict()
            else:
                params['is_individual'] = self.is_individual
        if self.legal_personal_name:
            if hasattr(self.legal_personal_name, 'to_alipay_dict'):
                params['legal_personal_name'] = self.legal_personal_name.to_alipay_dict()
            else:
                params['legal_personal_name'] = self.legal_personal_name
        if self.license_pic:
            if hasattr(self.license_pic, 'to_alipay_dict'):
                params['license_pic'] = self.license_pic.to_alipay_dict()
            else:
                params['license_pic'] = self.license_pic
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniIsvCertifyCreateModel()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'is_individual' in d:
            o.is_individual = d['is_individual']
        if 'legal_personal_name' in d:
            o.legal_personal_name = d['legal_personal_name']
        if 'license_pic' in d:
            o.license_pic = d['license_pic']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


