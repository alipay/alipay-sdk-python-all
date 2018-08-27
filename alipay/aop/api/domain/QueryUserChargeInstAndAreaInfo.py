#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryUserChargeInstAndAreaInfo(object):

    def __init__(self):
        self._charge_inst = None
        self._charge_inst_name = None
        self._city = None
        self._city_code = None
        self._pay_count = None
        self._pay_date = None
        self._sub_biz_type = None
        self._user_id = None

    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def charge_inst_name(self):
        return self._charge_inst_name

    @charge_inst_name.setter
    def charge_inst_name(self, value):
        self._charge_inst_name = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def pay_count(self):
        return self._pay_count

    @pay_count.setter
    def pay_count(self, value):
        self._pay_count = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.charge_inst_name:
            if hasattr(self.charge_inst_name, 'to_alipay_dict'):
                params['charge_inst_name'] = self.charge_inst_name.to_alipay_dict()
            else:
                params['charge_inst_name'] = self.charge_inst_name
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.pay_count:
            if hasattr(self.pay_count, 'to_alipay_dict'):
                params['pay_count'] = self.pay_count.to_alipay_dict()
            else:
                params['pay_count'] = self.pay_count
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryUserChargeInstAndAreaInfo()
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'charge_inst_name' in d:
            o.charge_inst_name = d['charge_inst_name']
        if 'city' in d:
            o.city = d['city']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'pay_count' in d:
            o.pay_count = d['pay_count']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


