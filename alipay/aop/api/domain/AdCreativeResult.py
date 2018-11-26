#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdMaterialResultDTO import AdMaterialResultDTO


class AdCreativeResult(object):

    def __init__(self):
        self._ad_id = None
        self._ad_material_list = None
        self._ad_name = None
        self._audit_status = None
        self._group_id = None
        self._status = None
        self._template_name = None

    @property
    def ad_id(self):
        return self._ad_id

    @ad_id.setter
    def ad_id(self, value):
        self._ad_id = value
    @property
    def ad_material_list(self):
        return self._ad_material_list

    @ad_material_list.setter
    def ad_material_list(self, value):
        if isinstance(value, list):
            self._ad_material_list = list()
            for i in value:
                if isinstance(i, AdMaterialResultDTO):
                    self._ad_material_list.append(i)
                else:
                    self._ad_material_list.append(AdMaterialResultDTO.from_alipay_dict(i))
    @property
    def ad_name(self):
        return self._ad_name

    @ad_name.setter
    def ad_name(self, value):
        self._ad_name = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_id:
            if hasattr(self.ad_id, 'to_alipay_dict'):
                params['ad_id'] = self.ad_id.to_alipay_dict()
            else:
                params['ad_id'] = self.ad_id
        if self.ad_material_list:
            if isinstance(self.ad_material_list, list):
                for i in range(0, len(self.ad_material_list)):
                    element = self.ad_material_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ad_material_list[i] = element.to_alipay_dict()
            if hasattr(self.ad_material_list, 'to_alipay_dict'):
                params['ad_material_list'] = self.ad_material_list.to_alipay_dict()
            else:
                params['ad_material_list'] = self.ad_material_list
        if self.ad_name:
            if hasattr(self.ad_name, 'to_alipay_dict'):
                params['ad_name'] = self.ad_name.to_alipay_dict()
            else:
                params['ad_name'] = self.ad_name
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdCreativeResult()
        if 'ad_id' in d:
            o.ad_id = d['ad_id']
        if 'ad_material_list' in d:
            o.ad_material_list = d['ad_material_list']
        if 'ad_name' in d:
            o.ad_name = d['ad_name']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'status' in d:
            o.status = d['status']
        if 'template_name' in d:
            o.template_name = d['template_name']
        return o


