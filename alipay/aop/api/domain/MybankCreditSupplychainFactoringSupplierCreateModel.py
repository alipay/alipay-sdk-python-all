#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainFactoringSupplierCreateModel(object):

    def __init__(self):
        self._buyer_ip_id = None
        self._buyer_ip_role_id = None
        self._buyer_site = None
        self._buyer_site_user_id = None
        self._rcv_account_type = None
        self._seller_bank_acc = None
        self._seller_bank_acc_name = None
        self._seller_bank_branch_union_code = None
        self._seller_bank_name = None
        self._seller_contact_email = None
        self._seller_contact_name = None
        self._seller_contact_phone = None
        self._seller_login_id = None

    @property
    def buyer_ip_id(self):
        return self._buyer_ip_id

    @buyer_ip_id.setter
    def buyer_ip_id(self, value):
        self._buyer_ip_id = value
    @property
    def buyer_ip_role_id(self):
        return self._buyer_ip_role_id

    @buyer_ip_role_id.setter
    def buyer_ip_role_id(self, value):
        self._buyer_ip_role_id = value
    @property
    def buyer_site(self):
        return self._buyer_site

    @buyer_site.setter
    def buyer_site(self, value):
        self._buyer_site = value
    @property
    def buyer_site_user_id(self):
        return self._buyer_site_user_id

    @buyer_site_user_id.setter
    def buyer_site_user_id(self, value):
        self._buyer_site_user_id = value
    @property
    def rcv_account_type(self):
        return self._rcv_account_type

    @rcv_account_type.setter
    def rcv_account_type(self, value):
        self._rcv_account_type = value
    @property
    def seller_bank_acc(self):
        return self._seller_bank_acc

    @seller_bank_acc.setter
    def seller_bank_acc(self, value):
        self._seller_bank_acc = value
    @property
    def seller_bank_acc_name(self):
        return self._seller_bank_acc_name

    @seller_bank_acc_name.setter
    def seller_bank_acc_name(self, value):
        self._seller_bank_acc_name = value
    @property
    def seller_bank_branch_union_code(self):
        return self._seller_bank_branch_union_code

    @seller_bank_branch_union_code.setter
    def seller_bank_branch_union_code(self, value):
        self._seller_bank_branch_union_code = value
    @property
    def seller_bank_name(self):
        return self._seller_bank_name

    @seller_bank_name.setter
    def seller_bank_name(self, value):
        self._seller_bank_name = value
    @property
    def seller_contact_email(self):
        return self._seller_contact_email

    @seller_contact_email.setter
    def seller_contact_email(self, value):
        self._seller_contact_email = value
    @property
    def seller_contact_name(self):
        return self._seller_contact_name

    @seller_contact_name.setter
    def seller_contact_name(self, value):
        self._seller_contact_name = value
    @property
    def seller_contact_phone(self):
        return self._seller_contact_phone

    @seller_contact_phone.setter
    def seller_contact_phone(self, value):
        self._seller_contact_phone = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_ip_id:
            if hasattr(self.buyer_ip_id, 'to_alipay_dict'):
                params['buyer_ip_id'] = self.buyer_ip_id.to_alipay_dict()
            else:
                params['buyer_ip_id'] = self.buyer_ip_id
        if self.buyer_ip_role_id:
            if hasattr(self.buyer_ip_role_id, 'to_alipay_dict'):
                params['buyer_ip_role_id'] = self.buyer_ip_role_id.to_alipay_dict()
            else:
                params['buyer_ip_role_id'] = self.buyer_ip_role_id
        if self.buyer_site:
            if hasattr(self.buyer_site, 'to_alipay_dict'):
                params['buyer_site'] = self.buyer_site.to_alipay_dict()
            else:
                params['buyer_site'] = self.buyer_site
        if self.buyer_site_user_id:
            if hasattr(self.buyer_site_user_id, 'to_alipay_dict'):
                params['buyer_site_user_id'] = self.buyer_site_user_id.to_alipay_dict()
            else:
                params['buyer_site_user_id'] = self.buyer_site_user_id
        if self.rcv_account_type:
            if hasattr(self.rcv_account_type, 'to_alipay_dict'):
                params['rcv_account_type'] = self.rcv_account_type.to_alipay_dict()
            else:
                params['rcv_account_type'] = self.rcv_account_type
        if self.seller_bank_acc:
            if hasattr(self.seller_bank_acc, 'to_alipay_dict'):
                params['seller_bank_acc'] = self.seller_bank_acc.to_alipay_dict()
            else:
                params['seller_bank_acc'] = self.seller_bank_acc
        if self.seller_bank_acc_name:
            if hasattr(self.seller_bank_acc_name, 'to_alipay_dict'):
                params['seller_bank_acc_name'] = self.seller_bank_acc_name.to_alipay_dict()
            else:
                params['seller_bank_acc_name'] = self.seller_bank_acc_name
        if self.seller_bank_branch_union_code:
            if hasattr(self.seller_bank_branch_union_code, 'to_alipay_dict'):
                params['seller_bank_branch_union_code'] = self.seller_bank_branch_union_code.to_alipay_dict()
            else:
                params['seller_bank_branch_union_code'] = self.seller_bank_branch_union_code
        if self.seller_bank_name:
            if hasattr(self.seller_bank_name, 'to_alipay_dict'):
                params['seller_bank_name'] = self.seller_bank_name.to_alipay_dict()
            else:
                params['seller_bank_name'] = self.seller_bank_name
        if self.seller_contact_email:
            if hasattr(self.seller_contact_email, 'to_alipay_dict'):
                params['seller_contact_email'] = self.seller_contact_email.to_alipay_dict()
            else:
                params['seller_contact_email'] = self.seller_contact_email
        if self.seller_contact_name:
            if hasattr(self.seller_contact_name, 'to_alipay_dict'):
                params['seller_contact_name'] = self.seller_contact_name.to_alipay_dict()
            else:
                params['seller_contact_name'] = self.seller_contact_name
        if self.seller_contact_phone:
            if hasattr(self.seller_contact_phone, 'to_alipay_dict'):
                params['seller_contact_phone'] = self.seller_contact_phone.to_alipay_dict()
            else:
                params['seller_contact_phone'] = self.seller_contact_phone
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainFactoringSupplierCreateModel()
        if 'buyer_ip_id' in d:
            o.buyer_ip_id = d['buyer_ip_id']
        if 'buyer_ip_role_id' in d:
            o.buyer_ip_role_id = d['buyer_ip_role_id']
        if 'buyer_site' in d:
            o.buyer_site = d['buyer_site']
        if 'buyer_site_user_id' in d:
            o.buyer_site_user_id = d['buyer_site_user_id']
        if 'rcv_account_type' in d:
            o.rcv_account_type = d['rcv_account_type']
        if 'seller_bank_acc' in d:
            o.seller_bank_acc = d['seller_bank_acc']
        if 'seller_bank_acc_name' in d:
            o.seller_bank_acc_name = d['seller_bank_acc_name']
        if 'seller_bank_branch_union_code' in d:
            o.seller_bank_branch_union_code = d['seller_bank_branch_union_code']
        if 'seller_bank_name' in d:
            o.seller_bank_name = d['seller_bank_name']
        if 'seller_contact_email' in d:
            o.seller_contact_email = d['seller_contact_email']
        if 'seller_contact_name' in d:
            o.seller_contact_name = d['seller_contact_name']
        if 'seller_contact_phone' in d:
            o.seller_contact_phone = d['seller_contact_phone']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        return o


