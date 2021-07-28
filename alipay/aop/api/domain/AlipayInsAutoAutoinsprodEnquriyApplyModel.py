#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.AgentOrganization import AgentOrganization
from alipay.aop.api.domain.AgentOrganization import AgentOrganization
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.ApplyBusinessCity import ApplyBusinessCity
from alipay.aop.api.domain.Car import Car
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsAutoAutoinsprodEnquriyApplyModel(object):

    def __init__(self):
        self._agent = None
        self._agent_organization = None
        self._agent_tech_organization = None
        self._agent_user_id = None
        self._applicant = None
        self._apply_business_city = None
        self._car = None
        self._car_owner = None
        self._city_code = None
        self._insured = None
        self._leads_id = None
        self._out_biz_no = None

    @property
    def agent(self):
        return self._agent

    @agent.setter
    def agent(self, value):
        if isinstance(value, InsPerson):
            self._agent = value
        else:
            self._agent = InsPerson.from_alipay_dict(value)
    @property
    def agent_organization(self):
        return self._agent_organization

    @agent_organization.setter
    def agent_organization(self, value):
        if isinstance(value, AgentOrganization):
            self._agent_organization = value
        else:
            self._agent_organization = AgentOrganization.from_alipay_dict(value)
    @property
    def agent_tech_organization(self):
        return self._agent_tech_organization

    @agent_tech_organization.setter
    def agent_tech_organization(self, value):
        if isinstance(value, AgentOrganization):
            self._agent_tech_organization = value
        else:
            self._agent_tech_organization = AgentOrganization.from_alipay_dict(value)
    @property
    def agent_user_id(self):
        return self._agent_user_id

    @agent_user_id.setter
    def agent_user_id(self, value):
        self._agent_user_id = value
    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, InsPerson):
            self._applicant = value
        else:
            self._applicant = InsPerson.from_alipay_dict(value)
    @property
    def apply_business_city(self):
        return self._apply_business_city

    @apply_business_city.setter
    def apply_business_city(self, value):
        if isinstance(value, ApplyBusinessCity):
            self._apply_business_city = value
        else:
            self._apply_business_city = ApplyBusinessCity.from_alipay_dict(value)
    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        if isinstance(value, Car):
            self._car = value
        else:
            self._car = Car.from_alipay_dict(value)
    @property
    def car_owner(self):
        return self._car_owner

    @car_owner.setter
    def car_owner(self, value):
        if isinstance(value, InsPerson):
            self._car_owner = value
        else:
            self._car_owner = InsPerson.from_alipay_dict(value)
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def insured(self):
        return self._insured

    @insured.setter
    def insured(self, value):
        if isinstance(value, InsPerson):
            self._insured = value
        else:
            self._insured = InsPerson.from_alipay_dict(value)
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent:
            if hasattr(self.agent, 'to_alipay_dict'):
                params['agent'] = self.agent.to_alipay_dict()
            else:
                params['agent'] = self.agent
        if self.agent_organization:
            if hasattr(self.agent_organization, 'to_alipay_dict'):
                params['agent_organization'] = self.agent_organization.to_alipay_dict()
            else:
                params['agent_organization'] = self.agent_organization
        if self.agent_tech_organization:
            if hasattr(self.agent_tech_organization, 'to_alipay_dict'):
                params['agent_tech_organization'] = self.agent_tech_organization.to_alipay_dict()
            else:
                params['agent_tech_organization'] = self.agent_tech_organization
        if self.agent_user_id:
            if hasattr(self.agent_user_id, 'to_alipay_dict'):
                params['agent_user_id'] = self.agent_user_id.to_alipay_dict()
            else:
                params['agent_user_id'] = self.agent_user_id
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.apply_business_city:
            if hasattr(self.apply_business_city, 'to_alipay_dict'):
                params['apply_business_city'] = self.apply_business_city.to_alipay_dict()
            else:
                params['apply_business_city'] = self.apply_business_city
        if self.car:
            if hasattr(self.car, 'to_alipay_dict'):
                params['car'] = self.car.to_alipay_dict()
            else:
                params['car'] = self.car
        if self.car_owner:
            if hasattr(self.car_owner, 'to_alipay_dict'):
                params['car_owner'] = self.car_owner.to_alipay_dict()
            else:
                params['car_owner'] = self.car_owner
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.insured:
            if hasattr(self.insured, 'to_alipay_dict'):
                params['insured'] = self.insured.to_alipay_dict()
            else:
                params['insured'] = self.insured
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoAutoinsprodEnquriyApplyModel()
        if 'agent' in d:
            o.agent = d['agent']
        if 'agent_organization' in d:
            o.agent_organization = d['agent_organization']
        if 'agent_tech_organization' in d:
            o.agent_tech_organization = d['agent_tech_organization']
        if 'agent_user_id' in d:
            o.agent_user_id = d['agent_user_id']
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'apply_business_city' in d:
            o.apply_business_city = d['apply_business_city']
        if 'car' in d:
            o.car = d['car']
        if 'car_owner' in d:
            o.car_owner = d['car_owner']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'insured' in d:
            o.insured = d['insured']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


