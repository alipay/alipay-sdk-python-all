#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ApprovalTravelerDTO import ApprovalTravelerDTO
from alipay.aop.api.domain.ApprovalTripDTO import ApprovalTripDTO


class AlipayCommerceEcApprovalQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcApprovalQueryResponse, self).__init__()
        self._approval_result = None
        self._approval_traveler_dto_list = None
        self._approval_trip_dto_list = None
        self._employee_id = None
        self._enterprise_id = None
        self._platform_approval_id = None
        self._purpose = None

    @property
    def approval_result(self):
        return self._approval_result

    @approval_result.setter
    def approval_result(self, value):
        self._approval_result = value
    @property
    def approval_traveler_dto_list(self):
        return self._approval_traveler_dto_list

    @approval_traveler_dto_list.setter
    def approval_traveler_dto_list(self, value):
        if isinstance(value, list):
            self._approval_traveler_dto_list = list()
            for i in value:
                if isinstance(i, ApprovalTravelerDTO):
                    self._approval_traveler_dto_list.append(i)
                else:
                    self._approval_traveler_dto_list.append(ApprovalTravelerDTO.from_alipay_dict(i))
    @property
    def approval_trip_dto_list(self):
        return self._approval_trip_dto_list

    @approval_trip_dto_list.setter
    def approval_trip_dto_list(self, value):
        if isinstance(value, list):
            self._approval_trip_dto_list = list()
            for i in value:
                if isinstance(i, ApprovalTripDTO):
                    self._approval_trip_dto_list.append(i)
                else:
                    self._approval_trip_dto_list.append(ApprovalTripDTO.from_alipay_dict(i))
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def platform_approval_id(self):
        return self._platform_approval_id

    @platform_approval_id.setter
    def platform_approval_id(self, value):
        self._platform_approval_id = value
    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, value):
        self._purpose = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcApprovalQueryResponse, self).parse_response_content(response_content)
        if 'approval_result' in response:
            self.approval_result = response['approval_result']
        if 'approval_traveler_dto_list' in response:
            self.approval_traveler_dto_list = response['approval_traveler_dto_list']
        if 'approval_trip_dto_list' in response:
            self.approval_trip_dto_list = response['approval_trip_dto_list']
        if 'employee_id' in response:
            self.employee_id = response['employee_id']
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'platform_approval_id' in response:
            self.platform_approval_id = response['platform_approval_id']
        if 'purpose' in response:
            self.purpose = response['purpose']
