#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreativeActionProperty import CreativeActionProperty
from alipay.aop.api.domain.CreativeMaterial import CreativeMaterial


class AlipayDataDataserviceAdcampaignCreativeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignCreativeQueryResponse, self).__init__()
        self._action_property_list = None
        self._action_type = None
        self._ad_id = None
        self._ad_name = None
        self._click_track_url = None
        self._gmt_modified = None
        self._group_id = None
        self._group_name = None
        self._impression_track_url = None
        self._market_target_code = None
        self._market_target_name = None
        self._material_list = None
        self._plan_id = None
        self._plan_name = None
        self._principal_id = None
        self._scene_code = None
        self._smart_switch = None
        self._status = None
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
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def impression_track_url(self):
        return self._impression_track_url

    @impression_track_url.setter
    def impression_track_url(self, value):
        self._impression_track_url = value
    @property
    def market_target_code(self):
        return self._market_target_code

    @market_target_code.setter
    def market_target_code(self, value):
        self._market_target_code = value
    @property
    def market_target_name(self):
        return self._market_target_name

    @market_target_name.setter
    def market_target_name(self, value):
        self._market_target_name = value
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
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def smart_switch(self):
        return self._smart_switch

    @smart_switch.setter
    def smart_switch(self, value):
        self._smart_switch = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignCreativeQueryResponse, self).parse_response_content(response_content)
        if 'action_property_list' in response:
            self.action_property_list = response['action_property_list']
        if 'action_type' in response:
            self.action_type = response['action_type']
        if 'ad_id' in response:
            self.ad_id = response['ad_id']
        if 'ad_name' in response:
            self.ad_name = response['ad_name']
        if 'click_track_url' in response:
            self.click_track_url = response['click_track_url']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'group_name' in response:
            self.group_name = response['group_name']
        if 'impression_track_url' in response:
            self.impression_track_url = response['impression_track_url']
        if 'market_target_code' in response:
            self.market_target_code = response['market_target_code']
        if 'market_target_name' in response:
            self.market_target_name = response['market_target_name']
        if 'material_list' in response:
            self.material_list = response['material_list']
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'plan_name' in response:
            self.plan_name = response['plan_name']
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'smart_switch' in response:
            self.smart_switch = response['smart_switch']
        if 'status' in response:
            self.status = response['status']
        if 'template_id' in response:
            self.template_id = response['template_id']
