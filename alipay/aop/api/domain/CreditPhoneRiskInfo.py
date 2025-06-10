#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPhoneRiskInfo(object):

    def __init__(self):
        self._acc_time = None
        self._branch_company = None
        self._cert_no = None
        self._contract_reg_cust_flag = None
        self._merchant_addr = None
        self._merchant_city = None
        self._merchant_district = None
        self._merchant_id = None
        self._merchant_name = None
        self._merchant_province = None
        self._monetary_6m = None
        self._net_age = None
        self._operator_id = None
        self._service_accept_time = None
        self._sub_alipay_account = None
        self._sub_pid = None
        self._user_name = None
        self._user_province = None

    @property
    def acc_time(self):
        return self._acc_time

    @acc_time.setter
    def acc_time(self, value):
        self._acc_time = value
    @property
    def branch_company(self):
        return self._branch_company

    @branch_company.setter
    def branch_company(self, value):
        self._branch_company = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def contract_reg_cust_flag(self):
        return self._contract_reg_cust_flag

    @contract_reg_cust_flag.setter
    def contract_reg_cust_flag(self, value):
        self._contract_reg_cust_flag = value
    @property
    def merchant_addr(self):
        return self._merchant_addr

    @merchant_addr.setter
    def merchant_addr(self, value):
        self._merchant_addr = value
    @property
    def merchant_city(self):
        return self._merchant_city

    @merchant_city.setter
    def merchant_city(self, value):
        self._merchant_city = value
    @property
    def merchant_district(self):
        return self._merchant_district

    @merchant_district.setter
    def merchant_district(self, value):
        self._merchant_district = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_province(self):
        return self._merchant_province

    @merchant_province.setter
    def merchant_province(self, value):
        self._merchant_province = value
    @property
    def monetary_6m(self):
        return self._monetary_6m

    @monetary_6m.setter
    def monetary_6m(self, value):
        self._monetary_6m = value
    @property
    def net_age(self):
        return self._net_age

    @net_age.setter
    def net_age(self, value):
        self._net_age = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def service_accept_time(self):
        return self._service_accept_time

    @service_accept_time.setter
    def service_accept_time(self, value):
        self._service_accept_time = value
    @property
    def sub_alipay_account(self):
        return self._sub_alipay_account

    @sub_alipay_account.setter
    def sub_alipay_account(self, value):
        self._sub_alipay_account = value
    @property
    def sub_pid(self):
        return self._sub_pid

    @sub_pid.setter
    def sub_pid(self, value):
        self._sub_pid = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_province(self):
        return self._user_province

    @user_province.setter
    def user_province(self, value):
        self._user_province = value


    def to_alipay_dict(self):
        params = dict()
        if self.acc_time:
            if hasattr(self.acc_time, 'to_alipay_dict'):
                params['acc_time'] = self.acc_time.to_alipay_dict()
            else:
                params['acc_time'] = self.acc_time
        if self.branch_company:
            if hasattr(self.branch_company, 'to_alipay_dict'):
                params['branch_company'] = self.branch_company.to_alipay_dict()
            else:
                params['branch_company'] = self.branch_company
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.contract_reg_cust_flag:
            if hasattr(self.contract_reg_cust_flag, 'to_alipay_dict'):
                params['contract_reg_cust_flag'] = self.contract_reg_cust_flag.to_alipay_dict()
            else:
                params['contract_reg_cust_flag'] = self.contract_reg_cust_flag
        if self.merchant_addr:
            if hasattr(self.merchant_addr, 'to_alipay_dict'):
                params['merchant_addr'] = self.merchant_addr.to_alipay_dict()
            else:
                params['merchant_addr'] = self.merchant_addr
        if self.merchant_city:
            if hasattr(self.merchant_city, 'to_alipay_dict'):
                params['merchant_city'] = self.merchant_city.to_alipay_dict()
            else:
                params['merchant_city'] = self.merchant_city
        if self.merchant_district:
            if hasattr(self.merchant_district, 'to_alipay_dict'):
                params['merchant_district'] = self.merchant_district.to_alipay_dict()
            else:
                params['merchant_district'] = self.merchant_district
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_province:
            if hasattr(self.merchant_province, 'to_alipay_dict'):
                params['merchant_province'] = self.merchant_province.to_alipay_dict()
            else:
                params['merchant_province'] = self.merchant_province
        if self.monetary_6m:
            if hasattr(self.monetary_6m, 'to_alipay_dict'):
                params['monetary_6m'] = self.monetary_6m.to_alipay_dict()
            else:
                params['monetary_6m'] = self.monetary_6m
        if self.net_age:
            if hasattr(self.net_age, 'to_alipay_dict'):
                params['net_age'] = self.net_age.to_alipay_dict()
            else:
                params['net_age'] = self.net_age
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.service_accept_time:
            if hasattr(self.service_accept_time, 'to_alipay_dict'):
                params['service_accept_time'] = self.service_accept_time.to_alipay_dict()
            else:
                params['service_accept_time'] = self.service_accept_time
        if self.sub_alipay_account:
            if hasattr(self.sub_alipay_account, 'to_alipay_dict'):
                params['sub_alipay_account'] = self.sub_alipay_account.to_alipay_dict()
            else:
                params['sub_alipay_account'] = self.sub_alipay_account
        if self.sub_pid:
            if hasattr(self.sub_pid, 'to_alipay_dict'):
                params['sub_pid'] = self.sub_pid.to_alipay_dict()
            else:
                params['sub_pid'] = self.sub_pid
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_province:
            if hasattr(self.user_province, 'to_alipay_dict'):
                params['user_province'] = self.user_province.to_alipay_dict()
            else:
                params['user_province'] = self.user_province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPhoneRiskInfo()
        if 'acc_time' in d:
            o.acc_time = d['acc_time']
        if 'branch_company' in d:
            o.branch_company = d['branch_company']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'contract_reg_cust_flag' in d:
            o.contract_reg_cust_flag = d['contract_reg_cust_flag']
        if 'merchant_addr' in d:
            o.merchant_addr = d['merchant_addr']
        if 'merchant_city' in d:
            o.merchant_city = d['merchant_city']
        if 'merchant_district' in d:
            o.merchant_district = d['merchant_district']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_province' in d:
            o.merchant_province = d['merchant_province']
        if 'monetary_6m' in d:
            o.monetary_6m = d['monetary_6m']
        if 'net_age' in d:
            o.net_age = d['net_age']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'service_accept_time' in d:
            o.service_accept_time = d['service_accept_time']
        if 'sub_alipay_account' in d:
            o.sub_alipay_account = d['sub_alipay_account']
        if 'sub_pid' in d:
            o.sub_pid = d['sub_pid']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_province' in d:
            o.user_province = d['user_province']
        return o


