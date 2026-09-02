#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssistantCompanySimpleInfo import AssistantCompanySimpleInfo


class ZhimaCreditEpAssistantMemberzptaskSubmitModel(object):

    def __init__(self):
        self._company_info_list = None
        self._out_biz_no = None
        self._partner_corp_id = None
        self._partner_corp_name = None
        self._partner_user_id = None
        self._task_type = None

    @property
    def company_info_list(self):
        return self._company_info_list

    @company_info_list.setter
    def company_info_list(self, value):
        if isinstance(value, list):
            self._company_info_list = list()
            for i in value:
                if isinstance(i, AssistantCompanySimpleInfo):
                    self._company_info_list.append(i)
                else:
                    self._company_info_list.append(AssistantCompanySimpleInfo.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_corp_id(self):
        return self._partner_corp_id

    @partner_corp_id.setter
    def partner_corp_id(self, value):
        self._partner_corp_id = value
    @property
    def partner_corp_name(self):
        return self._partner_corp_name

    @partner_corp_name.setter
    def partner_corp_name(self, value):
        self._partner_corp_name = value
    @property
    def partner_user_id(self):
        return self._partner_user_id

    @partner_user_id.setter
    def partner_user_id(self, value):
        self._partner_user_id = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_info_list:
            if isinstance(self.company_info_list, list):
                for i in range(0, len(self.company_info_list)):
                    element = self.company_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.company_info_list[i] = element.to_alipay_dict()
            if hasattr(self.company_info_list, 'to_alipay_dict'):
                params['company_info_list'] = self.company_info_list.to_alipay_dict()
            else:
                params['company_info_list'] = self.company_info_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_corp_id:
            if hasattr(self.partner_corp_id, 'to_alipay_dict'):
                params['partner_corp_id'] = self.partner_corp_id.to_alipay_dict()
            else:
                params['partner_corp_id'] = self.partner_corp_id
        if self.partner_corp_name:
            if hasattr(self.partner_corp_name, 'to_alipay_dict'):
                params['partner_corp_name'] = self.partner_corp_name.to_alipay_dict()
            else:
                params['partner_corp_name'] = self.partner_corp_name
        if self.partner_user_id:
            if hasattr(self.partner_user_id, 'to_alipay_dict'):
                params['partner_user_id'] = self.partner_user_id.to_alipay_dict()
            else:
                params['partner_user_id'] = self.partner_user_id
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAssistantMemberzptaskSubmitModel()
        if 'company_info_list' in d:
            o.company_info_list = d['company_info_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_corp_id' in d:
            o.partner_corp_id = d['partner_corp_id']
        if 'partner_corp_name' in d:
            o.partner_corp_name = d['partner_corp_name']
        if 'partner_user_id' in d:
            o.partner_user_id = d['partner_user_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


