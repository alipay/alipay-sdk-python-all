#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ApprovalTravelerDTO import ApprovalTravelerDTO
from alipay.aop.api.domain.ApprovalTripDTO import ApprovalTripDTO


class AlipayCommerceEcApprovalQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcApprovalQueryResponse, self).__init__()
        self._apply_finish_time = None
        self._apply_start_time = None
        self._approval_result = None
        self._approval_traveler_dto_list = None
        self._approval_trip_dto_list = None
        self._category = None
        self._employee_id = None
        self._enterprise_id = None
        self._ex_json = None
        self._expense_type_sub_category = None
        self._out_ext = None
        self._payment_type = None
        self._platform_approval_id = None
        self._purpose = None
        self._scene = None

    @property
    def apply_finish_time(self):
        return self._apply_finish_time

    @apply_finish_time.setter
    def apply_finish_time(self, value):
        self._apply_finish_time = value
    @property
    def apply_start_time(self):
        return self._apply_start_time

    @apply_start_time.setter
    def apply_start_time(self, value):
        self._apply_start_time = value
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
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
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
    def ex_json(self):
        return self._ex_json

    @ex_json.setter
    def ex_json(self, value):
        self._ex_json = value
    @property
    def expense_type_sub_category(self):
        return self._expense_type_sub_category

    @expense_type_sub_category.setter
    def expense_type_sub_category(self, value):
        self._expense_type_sub_category = value
    @property
    def out_ext(self):
        return self._out_ext

    @out_ext.setter
    def out_ext(self, value):
        self._out_ext = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
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
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcApprovalQueryResponse, self).parse_response_content(response_content)
        if 'apply_finish_time' in response:
            self.apply_finish_time = response['apply_finish_time']
        if 'apply_start_time' in response:
            self.apply_start_time = response['apply_start_time']
        if 'approval_result' in response:
            self.approval_result = response['approval_result']
        if 'approval_traveler_dto_list' in response:
            self.approval_traveler_dto_list = response['approval_traveler_dto_list']
        if 'approval_trip_dto_list' in response:
            self.approval_trip_dto_list = response['approval_trip_dto_list']
        if 'category' in response:
            self.category = response['category']
        if 'employee_id' in response:
            self.employee_id = response['employee_id']
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'ex_json' in response:
            self.ex_json = response['ex_json']
        if 'expense_type_sub_category' in response:
            self.expense_type_sub_category = response['expense_type_sub_category']
        if 'out_ext' in response:
            self.out_ext = response['out_ext']
        if 'payment_type' in response:
            self.payment_type = response['payment_type']
        if 'platform_approval_id' in response:
            self.platform_approval_id = response['platform_approval_id']
        if 'purpose' in response:
            self.purpose = response['purpose']
        if 'scene' in response:
            self.scene = response['scene']
