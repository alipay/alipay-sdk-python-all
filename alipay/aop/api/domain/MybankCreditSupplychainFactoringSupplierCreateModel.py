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
        self._merchant_id = None
        self._operator_name = None
        self._rcv_account_type = None
        self._seller_bank_acc = None
        self._seller_bank_acc_name = None
        self._seller_bank_branch_union_code = None
        self._seller_bank_name = None
        self._seller_contact_email = None
        self._seller_contact_name = None
        self._seller_contact_phone = None
        self._seller_login_id = None
        self._store_city = None
        self._store_county = None
        self._store_name = None
        self._store_no = None
        self._store_province = None
        self._store_subject_cert_no = None
        self._store_subject_name = None

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
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
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
    @property
    def store_city(self):
        return self._store_city

    @store_city.setter
    def store_city(self, value):
        self._store_city = value
    @property
    def store_county(self):
        return self._store_county

    @store_county.setter
    def store_county(self, value):
        self._store_county = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def store_no(self):
        return self._store_no

    @store_no.setter
    def store_no(self, value):
        self._store_no = value
    @property
    def store_province(self):
        return self._store_province

    @store_province.setter
    def store_province(self, value):
        self._store_province = value
    @property
    def store_subject_cert_no(self):
        return self._store_subject_cert_no

    @store_subject_cert_no.setter
    def store_subject_cert_no(self, value):
        self._store_subject_cert_no = value
    @property
    def store_subject_name(self):
        return self._store_subject_name

    @store_subject_name.setter
    def store_subject_name(self, value):
        self._store_subject_name = value


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
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
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
        if self.store_city:
            if hasattr(self.store_city, 'to_alipay_dict'):
                params['store_city'] = self.store_city.to_alipay_dict()
            else:
                params['store_city'] = self.store_city
        if self.store_county:
            if hasattr(self.store_county, 'to_alipay_dict'):
                params['store_county'] = self.store_county.to_alipay_dict()
            else:
                params['store_county'] = self.store_county
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.store_no:
            if hasattr(self.store_no, 'to_alipay_dict'):
                params['store_no'] = self.store_no.to_alipay_dict()
            else:
                params['store_no'] = self.store_no
        if self.store_province:
            if hasattr(self.store_province, 'to_alipay_dict'):
                params['store_province'] = self.store_province.to_alipay_dict()
            else:
                params['store_province'] = self.store_province
        if self.store_subject_cert_no:
            if hasattr(self.store_subject_cert_no, 'to_alipay_dict'):
                params['store_subject_cert_no'] = self.store_subject_cert_no.to_alipay_dict()
            else:
                params['store_subject_cert_no'] = self.store_subject_cert_no
        if self.store_subject_name:
            if hasattr(self.store_subject_name, 'to_alipay_dict'):
                params['store_subject_name'] = self.store_subject_name.to_alipay_dict()
            else:
                params['store_subject_name'] = self.store_subject_name
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
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
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
        if 'store_city' in d:
            o.store_city = d['store_city']
        if 'store_county' in d:
            o.store_county = d['store_county']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'store_no' in d:
            o.store_no = d['store_no']
        if 'store_province' in d:
            o.store_province = d['store_province']
        if 'store_subject_cert_no' in d:
            o.store_subject_cert_no = d['store_subject_cert_no']
        if 'store_subject_name' in d:
            o.store_subject_name = d['store_subject_name']
        return o


