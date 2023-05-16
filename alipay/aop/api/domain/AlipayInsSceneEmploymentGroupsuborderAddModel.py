#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsEmployee import InsEmployee


class AlipayInsSceneEmploymentGroupsuborderAddModel(object):

    def __init__(self):
        self._employee_list = None
        self._out_biz_no = None
        self._partner_org_id = None
        self._scene_code = None
        self._summary_order_no = None

    @property
    def employee_list(self):
        return self._employee_list

    @employee_list.setter
    def employee_list(self, value):
        if isinstance(value, list):
            self._employee_list = list()
            for i in value:
                if isinstance(i, InsEmployee):
                    self._employee_list.append(i)
                else:
                    self._employee_list.append(InsEmployee.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def summary_order_no(self):
        return self._summary_order_no

    @summary_order_no.setter
    def summary_order_no(self, value):
        self._summary_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_list:
            if isinstance(self.employee_list, list):
                for i in range(0, len(self.employee_list)):
                    element = self.employee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.employee_list[i] = element.to_alipay_dict()
            if hasattr(self.employee_list, 'to_alipay_dict'):
                params['employee_list'] = self.employee_list.to_alipay_dict()
            else:
                params['employee_list'] = self.employee_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.summary_order_no:
            if hasattr(self.summary_order_no, 'to_alipay_dict'):
                params['summary_order_no'] = self.summary_order_no.to_alipay_dict()
            else:
                params['summary_order_no'] = self.summary_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEmploymentGroupsuborderAddModel()
        if 'employee_list' in d:
            o.employee_list = d['employee_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'summary_order_no' in d:
            o.summary_order_no = d['summary_order_no']
        return o


