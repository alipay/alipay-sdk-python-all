#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FundExtInfo import FundExtInfo


class InviteMemberBusinessParamsDTO(object):

    def __init__(self):
        self._employee_id = None
        self._fund_ext_info = None
        self._group_id_list = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def fund_ext_info(self):
        return self._fund_ext_info

    @fund_ext_info.setter
    def fund_ext_info(self, value):
        if isinstance(value, FundExtInfo):
            self._fund_ext_info = value
        else:
            self._fund_ext_info = FundExtInfo.from_alipay_dict(value)
    @property
    def group_id_list(self):
        return self._group_id_list

    @group_id_list.setter
    def group_id_list(self, value):
        if isinstance(value, list):
            self._group_id_list = list()
            for i in value:
                self._group_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.fund_ext_info:
            if hasattr(self.fund_ext_info, 'to_alipay_dict'):
                params['fund_ext_info'] = self.fund_ext_info.to_alipay_dict()
            else:
                params['fund_ext_info'] = self.fund_ext_info
        if self.group_id_list:
            if isinstance(self.group_id_list, list):
                for i in range(0, len(self.group_id_list)):
                    element = self.group_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_id_list, 'to_alipay_dict'):
                params['group_id_list'] = self.group_id_list.to_alipay_dict()
            else:
                params['group_id_list'] = self.group_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InviteMemberBusinessParamsDTO()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'fund_ext_info' in d:
            o.fund_ext_info = d['fund_ext_info']
        if 'group_id_list' in d:
            o.group_id_list = d['group_id_list']
        return o


