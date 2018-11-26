#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdMaterial import AdMaterial


class AdCreative(object):

    def __init__(self):
        self._ad_material_list = None
        self._ad_name = None
        self._group_id = None
        self._template_id = None

    @property
    def ad_material_list(self):
        return self._ad_material_list

    @ad_material_list.setter
    def ad_material_list(self, value):
        if isinstance(value, list):
            self._ad_material_list = list()
            for i in value:
                if isinstance(i, AdMaterial):
                    self._ad_material_list.append(i)
                else:
                    self._ad_material_list.append(AdMaterial.from_alipay_dict(i))
    @property
    def ad_name(self):
        return self._ad_name

    @ad_name.setter
    def ad_name(self, value):
        self._ad_name = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
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
        o = AdCreative()
        if 'ad_material_list' in d:
            o.ad_material_list = d['ad_material_list']
        if 'ad_name' in d:
            o.ad_name = d['ad_name']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


