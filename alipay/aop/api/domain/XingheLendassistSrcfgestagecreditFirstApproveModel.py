#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistSrcfgestagecreditFirstApproveModel(object):

    def __init__(self):
        self._city = None
        self._cust_manager_id_card = None
        self._cust_manager_name = None
        self._district = None
        self._gov_enter_cert_no = None
        self._gov_enter_name = None
        self._ip_id = None
        self._leader_flag = None
        self._operator = None
        self._operator_company = None
        self._out_bsn_no = None
        self._prod_code = None
        self._provincial = None
        self._social_security_image_id = None
        self._user_id_card = None
        self._user_name = None
        self._user_phone = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def cust_manager_id_card(self):
        return self._cust_manager_id_card

    @cust_manager_id_card.setter
    def cust_manager_id_card(self, value):
        self._cust_manager_id_card = value
    @property
    def cust_manager_name(self):
        return self._cust_manager_name

    @cust_manager_name.setter
    def cust_manager_name(self, value):
        self._cust_manager_name = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def gov_enter_cert_no(self):
        return self._gov_enter_cert_no

    @gov_enter_cert_no.setter
    def gov_enter_cert_no(self, value):
        self._gov_enter_cert_no = value
    @property
    def gov_enter_name(self):
        return self._gov_enter_name

    @gov_enter_name.setter
    def gov_enter_name(self, value):
        self._gov_enter_name = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def leader_flag(self):
        return self._leader_flag

    @leader_flag.setter
    def leader_flag(self, value):
        self._leader_flag = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operator_company(self):
        return self._operator_company

    @operator_company.setter
    def operator_company(self, value):
        self._operator_company = value
    @property
    def out_bsn_no(self):
        return self._out_bsn_no

    @out_bsn_no.setter
    def out_bsn_no(self, value):
        self._out_bsn_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def provincial(self):
        return self._provincial

    @provincial.setter
    def provincial(self, value):
        self._provincial = value
    @property
    def social_security_image_id(self):
        return self._social_security_image_id

    @social_security_image_id.setter
    def social_security_image_id(self, value):
        self._social_security_image_id = value
    @property
    def user_id_card(self):
        return self._user_id_card

    @user_id_card.setter
    def user_id_card(self, value):
        self._user_id_card = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.cust_manager_id_card:
            if hasattr(self.cust_manager_id_card, 'to_alipay_dict'):
                params['cust_manager_id_card'] = self.cust_manager_id_card.to_alipay_dict()
            else:
                params['cust_manager_id_card'] = self.cust_manager_id_card
        if self.cust_manager_name:
            if hasattr(self.cust_manager_name, 'to_alipay_dict'):
                params['cust_manager_name'] = self.cust_manager_name.to_alipay_dict()
            else:
                params['cust_manager_name'] = self.cust_manager_name
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.gov_enter_cert_no:
            if hasattr(self.gov_enter_cert_no, 'to_alipay_dict'):
                params['gov_enter_cert_no'] = self.gov_enter_cert_no.to_alipay_dict()
            else:
                params['gov_enter_cert_no'] = self.gov_enter_cert_no
        if self.gov_enter_name:
            if hasattr(self.gov_enter_name, 'to_alipay_dict'):
                params['gov_enter_name'] = self.gov_enter_name.to_alipay_dict()
            else:
                params['gov_enter_name'] = self.gov_enter_name
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.leader_flag:
            if hasattr(self.leader_flag, 'to_alipay_dict'):
                params['leader_flag'] = self.leader_flag.to_alipay_dict()
            else:
                params['leader_flag'] = self.leader_flag
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operator_company:
            if hasattr(self.operator_company, 'to_alipay_dict'):
                params['operator_company'] = self.operator_company.to_alipay_dict()
            else:
                params['operator_company'] = self.operator_company
        if self.out_bsn_no:
            if hasattr(self.out_bsn_no, 'to_alipay_dict'):
                params['out_bsn_no'] = self.out_bsn_no.to_alipay_dict()
            else:
                params['out_bsn_no'] = self.out_bsn_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.provincial:
            if hasattr(self.provincial, 'to_alipay_dict'):
                params['provincial'] = self.provincial.to_alipay_dict()
            else:
                params['provincial'] = self.provincial
        if self.social_security_image_id:
            if hasattr(self.social_security_image_id, 'to_alipay_dict'):
                params['social_security_image_id'] = self.social_security_image_id.to_alipay_dict()
            else:
                params['social_security_image_id'] = self.social_security_image_id
        if self.user_id_card:
            if hasattr(self.user_id_card, 'to_alipay_dict'):
                params['user_id_card'] = self.user_id_card.to_alipay_dict()
            else:
                params['user_id_card'] = self.user_id_card
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistSrcfgestagecreditFirstApproveModel()
        if 'city' in d:
            o.city = d['city']
        if 'cust_manager_id_card' in d:
            o.cust_manager_id_card = d['cust_manager_id_card']
        if 'cust_manager_name' in d:
            o.cust_manager_name = d['cust_manager_name']
        if 'district' in d:
            o.district = d['district']
        if 'gov_enter_cert_no' in d:
            o.gov_enter_cert_no = d['gov_enter_cert_no']
        if 'gov_enter_name' in d:
            o.gov_enter_name = d['gov_enter_name']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'leader_flag' in d:
            o.leader_flag = d['leader_flag']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_company' in d:
            o.operator_company = d['operator_company']
        if 'out_bsn_no' in d:
            o.out_bsn_no = d['out_bsn_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'provincial' in d:
            o.provincial = d['provincial']
        if 'social_security_image_id' in d:
            o.social_security_image_id = d['social_security_image_id']
        if 'user_id_card' in d:
            o.user_id_card = d['user_id_card']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        return o


