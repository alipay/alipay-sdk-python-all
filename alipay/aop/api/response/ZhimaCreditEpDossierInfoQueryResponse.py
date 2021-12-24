#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpBranchInfo import EpBranchInfo


class ZhimaCreditEpDossierInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierInfoQueryResponse, self).__init__()
        self._business_period_from = None
        self._business_period_to = None
        self._business_scope = None
        self._charge_person_name = None
        self._charge_person_type = None
        self._employee_account = None
        self._ep_branch_list = None
        self._ep_cert_no = None
        self._ep_name = None
        self._ep_status = None
        self._ep_type = None
        self._ep_type_scope = None
        self._established_time = None
        self._industry = None
        self._location = None
        self._registered_address = None
        self._registered_capital = None
        self._registered_org = None
        self._social_security_account = None

    @property
    def business_period_from(self):
        return self._business_period_from

    @business_period_from.setter
    def business_period_from(self, value):
        self._business_period_from = value
    @property
    def business_period_to(self):
        return self._business_period_to

    @business_period_to.setter
    def business_period_to(self, value):
        self._business_period_to = value
    @property
    def business_scope(self):
        return self._business_scope

    @business_scope.setter
    def business_scope(self, value):
        self._business_scope = value
    @property
    def charge_person_name(self):
        return self._charge_person_name

    @charge_person_name.setter
    def charge_person_name(self, value):
        self._charge_person_name = value
    @property
    def charge_person_type(self):
        return self._charge_person_type

    @charge_person_type.setter
    def charge_person_type(self, value):
        self._charge_person_type = value
    @property
    def employee_account(self):
        return self._employee_account

    @employee_account.setter
    def employee_account(self, value):
        self._employee_account = value
    @property
    def ep_branch_list(self):
        return self._ep_branch_list

    @ep_branch_list.setter
    def ep_branch_list(self, value):
        if isinstance(value, list):
            self._ep_branch_list = list()
            for i in value:
                if isinstance(i, EpBranchInfo):
                    self._ep_branch_list.append(i)
                else:
                    self._ep_branch_list.append(EpBranchInfo.from_alipay_dict(i))
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def ep_status(self):
        return self._ep_status

    @ep_status.setter
    def ep_status(self, value):
        self._ep_status = value
    @property
    def ep_type(self):
        return self._ep_type

    @ep_type.setter
    def ep_type(self, value):
        self._ep_type = value
    @property
    def ep_type_scope(self):
        return self._ep_type_scope

    @ep_type_scope.setter
    def ep_type_scope(self, value):
        self._ep_type_scope = value
    @property
    def established_time(self):
        return self._established_time

    @established_time.setter
    def established_time(self, value):
        self._established_time = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def registered_address(self):
        return self._registered_address

    @registered_address.setter
    def registered_address(self, value):
        self._registered_address = value
    @property
    def registered_capital(self):
        return self._registered_capital

    @registered_capital.setter
    def registered_capital(self, value):
        self._registered_capital = value
    @property
    def registered_org(self):
        return self._registered_org

    @registered_org.setter
    def registered_org(self, value):
        self._registered_org = value
    @property
    def social_security_account(self):
        return self._social_security_account

    @social_security_account.setter
    def social_security_account(self, value):
        self._social_security_account = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierInfoQueryResponse, self).parse_response_content(response_content)
        if 'business_period_from' in response:
            self.business_period_from = response['business_period_from']
        if 'business_period_to' in response:
            self.business_period_to = response['business_period_to']
        if 'business_scope' in response:
            self.business_scope = response['business_scope']
        if 'charge_person_name' in response:
            self.charge_person_name = response['charge_person_name']
        if 'charge_person_type' in response:
            self.charge_person_type = response['charge_person_type']
        if 'employee_account' in response:
            self.employee_account = response['employee_account']
        if 'ep_branch_list' in response:
            self.ep_branch_list = response['ep_branch_list']
        if 'ep_cert_no' in response:
            self.ep_cert_no = response['ep_cert_no']
        if 'ep_name' in response:
            self.ep_name = response['ep_name']
        if 'ep_status' in response:
            self.ep_status = response['ep_status']
        if 'ep_type' in response:
            self.ep_type = response['ep_type']
        if 'ep_type_scope' in response:
            self.ep_type_scope = response['ep_type_scope']
        if 'established_time' in response:
            self.established_time = response['established_time']
        if 'industry' in response:
            self.industry = response['industry']
        if 'location' in response:
            self.location = response['location']
        if 'registered_address' in response:
            self.registered_address = response['registered_address']
        if 'registered_capital' in response:
            self.registered_capital = response['registered_capital']
        if 'registered_org' in response:
            self.registered_org = response['registered_org']
        if 'social_security_account' in response:
            self.social_security_account = response['social_security_account']
