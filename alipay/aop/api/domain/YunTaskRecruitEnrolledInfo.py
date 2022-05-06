#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.YunTaskVoucherTemplateInfo import YunTaskVoucherTemplateInfo


class YunTaskRecruitEnrolledInfo(object):

    def __init__(self):
        self._investor_logo = None
        self._investor_pid = None
        self._plan_id = None
        self._plan_name = None
        self._voucher_templates = None

    @property
    def investor_logo(self):
        return self._investor_logo

    @investor_logo.setter
    def investor_logo(self, value):
        self._investor_logo = value
    @property
    def investor_pid(self):
        return self._investor_pid

    @investor_pid.setter
    def investor_pid(self, value):
        self._investor_pid = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def voucher_templates(self):
        return self._voucher_templates

    @voucher_templates.setter
    def voucher_templates(self, value):
        if isinstance(value, list):
            self._voucher_templates = list()
            for i in value:
                if isinstance(i, YunTaskVoucherTemplateInfo):
                    self._voucher_templates.append(i)
                else:
                    self._voucher_templates.append(YunTaskVoucherTemplateInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.investor_logo:
            if hasattr(self.investor_logo, 'to_alipay_dict'):
                params['investor_logo'] = self.investor_logo.to_alipay_dict()
            else:
                params['investor_logo'] = self.investor_logo
        if self.investor_pid:
            if hasattr(self.investor_pid, 'to_alipay_dict'):
                params['investor_pid'] = self.investor_pid.to_alipay_dict()
            else:
                params['investor_pid'] = self.investor_pid
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.voucher_templates:
            if isinstance(self.voucher_templates, list):
                for i in range(0, len(self.voucher_templates)):
                    element = self.voucher_templates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_templates[i] = element.to_alipay_dict()
            if hasattr(self.voucher_templates, 'to_alipay_dict'):
                params['voucher_templates'] = self.voucher_templates.to_alipay_dict()
            else:
                params['voucher_templates'] = self.voucher_templates
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YunTaskRecruitEnrolledInfo()
        if 'investor_logo' in d:
            o.investor_logo = d['investor_logo']
        if 'investor_pid' in d:
            o.investor_pid = d['investor_pid']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'voucher_templates' in d:
            o.voucher_templates = d['voucher_templates']
        return o


