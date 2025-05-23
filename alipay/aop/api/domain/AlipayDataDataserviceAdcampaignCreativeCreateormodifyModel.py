#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreativeActionProperty import CreativeActionProperty
from alipay.aop.api.domain.CreativeMaterial import CreativeMaterial


class AlipayDataDataserviceAdcampaignCreativeCreateormodifyModel(object):

    def __init__(self):
        self._action_property_list = None
        self._action_type = None
        self._ad_id = None
        self._ad_name = None
        self._click_track_url = None
        self._group_id = None
        self._impression_track_url = None
        self._material_list = None
        self._principal_tag = None
        self._smart_switch = None
        self._template_id = None

    @property
    def action_property_list(self):
        return self._action_property_list

    @action_property_list.setter
    def action_property_list(self, value):
        if isinstance(value, list):
            self._action_property_list = list()
            for i in value:
                if isinstance(i, CreativeActionProperty):
                    self._action_property_list.append(i)
                else:
                    self._action_property_list.append(CreativeActionProperty.from_alipay_dict(i))
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def ad_id(self):
        return self._ad_id

    @ad_id.setter
    def ad_id(self, value):
        self._ad_id = value
    @property
    def ad_name(self):
        return self._ad_name

    @ad_name.setter
    def ad_name(self, value):
        self._ad_name = value
    @property
    def click_track_url(self):
        return self._click_track_url

    @click_track_url.setter
    def click_track_url(self, value):
        self._click_track_url = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def impression_track_url(self):
        return self._impression_track_url

    @impression_track_url.setter
    def impression_track_url(self, value):
        self._impression_track_url = value
    @property
    def material_list(self):
        return self._material_list

    @material_list.setter
    def material_list(self, value):
        if isinstance(value, list):
            self._material_list = list()
            for i in value:
                if isinstance(i, CreativeMaterial):
                    self._material_list.append(i)
                else:
                    self._material_list.append(CreativeMaterial.from_alipay_dict(i))
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def smart_switch(self):
        return self._smart_switch

    @smart_switch.setter
    def smart_switch(self, value):
        self._smart_switch = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_property_list:
            if isinstance(self.action_property_list, list):
                for i in range(0, len(self.action_property_list)):
                    element = self.action_property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.action_property_list[i] = element.to_alipay_dict()
            if hasattr(self.action_property_list, 'to_alipay_dict'):
                params['action_property_list'] = self.action_property_list.to_alipay_dict()
            else:
                params['action_property_list'] = self.action_property_list
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.ad_id:
            if hasattr(self.ad_id, 'to_alipay_dict'):
                params['ad_id'] = self.ad_id.to_alipay_dict()
            else:
                params['ad_id'] = self.ad_id
        if self.ad_name:
            if hasattr(self.ad_name, 'to_alipay_dict'):
                params['ad_name'] = self.ad_name.to_alipay_dict()
            else:
                params['ad_name'] = self.ad_name
        if self.click_track_url:
            if hasattr(self.click_track_url, 'to_alipay_dict'):
                params['click_track_url'] = self.click_track_url.to_alipay_dict()
            else:
                params['click_track_url'] = self.click_track_url
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.impression_track_url:
            if hasattr(self.impression_track_url, 'to_alipay_dict'):
                params['impression_track_url'] = self.impression_track_url.to_alipay_dict()
            else:
                params['impression_track_url'] = self.impression_track_url
        if self.material_list:
            if isinstance(self.material_list, list):
                for i in range(0, len(self.material_list)):
                    element = self.material_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_list[i] = element.to_alipay_dict()
            if hasattr(self.material_list, 'to_alipay_dict'):
                params['material_list'] = self.material_list.to_alipay_dict()
            else:
                params['material_list'] = self.material_list
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.smart_switch:
            if hasattr(self.smart_switch, 'to_alipay_dict'):
                params['smart_switch'] = self.smart_switch.to_alipay_dict()
            else:
                params['smart_switch'] = self.smart_switch
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
        o = AlipayDataDataserviceAdcampaignCreativeCreateormodifyModel()
        if 'action_property_list' in d:
            o.action_property_list = d['action_property_list']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'ad_id' in d:
            o.ad_id = d['ad_id']
        if 'ad_name' in d:
            o.ad_name = d['ad_name']
        if 'click_track_url' in d:
            o.click_track_url = d['click_track_url']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'impression_track_url' in d:
            o.impression_track_url = d['impression_track_url']
        if 'material_list' in d:
            o.material_list = d['material_list']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'smart_switch' in d:
            o.smart_switch = d['smart_switch']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


