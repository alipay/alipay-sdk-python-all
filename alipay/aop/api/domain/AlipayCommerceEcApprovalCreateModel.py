#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApprovalTravelerDTO import ApprovalTravelerDTO
from alipay.aop.api.domain.ApprovalTripDTO import ApprovalTripDTO


class AlipayCommerceEcApprovalCreateModel(object):

    def __init__(self):
        self._apply_finish_time = None
        self._apply_start_time = None
        self._category = None
        self._employee_id = None
        self._enterprise_id = None
        self._expense_type_sub_category = None
        self._institution_id_list = None
        self._payment_type = None
        self._platform_approval_id = None
        self._purpose = None
        self._scene = None
        self._traveler_list = None
        self._trip_info_list = None

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
    def expense_type_sub_category(self):
        return self._expense_type_sub_category

    @expense_type_sub_category.setter
    def expense_type_sub_category(self, value):
        self._expense_type_sub_category = value
    @property
    def institution_id_list(self):
        return self._institution_id_list

    @institution_id_list.setter
    def institution_id_list(self, value):
        if isinstance(value, list):
            self._institution_id_list = list()
            for i in value:
                self._institution_id_list.append(i)
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
    @property
    def traveler_list(self):
        return self._traveler_list

    @traveler_list.setter
    def traveler_list(self, value):
        if isinstance(value, list):
            self._traveler_list = list()
            for i in value:
                if isinstance(i, ApprovalTravelerDTO):
                    self._traveler_list.append(i)
                else:
                    self._traveler_list.append(ApprovalTravelerDTO.from_alipay_dict(i))
    @property
    def trip_info_list(self):
        return self._trip_info_list

    @trip_info_list.setter
    def trip_info_list(self, value):
        if isinstance(value, list):
            self._trip_info_list = list()
            for i in value:
                if isinstance(i, ApprovalTripDTO):
                    self._trip_info_list.append(i)
                else:
                    self._trip_info_list.append(ApprovalTripDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apply_finish_time:
            if hasattr(self.apply_finish_time, 'to_alipay_dict'):
                params['apply_finish_time'] = self.apply_finish_time.to_alipay_dict()
            else:
                params['apply_finish_time'] = self.apply_finish_time
        if self.apply_start_time:
            if hasattr(self.apply_start_time, 'to_alipay_dict'):
                params['apply_start_time'] = self.apply_start_time.to_alipay_dict()
            else:
                params['apply_start_time'] = self.apply_start_time
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.expense_type_sub_category:
            if hasattr(self.expense_type_sub_category, 'to_alipay_dict'):
                params['expense_type_sub_category'] = self.expense_type_sub_category.to_alipay_dict()
            else:
                params['expense_type_sub_category'] = self.expense_type_sub_category
        if self.institution_id_list:
            if isinstance(self.institution_id_list, list):
                for i in range(0, len(self.institution_id_list)):
                    element = self.institution_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.institution_id_list[i] = element.to_alipay_dict()
            if hasattr(self.institution_id_list, 'to_alipay_dict'):
                params['institution_id_list'] = self.institution_id_list.to_alipay_dict()
            else:
                params['institution_id_list'] = self.institution_id_list
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.platform_approval_id:
            if hasattr(self.platform_approval_id, 'to_alipay_dict'):
                params['platform_approval_id'] = self.platform_approval_id.to_alipay_dict()
            else:
                params['platform_approval_id'] = self.platform_approval_id
        if self.purpose:
            if hasattr(self.purpose, 'to_alipay_dict'):
                params['purpose'] = self.purpose.to_alipay_dict()
            else:
                params['purpose'] = self.purpose
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.traveler_list:
            if isinstance(self.traveler_list, list):
                for i in range(0, len(self.traveler_list)):
                    element = self.traveler_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.traveler_list[i] = element.to_alipay_dict()
            if hasattr(self.traveler_list, 'to_alipay_dict'):
                params['traveler_list'] = self.traveler_list.to_alipay_dict()
            else:
                params['traveler_list'] = self.traveler_list
        if self.trip_info_list:
            if isinstance(self.trip_info_list, list):
                for i in range(0, len(self.trip_info_list)):
                    element = self.trip_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trip_info_list[i] = element.to_alipay_dict()
            if hasattr(self.trip_info_list, 'to_alipay_dict'):
                params['trip_info_list'] = self.trip_info_list.to_alipay_dict()
            else:
                params['trip_info_list'] = self.trip_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcApprovalCreateModel()
        if 'apply_finish_time' in d:
            o.apply_finish_time = d['apply_finish_time']
        if 'apply_start_time' in d:
            o.apply_start_time = d['apply_start_time']
        if 'category' in d:
            o.category = d['category']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'expense_type_sub_category' in d:
            o.expense_type_sub_category = d['expense_type_sub_category']
        if 'institution_id_list' in d:
            o.institution_id_list = d['institution_id_list']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'platform_approval_id' in d:
            o.platform_approval_id = d['platform_approval_id']
        if 'purpose' in d:
            o.purpose = d['purpose']
        if 'scene' in d:
            o.scene = d['scene']
        if 'traveler_list' in d:
            o.traveler_list = d['traveler_list']
        if 'trip_info_list' in d:
            o.trip_info_list = d['trip_info_list']
        return o


