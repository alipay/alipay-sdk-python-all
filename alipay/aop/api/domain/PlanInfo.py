#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.YunTaskVoucherTemplateInfo import YunTaskVoucherTemplateInfo


class PlanInfo(object):

    def __init__(self):
        self._logo = None
        self._plan_id = None
        self._plan_name = None
        self._voucher_template_list = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
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
    def voucher_template_list(self):
        return self._voucher_template_list

    @voucher_template_list.setter
    def voucher_template_list(self, value):
        if isinstance(value, list):
            self._voucher_template_list = list()
            for i in value:
                if isinstance(i, YunTaskVoucherTemplateInfo):
                    self._voucher_template_list.append(i)
                else:
                    self._voucher_template_list.append(YunTaskVoucherTemplateInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
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
        if self.voucher_template_list:
            if isinstance(self.voucher_template_list, list):
                for i in range(0, len(self.voucher_template_list)):
                    element = self.voucher_template_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_template_list[i] = element.to_alipay_dict()
            if hasattr(self.voucher_template_list, 'to_alipay_dict'):
                params['voucher_template_list'] = self.voucher_template_list.to_alipay_dict()
            else:
                params['voucher_template_list'] = self.voucher_template_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlanInfo()
        if 'logo' in d:
            o.logo = d['logo']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'voucher_template_list' in d:
            o.voucher_template_list = d['voucher_template_list']
        return o


