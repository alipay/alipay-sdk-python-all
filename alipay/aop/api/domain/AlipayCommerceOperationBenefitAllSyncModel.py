#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityBenefit import ActivityBenefit
from alipay.aop.api.domain.PrivilegeBenefit import PrivilegeBenefit


class AlipayCommerceOperationBenefitAllSyncModel(object):

    def __init__(self):
        self._activity_benefit_list = None
        self._privilege_benefit_list = None
        self._template_id = None

    @property
    def activity_benefit_list(self):
        return self._activity_benefit_list

    @activity_benefit_list.setter
    def activity_benefit_list(self, value):
        if isinstance(value, list):
            self._activity_benefit_list = list()
            for i in value:
                if isinstance(i, ActivityBenefit):
                    self._activity_benefit_list.append(i)
                else:
                    self._activity_benefit_list.append(ActivityBenefit.from_alipay_dict(i))
    @property
    def privilege_benefit_list(self):
        return self._privilege_benefit_list

    @privilege_benefit_list.setter
    def privilege_benefit_list(self, value):
        if isinstance(value, list):
            self._privilege_benefit_list = list()
            for i in value:
                if isinstance(i, PrivilegeBenefit):
                    self._privilege_benefit_list.append(i)
                else:
                    self._privilege_benefit_list.append(PrivilegeBenefit.from_alipay_dict(i))
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_benefit_list:
            if isinstance(self.activity_benefit_list, list):
                for i in range(0, len(self.activity_benefit_list)):
                    element = self.activity_benefit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_benefit_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_benefit_list, 'to_alipay_dict'):
                params['activity_benefit_list'] = self.activity_benefit_list.to_alipay_dict()
            else:
                params['activity_benefit_list'] = self.activity_benefit_list
        if self.privilege_benefit_list:
            if isinstance(self.privilege_benefit_list, list):
                for i in range(0, len(self.privilege_benefit_list)):
                    element = self.privilege_benefit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.privilege_benefit_list[i] = element.to_alipay_dict()
            if hasattr(self.privilege_benefit_list, 'to_alipay_dict'):
                params['privilege_benefit_list'] = self.privilege_benefit_list.to_alipay_dict()
            else:
                params['privilege_benefit_list'] = self.privilege_benefit_list
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationBenefitAllSyncModel()
        if 'activity_benefit_list' in d:
            o.activity_benefit_list = d['activity_benefit_list']
        if 'privilege_benefit_list' in d:
            o.privilege_benefit_list = d['privilege_benefit_list']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


