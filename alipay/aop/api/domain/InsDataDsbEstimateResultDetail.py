#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsDataDsbEstimateResultDetail(object):

    def __init__(self):
        self._damage_degree = None
        self._damage_degree_desc = None
        self._damage_type = None
        self._damage_type_desc = None
        self._hourly_code = None
        self._hourly_wage = None
        self._oe_code = None
        self._old_recycle = None
        self._parts_cost = None
        self._parts_manage_fee = None
        self._parts_name = None
        self._remain_value = None
        self._repair_type = None
        self._repair_type_desc = None

    @property
    def damage_degree(self):
        return self._damage_degree

    @damage_degree.setter
    def damage_degree(self, value):
        self._damage_degree = value
    @property
    def damage_degree_desc(self):
        return self._damage_degree_desc

    @damage_degree_desc.setter
    def damage_degree_desc(self, value):
        self._damage_degree_desc = value
    @property
    def damage_type(self):
        return self._damage_type

    @damage_type.setter
    def damage_type(self, value):
        self._damage_type = value
    @property
    def damage_type_desc(self):
        return self._damage_type_desc

    @damage_type_desc.setter
    def damage_type_desc(self, value):
        self._damage_type_desc = value
    @property
    def hourly_code(self):
        return self._hourly_code

    @hourly_code.setter
    def hourly_code(self, value):
        self._hourly_code = value
    @property
    def hourly_wage(self):
        return self._hourly_wage

    @hourly_wage.setter
    def hourly_wage(self, value):
        self._hourly_wage = value
    @property
    def oe_code(self):
        return self._oe_code

    @oe_code.setter
    def oe_code(self, value):
        self._oe_code = value
    @property
    def old_recycle(self):
        return self._old_recycle

    @old_recycle.setter
    def old_recycle(self, value):
        self._old_recycle = value
    @property
    def parts_cost(self):
        return self._parts_cost

    @parts_cost.setter
    def parts_cost(self, value):
        self._parts_cost = value
    @property
    def parts_manage_fee(self):
        return self._parts_manage_fee

    @parts_manage_fee.setter
    def parts_manage_fee(self, value):
        self._parts_manage_fee = value
    @property
    def parts_name(self):
        return self._parts_name

    @parts_name.setter
    def parts_name(self, value):
        self._parts_name = value
    @property
    def remain_value(self):
        return self._remain_value

    @remain_value.setter
    def remain_value(self, value):
        self._remain_value = value
    @property
    def repair_type(self):
        return self._repair_type

    @repair_type.setter
    def repair_type(self, value):
        self._repair_type = value
    @property
    def repair_type_desc(self):
        return self._repair_type_desc

    @repair_type_desc.setter
    def repair_type_desc(self, value):
        self._repair_type_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.damage_degree:
            if hasattr(self.damage_degree, 'to_alipay_dict'):
                params['damage_degree'] = self.damage_degree.to_alipay_dict()
            else:
                params['damage_degree'] = self.damage_degree
        if self.damage_degree_desc:
            if hasattr(self.damage_degree_desc, 'to_alipay_dict'):
                params['damage_degree_desc'] = self.damage_degree_desc.to_alipay_dict()
            else:
                params['damage_degree_desc'] = self.damage_degree_desc
        if self.damage_type:
            if hasattr(self.damage_type, 'to_alipay_dict'):
                params['damage_type'] = self.damage_type.to_alipay_dict()
            else:
                params['damage_type'] = self.damage_type
        if self.damage_type_desc:
            if hasattr(self.damage_type_desc, 'to_alipay_dict'):
                params['damage_type_desc'] = self.damage_type_desc.to_alipay_dict()
            else:
                params['damage_type_desc'] = self.damage_type_desc
        if self.hourly_code:
            if hasattr(self.hourly_code, 'to_alipay_dict'):
                params['hourly_code'] = self.hourly_code.to_alipay_dict()
            else:
                params['hourly_code'] = self.hourly_code
        if self.hourly_wage:
            if hasattr(self.hourly_wage, 'to_alipay_dict'):
                params['hourly_wage'] = self.hourly_wage.to_alipay_dict()
            else:
                params['hourly_wage'] = self.hourly_wage
        if self.oe_code:
            if hasattr(self.oe_code, 'to_alipay_dict'):
                params['oe_code'] = self.oe_code.to_alipay_dict()
            else:
                params['oe_code'] = self.oe_code
        if self.old_recycle:
            if hasattr(self.old_recycle, 'to_alipay_dict'):
                params['old_recycle'] = self.old_recycle.to_alipay_dict()
            else:
                params['old_recycle'] = self.old_recycle
        if self.parts_cost:
            if hasattr(self.parts_cost, 'to_alipay_dict'):
                params['parts_cost'] = self.parts_cost.to_alipay_dict()
            else:
                params['parts_cost'] = self.parts_cost
        if self.parts_manage_fee:
            if hasattr(self.parts_manage_fee, 'to_alipay_dict'):
                params['parts_manage_fee'] = self.parts_manage_fee.to_alipay_dict()
            else:
                params['parts_manage_fee'] = self.parts_manage_fee
        if self.parts_name:
            if hasattr(self.parts_name, 'to_alipay_dict'):
                params['parts_name'] = self.parts_name.to_alipay_dict()
            else:
                params['parts_name'] = self.parts_name
        if self.remain_value:
            if hasattr(self.remain_value, 'to_alipay_dict'):
                params['remain_value'] = self.remain_value.to_alipay_dict()
            else:
                params['remain_value'] = self.remain_value
        if self.repair_type:
            if hasattr(self.repair_type, 'to_alipay_dict'):
                params['repair_type'] = self.repair_type.to_alipay_dict()
            else:
                params['repair_type'] = self.repair_type
        if self.repair_type_desc:
            if hasattr(self.repair_type_desc, 'to_alipay_dict'):
                params['repair_type_desc'] = self.repair_type_desc.to_alipay_dict()
            else:
                params['repair_type_desc'] = self.repair_type_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsDataDsbEstimateResultDetail()
        if 'damage_degree' in d:
            o.damage_degree = d['damage_degree']
        if 'damage_degree_desc' in d:
            o.damage_degree_desc = d['damage_degree_desc']
        if 'damage_type' in d:
            o.damage_type = d['damage_type']
        if 'damage_type_desc' in d:
            o.damage_type_desc = d['damage_type_desc']
        if 'hourly_code' in d:
            o.hourly_code = d['hourly_code']
        if 'hourly_wage' in d:
            o.hourly_wage = d['hourly_wage']
        if 'oe_code' in d:
            o.oe_code = d['oe_code']
        if 'old_recycle' in d:
            o.old_recycle = d['old_recycle']
        if 'parts_cost' in d:
            o.parts_cost = d['parts_cost']
        if 'parts_manage_fee' in d:
            o.parts_manage_fee = d['parts_manage_fee']
        if 'parts_name' in d:
            o.parts_name = d['parts_name']
        if 'remain_value' in d:
            o.remain_value = d['remain_value']
        if 'repair_type' in d:
            o.repair_type = d['repair_type']
        if 'repair_type_desc' in d:
            o.repair_type_desc = d['repair_type_desc']
        return o


