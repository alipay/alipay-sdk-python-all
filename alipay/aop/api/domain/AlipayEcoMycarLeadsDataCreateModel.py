#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LeadsCarInfo import LeadsCarInfo
from alipay.aop.api.domain.LeadsMerchantInfo import LeadsMerchantInfo


class AlipayEcoMycarLeadsDataCreateModel(object):

    def __init__(self):
        self._alipay_account = None
        self._leads_car = None
        self._leads_city_code = None
        self._leads_merchants = None
        self._leads_source = None
        self._mobile_no = None
        self._open_id = None
        self._out_leads_id = None
        self._user_id = None
        self._user_name = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def leads_car(self):
        return self._leads_car

    @leads_car.setter
    def leads_car(self, value):
        if isinstance(value, LeadsCarInfo):
            self._leads_car = value
        else:
            self._leads_car = LeadsCarInfo.from_alipay_dict(value)
    @property
    def leads_city_code(self):
        return self._leads_city_code

    @leads_city_code.setter
    def leads_city_code(self, value):
        self._leads_city_code = value
    @property
    def leads_merchants(self):
        return self._leads_merchants

    @leads_merchants.setter
    def leads_merchants(self, value):
        if isinstance(value, list):
            self._leads_merchants = list()
            for i in value:
                if isinstance(i, LeadsMerchantInfo):
                    self._leads_merchants.append(i)
                else:
                    self._leads_merchants.append(LeadsMerchantInfo.from_alipay_dict(i))
    @property
    def leads_source(self):
        return self._leads_source

    @leads_source.setter
    def leads_source(self, value):
        self._leads_source = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_leads_id(self):
        return self._out_leads_id

    @out_leads_id.setter
    def out_leads_id(self, value):
        self._out_leads_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.leads_car:
            if hasattr(self.leads_car, 'to_alipay_dict'):
                params['leads_car'] = self.leads_car.to_alipay_dict()
            else:
                params['leads_car'] = self.leads_car
        if self.leads_city_code:
            if hasattr(self.leads_city_code, 'to_alipay_dict'):
                params['leads_city_code'] = self.leads_city_code.to_alipay_dict()
            else:
                params['leads_city_code'] = self.leads_city_code
        if self.leads_merchants:
            if isinstance(self.leads_merchants, list):
                for i in range(0, len(self.leads_merchants)):
                    element = self.leads_merchants[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.leads_merchants[i] = element.to_alipay_dict()
            if hasattr(self.leads_merchants, 'to_alipay_dict'):
                params['leads_merchants'] = self.leads_merchants.to_alipay_dict()
            else:
                params['leads_merchants'] = self.leads_merchants
        if self.leads_source:
            if hasattr(self.leads_source, 'to_alipay_dict'):
                params['leads_source'] = self.leads_source.to_alipay_dict()
            else:
                params['leads_source'] = self.leads_source
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_leads_id:
            if hasattr(self.out_leads_id, 'to_alipay_dict'):
                params['out_leads_id'] = self.out_leads_id.to_alipay_dict()
            else:
                params['out_leads_id'] = self.out_leads_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarLeadsDataCreateModel()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'leads_car' in d:
            o.leads_car = d['leads_car']
        if 'leads_city_code' in d:
            o.leads_city_code = d['leads_city_code']
        if 'leads_merchants' in d:
            o.leads_merchants = d['leads_merchants']
        if 'leads_source' in d:
            o.leads_source = d['leads_source']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_leads_id' in d:
            o.out_leads_id = d['out_leads_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


