#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityBenefit import ActivityBenefit
from alipay.aop.api.domain.PrivilegeBenefit import PrivilegeBenefit


class AlipayCommerceOperationBenefitSingleSyncModel(object):

    def __init__(self):
        self._action = None
        self._activity_benefit = None
        self._privilege_benefit = None
        self._template_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def activity_benefit(self):
        return self._activity_benefit

    @activity_benefit.setter
    def activity_benefit(self, value):
        if isinstance(value, ActivityBenefit):
            self._activity_benefit = value
        else:
            self._activity_benefit = ActivityBenefit.from_alipay_dict(value)
    @property
    def privilege_benefit(self):
        return self._privilege_benefit

    @privilege_benefit.setter
    def privilege_benefit(self, value):
        if isinstance(value, PrivilegeBenefit):
            self._privilege_benefit = value
        else:
            self._privilege_benefit = PrivilegeBenefit.from_alipay_dict(value)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.activity_benefit:
            if hasattr(self.activity_benefit, 'to_alipay_dict'):
                params['activity_benefit'] = self.activity_benefit.to_alipay_dict()
            else:
                params['activity_benefit'] = self.activity_benefit
        if self.privilege_benefit:
            if hasattr(self.privilege_benefit, 'to_alipay_dict'):
                params['privilege_benefit'] = self.privilege_benefit.to_alipay_dict()
            else:
                params['privilege_benefit'] = self.privilege_benefit
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
        o = AlipayCommerceOperationBenefitSingleSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'activity_benefit' in d:
            o.activity_benefit = d['activity_benefit']
        if 'privilege_benefit' in d:
            o.privilege_benefit = d['privilege_benefit']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


