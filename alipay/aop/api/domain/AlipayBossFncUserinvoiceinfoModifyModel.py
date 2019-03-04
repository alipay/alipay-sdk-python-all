#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserMailInfoOrder import UserMailInfoOrder


class AlipayBossFncUserinvoiceinfoModifyModel(object):

    def __init__(self):
        self._accept_electronic = None
        self._address = None
        self._auto = None
        self._bank_account = None
        self._bank_name = None
        self._business_licence_url = None
        self._hold = None
        self._id = None
        self._open_account_permit_url = None
        self._operator = None
        self._operator_type = None
        self._other_qualification_url = None
        self._tax_no = None
        self._tax_payer_quali_valid = None
        self._tax_payer_qualification = None
        self._tax_qualification_url = None
        self._tax_reg_cert_url = None
        self._telephone = None
        self._title = None
        self._user_mail_info_order_list = None

    @property
    def accept_electronic(self):
        return self._accept_electronic

    @accept_electronic.setter
    def accept_electronic(self, value):
        self._accept_electronic = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def auto(self):
        return self._auto

    @auto.setter
    def auto(self, value):
        self._auto = value
    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, value):
        self._bank_account = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def business_licence_url(self):
        return self._business_licence_url

    @business_licence_url.setter
    def business_licence_url(self, value):
        self._business_licence_url = value
    @property
    def hold(self):
        return self._hold

    @hold.setter
    def hold(self, value):
        self._hold = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def open_account_permit_url(self):
        return self._open_account_permit_url

    @open_account_permit_url.setter
    def open_account_permit_url(self, value):
        self._open_account_permit_url = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def other_qualification_url(self):
        return self._other_qualification_url

    @other_qualification_url.setter
    def other_qualification_url(self, value):
        self._other_qualification_url = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def tax_payer_quali_valid(self):
        return self._tax_payer_quali_valid

    @tax_payer_quali_valid.setter
    def tax_payer_quali_valid(self, value):
        self._tax_payer_quali_valid = value
    @property
    def tax_payer_qualification(self):
        return self._tax_payer_qualification

    @tax_payer_qualification.setter
    def tax_payer_qualification(self, value):
        self._tax_payer_qualification = value
    @property
    def tax_qualification_url(self):
        return self._tax_qualification_url

    @tax_qualification_url.setter
    def tax_qualification_url(self, value):
        self._tax_qualification_url = value
    @property
    def tax_reg_cert_url(self):
        return self._tax_reg_cert_url

    @tax_reg_cert_url.setter
    def tax_reg_cert_url(self, value):
        self._tax_reg_cert_url = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_mail_info_order_list(self):
        return self._user_mail_info_order_list

    @user_mail_info_order_list.setter
    def user_mail_info_order_list(self, value):
        if isinstance(value, list):
            self._user_mail_info_order_list = list()
            for i in value:
                if isinstance(i, UserMailInfoOrder):
                    self._user_mail_info_order_list.append(i)
                else:
                    self._user_mail_info_order_list.append(UserMailInfoOrder.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.accept_electronic:
            if hasattr(self.accept_electronic, 'to_alipay_dict'):
                params['accept_electronic'] = self.accept_electronic.to_alipay_dict()
            else:
                params['accept_electronic'] = self.accept_electronic
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.auto:
            if hasattr(self.auto, 'to_alipay_dict'):
                params['auto'] = self.auto.to_alipay_dict()
            else:
                params['auto'] = self.auto
        if self.bank_account:
            if hasattr(self.bank_account, 'to_alipay_dict'):
                params['bank_account'] = self.bank_account.to_alipay_dict()
            else:
                params['bank_account'] = self.bank_account
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.business_licence_url:
            if hasattr(self.business_licence_url, 'to_alipay_dict'):
                params['business_licence_url'] = self.business_licence_url.to_alipay_dict()
            else:
                params['business_licence_url'] = self.business_licence_url
        if self.hold:
            if hasattr(self.hold, 'to_alipay_dict'):
                params['hold'] = self.hold.to_alipay_dict()
            else:
                params['hold'] = self.hold
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.open_account_permit_url:
            if hasattr(self.open_account_permit_url, 'to_alipay_dict'):
                params['open_account_permit_url'] = self.open_account_permit_url.to_alipay_dict()
            else:
                params['open_account_permit_url'] = self.open_account_permit_url
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.other_qualification_url:
            if hasattr(self.other_qualification_url, 'to_alipay_dict'):
                params['other_qualification_url'] = self.other_qualification_url.to_alipay_dict()
            else:
                params['other_qualification_url'] = self.other_qualification_url
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.tax_payer_quali_valid:
            if hasattr(self.tax_payer_quali_valid, 'to_alipay_dict'):
                params['tax_payer_quali_valid'] = self.tax_payer_quali_valid.to_alipay_dict()
            else:
                params['tax_payer_quali_valid'] = self.tax_payer_quali_valid
        if self.tax_payer_qualification:
            if hasattr(self.tax_payer_qualification, 'to_alipay_dict'):
                params['tax_payer_qualification'] = self.tax_payer_qualification.to_alipay_dict()
            else:
                params['tax_payer_qualification'] = self.tax_payer_qualification
        if self.tax_qualification_url:
            if hasattr(self.tax_qualification_url, 'to_alipay_dict'):
                params['tax_qualification_url'] = self.tax_qualification_url.to_alipay_dict()
            else:
                params['tax_qualification_url'] = self.tax_qualification_url
        if self.tax_reg_cert_url:
            if hasattr(self.tax_reg_cert_url, 'to_alipay_dict'):
                params['tax_reg_cert_url'] = self.tax_reg_cert_url.to_alipay_dict()
            else:
                params['tax_reg_cert_url'] = self.tax_reg_cert_url
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.user_mail_info_order_list:
            if isinstance(self.user_mail_info_order_list, list):
                for i in range(0, len(self.user_mail_info_order_list)):
                    element = self.user_mail_info_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_mail_info_order_list[i] = element.to_alipay_dict()
            if hasattr(self.user_mail_info_order_list, 'to_alipay_dict'):
                params['user_mail_info_order_list'] = self.user_mail_info_order_list.to_alipay_dict()
            else:
                params['user_mail_info_order_list'] = self.user_mail_info_order_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncUserinvoiceinfoModifyModel()
        if 'accept_electronic' in d:
            o.accept_electronic = d['accept_electronic']
        if 'address' in d:
            o.address = d['address']
        if 'auto' in d:
            o.auto = d['auto']
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'business_licence_url' in d:
            o.business_licence_url = d['business_licence_url']
        if 'hold' in d:
            o.hold = d['hold']
        if 'id' in d:
            o.id = d['id']
        if 'open_account_permit_url' in d:
            o.open_account_permit_url = d['open_account_permit_url']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'other_qualification_url' in d:
            o.other_qualification_url = d['other_qualification_url']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'tax_payer_quali_valid' in d:
            o.tax_payer_quali_valid = d['tax_payer_quali_valid']
        if 'tax_payer_qualification' in d:
            o.tax_payer_qualification = d['tax_payer_qualification']
        if 'tax_qualification_url' in d:
            o.tax_qualification_url = d['tax_qualification_url']
        if 'tax_reg_cert_url' in d:
            o.tax_reg_cert_url = d['tax_reg_cert_url']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'title' in d:
            o.title = d['title']
        if 'user_mail_info_order_list' in d:
            o.user_mail_info_order_list = d['user_mail_info_order_list']
        return o


