#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PunishBreakInfo(object):

    def __init__(self):
        self._business_entity = None
        self._card_num = None
        self._case_code = None
        self._court_name = None
        self._disrupt_type_name = None
        self._duty = None
        self._gist_id = None
        self._gist_unit = None
        self._name = None
        self._performance = None
        self._performed_part = None
        self._province = None
        self._publish_date = None
        self._reg_case_date = None
        self._trpe = None
        self._type = None
        self._un_perform_part = None

    @property
    def business_entity(self):
        return self._business_entity

    @business_entity.setter
    def business_entity(self, value):
        self._business_entity = value
    @property
    def card_num(self):
        return self._card_num

    @card_num.setter
    def card_num(self, value):
        self._card_num = value
    @property
    def case_code(self):
        return self._case_code

    @case_code.setter
    def case_code(self, value):
        self._case_code = value
    @property
    def court_name(self):
        return self._court_name

    @court_name.setter
    def court_name(self, value):
        self._court_name = value
    @property
    def disrupt_type_name(self):
        return self._disrupt_type_name

    @disrupt_type_name.setter
    def disrupt_type_name(self, value):
        self._disrupt_type_name = value
    @property
    def duty(self):
        return self._duty

    @duty.setter
    def duty(self, value):
        self._duty = value
    @property
    def gist_id(self):
        return self._gist_id

    @gist_id.setter
    def gist_id(self, value):
        self._gist_id = value
    @property
    def gist_unit(self):
        return self._gist_unit

    @gist_unit.setter
    def gist_unit(self, value):
        self._gist_unit = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def performance(self):
        return self._performance

    @performance.setter
    def performance(self, value):
        self._performance = value
    @property
    def performed_part(self):
        return self._performed_part

    @performed_part.setter
    def performed_part(self, value):
        self._performed_part = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def publish_date(self):
        return self._publish_date

    @publish_date.setter
    def publish_date(self, value):
        self._publish_date = value
    @property
    def reg_case_date(self):
        return self._reg_case_date

    @reg_case_date.setter
    def reg_case_date(self, value):
        self._reg_case_date = value
    @property
    def trpe(self):
        return self._trpe

    @trpe.setter
    def trpe(self, value):
        self._trpe = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def un_perform_part(self):
        return self._un_perform_part

    @un_perform_part.setter
    def un_perform_part(self, value):
        self._un_perform_part = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_entity:
            if hasattr(self.business_entity, 'to_alipay_dict'):
                params['business_entity'] = self.business_entity.to_alipay_dict()
            else:
                params['business_entity'] = self.business_entity
        if self.card_num:
            if hasattr(self.card_num, 'to_alipay_dict'):
                params['card_num'] = self.card_num.to_alipay_dict()
            else:
                params['card_num'] = self.card_num
        if self.case_code:
            if hasattr(self.case_code, 'to_alipay_dict'):
                params['case_code'] = self.case_code.to_alipay_dict()
            else:
                params['case_code'] = self.case_code
        if self.court_name:
            if hasattr(self.court_name, 'to_alipay_dict'):
                params['court_name'] = self.court_name.to_alipay_dict()
            else:
                params['court_name'] = self.court_name
        if self.disrupt_type_name:
            if hasattr(self.disrupt_type_name, 'to_alipay_dict'):
                params['disrupt_type_name'] = self.disrupt_type_name.to_alipay_dict()
            else:
                params['disrupt_type_name'] = self.disrupt_type_name
        if self.duty:
            if hasattr(self.duty, 'to_alipay_dict'):
                params['duty'] = self.duty.to_alipay_dict()
            else:
                params['duty'] = self.duty
        if self.gist_id:
            if hasattr(self.gist_id, 'to_alipay_dict'):
                params['gist_id'] = self.gist_id.to_alipay_dict()
            else:
                params['gist_id'] = self.gist_id
        if self.gist_unit:
            if hasattr(self.gist_unit, 'to_alipay_dict'):
                params['gist_unit'] = self.gist_unit.to_alipay_dict()
            else:
                params['gist_unit'] = self.gist_unit
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.performance:
            if hasattr(self.performance, 'to_alipay_dict'):
                params['performance'] = self.performance.to_alipay_dict()
            else:
                params['performance'] = self.performance
        if self.performed_part:
            if hasattr(self.performed_part, 'to_alipay_dict'):
                params['performed_part'] = self.performed_part.to_alipay_dict()
            else:
                params['performed_part'] = self.performed_part
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.publish_date:
            if hasattr(self.publish_date, 'to_alipay_dict'):
                params['publish_date'] = self.publish_date.to_alipay_dict()
            else:
                params['publish_date'] = self.publish_date
        if self.reg_case_date:
            if hasattr(self.reg_case_date, 'to_alipay_dict'):
                params['reg_case_date'] = self.reg_case_date.to_alipay_dict()
            else:
                params['reg_case_date'] = self.reg_case_date
        if self.trpe:
            if hasattr(self.trpe, 'to_alipay_dict'):
                params['trpe'] = self.trpe.to_alipay_dict()
            else:
                params['trpe'] = self.trpe
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.un_perform_part:
            if hasattr(self.un_perform_part, 'to_alipay_dict'):
                params['un_perform_part'] = self.un_perform_part.to_alipay_dict()
            else:
                params['un_perform_part'] = self.un_perform_part
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PunishBreakInfo()
        if 'business_entity' in d:
            o.business_entity = d['business_entity']
        if 'card_num' in d:
            o.card_num = d['card_num']
        if 'case_code' in d:
            o.case_code = d['case_code']
        if 'court_name' in d:
            o.court_name = d['court_name']
        if 'disrupt_type_name' in d:
            o.disrupt_type_name = d['disrupt_type_name']
        if 'duty' in d:
            o.duty = d['duty']
        if 'gist_id' in d:
            o.gist_id = d['gist_id']
        if 'gist_unit' in d:
            o.gist_unit = d['gist_unit']
        if 'name' in d:
            o.name = d['name']
        if 'performance' in d:
            o.performance = d['performance']
        if 'performed_part' in d:
            o.performed_part = d['performed_part']
        if 'province' in d:
            o.province = d['province']
        if 'publish_date' in d:
            o.publish_date = d['publish_date']
        if 'reg_case_date' in d:
            o.reg_case_date = d['reg_case_date']
        if 'trpe' in d:
            o.trpe = d['trpe']
        if 'type' in d:
            o.type = d['type']
        if 'un_perform_part' in d:
            o.un_perform_part = d['un_perform_part']
        return o


