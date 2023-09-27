#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsureEmployee import InsureEmployee
from alipay.aop.api.domain.InsureCompany import InsureCompany
from alipay.aop.api.domain.InsurePartnerOrganization import InsurePartnerOrganization


class EmployeeInsureDomainEvent(object):

    def __init__(self):
        self._employee = None
        self._event_place = None
        self._event_time = None
        self._event_type = None
        self._merchant = None
        self._partner_organization = None
        self._product_plan_id = None

    @property
    def employee(self):
        return self._employee

    @employee.setter
    def employee(self, value):
        if isinstance(value, InsureEmployee):
            self._employee = value
        else:
            self._employee = InsureEmployee.from_alipay_dict(value)
    @property
    def event_place(self):
        return self._event_place

    @event_place.setter
    def event_place(self, value):
        self._event_place = value
    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, InsureCompany):
            self._merchant = value
        else:
            self._merchant = InsureCompany.from_alipay_dict(value)
    @property
    def partner_organization(self):
        return self._partner_organization

    @partner_organization.setter
    def partner_organization(self, value):
        if isinstance(value, InsurePartnerOrganization):
            self._partner_organization = value
        else:
            self._partner_organization = InsurePartnerOrganization.from_alipay_dict(value)
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee:
            if hasattr(self.employee, 'to_alipay_dict'):
                params['employee'] = self.employee.to_alipay_dict()
            else:
                params['employee'] = self.employee
        if self.event_place:
            if hasattr(self.event_place, 'to_alipay_dict'):
                params['event_place'] = self.event_place.to_alipay_dict()
            else:
                params['event_place'] = self.event_place
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.partner_organization:
            if hasattr(self.partner_organization, 'to_alipay_dict'):
                params['partner_organization'] = self.partner_organization.to_alipay_dict()
            else:
                params['partner_organization'] = self.partner_organization
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EmployeeInsureDomainEvent()
        if 'employee' in d:
            o.employee = d['employee']
        if 'event_place' in d:
            o.event_place = d['event_place']
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'partner_organization' in d:
            o.partner_organization = d['partner_organization']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        return o


