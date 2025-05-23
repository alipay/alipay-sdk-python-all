#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenLbsEntry import OpenLbsEntry


class AlipayDataDataserviceAdcampaignGroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignGroupQueryResponse, self).__init__()
        self._age_list = None
        self._asset = None
        self._behavior_list = None
        self._bid_type = None
        self._boost_budget = None
        self._boost_end_date = None
        self._boost_id = None
        self._boost_start_date = None
        self._city_level_list = None
        self._converted_event = None
        self._converted_event_grp = None
        self._converted_id = None
        self._district = None
        self._exclude_customized_crowd_list = None
        self._filter_converted_event_list = None
        self._filter_converted_scope = None
        self._filter_converted_time_range = None
        self._gender_list = None
        self._gmt_modified = None
        self._group_budget = None
        self._group_charge = None
        self._group_id = None
        self._group_inherit = None
        self._group_name = None
        self._group_status = None
        self._include_customized_crowd_list = None
        self._intelligent_target_switch = None
        self._interest_list = None
        self._lbs_list = None
        self._market_target_code = None
        self._market_target_name = None
        self._one_boost_status = None
        self._os_list = None
        self._plan_id = None
        self._plan_name = None
        self._principal_id = None
        self._region_list = None
        self._region_type = None
        self._scene_code = None
        self._target_cpa = None
        self._theme_crowd_list = None

    @property
    def age_list(self):
        return self._age_list

    @age_list.setter
    def age_list(self, value):
        if isinstance(value, list):
            self._age_list = list()
            for i in value:
                self._age_list.append(i)
    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, value):
        self._asset = value
    @property
    def behavior_list(self):
        return self._behavior_list

    @behavior_list.setter
    def behavior_list(self, value):
        if isinstance(value, list):
            self._behavior_list = list()
            for i in value:
                self._behavior_list.append(i)
    @property
    def bid_type(self):
        return self._bid_type

    @bid_type.setter
    def bid_type(self, value):
        self._bid_type = value
    @property
    def boost_budget(self):
        return self._boost_budget

    @boost_budget.setter
    def boost_budget(self, value):
        self._boost_budget = value
    @property
    def boost_end_date(self):
        return self._boost_end_date

    @boost_end_date.setter
    def boost_end_date(self, value):
        self._boost_end_date = value
    @property
    def boost_id(self):
        return self._boost_id

    @boost_id.setter
    def boost_id(self, value):
        self._boost_id = value
    @property
    def boost_start_date(self):
        return self._boost_start_date

    @boost_start_date.setter
    def boost_start_date(self, value):
        self._boost_start_date = value
    @property
    def city_level_list(self):
        return self._city_level_list

    @city_level_list.setter
    def city_level_list(self, value):
        if isinstance(value, list):
            self._city_level_list = list()
            for i in value:
                self._city_level_list.append(i)
    @property
    def converted_event(self):
        return self._converted_event

    @converted_event.setter
    def converted_event(self, value):
        self._converted_event = value
    @property
    def converted_event_grp(self):
        return self._converted_event_grp

    @converted_event_grp.setter
    def converted_event_grp(self, value):
        self._converted_event_grp = value
    @property
    def converted_id(self):
        return self._converted_id

    @converted_id.setter
    def converted_id(self, value):
        self._converted_id = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def exclude_customized_crowd_list(self):
        return self._exclude_customized_crowd_list

    @exclude_customized_crowd_list.setter
    def exclude_customized_crowd_list(self, value):
        if isinstance(value, list):
            self._exclude_customized_crowd_list = list()
            for i in value:
                self._exclude_customized_crowd_list.append(i)
    @property
    def filter_converted_event_list(self):
        return self._filter_converted_event_list

    @filter_converted_event_list.setter
    def filter_converted_event_list(self, value):
        if isinstance(value, list):
            self._filter_converted_event_list = list()
            for i in value:
                self._filter_converted_event_list.append(i)
    @property
    def filter_converted_scope(self):
        return self._filter_converted_scope

    @filter_converted_scope.setter
    def filter_converted_scope(self, value):
        self._filter_converted_scope = value
    @property
    def filter_converted_time_range(self):
        return self._filter_converted_time_range

    @filter_converted_time_range.setter
    def filter_converted_time_range(self, value):
        self._filter_converted_time_range = value
    @property
    def gender_list(self):
        return self._gender_list

    @gender_list.setter
    def gender_list(self, value):
        if isinstance(value, list):
            self._gender_list = list()
            for i in value:
                self._gender_list.append(i)
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def group_budget(self):
        return self._group_budget

    @group_budget.setter
    def group_budget(self, value):
        self._group_budget = value
    @property
    def group_charge(self):
        return self._group_charge

    @group_charge.setter
    def group_charge(self, value):
        self._group_charge = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_inherit(self):
        return self._group_inherit

    @group_inherit.setter
    def group_inherit(self, value):
        self._group_inherit = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def group_status(self):
        return self._group_status

    @group_status.setter
    def group_status(self, value):
        self._group_status = value
    @property
    def include_customized_crowd_list(self):
        return self._include_customized_crowd_list

    @include_customized_crowd_list.setter
    def include_customized_crowd_list(self, value):
        if isinstance(value, list):
            self._include_customized_crowd_list = list()
            for i in value:
                self._include_customized_crowd_list.append(i)
    @property
    def intelligent_target_switch(self):
        return self._intelligent_target_switch

    @intelligent_target_switch.setter
    def intelligent_target_switch(self, value):
        self._intelligent_target_switch = value
    @property
    def interest_list(self):
        return self._interest_list

    @interest_list.setter
    def interest_list(self, value):
        if isinstance(value, list):
            self._interest_list = list()
            for i in value:
                self._interest_list.append(i)
    @property
    def lbs_list(self):
        return self._lbs_list

    @lbs_list.setter
    def lbs_list(self, value):
        if isinstance(value, list):
            self._lbs_list = list()
            for i in value:
                if isinstance(i, OpenLbsEntry):
                    self._lbs_list.append(i)
                else:
                    self._lbs_list.append(OpenLbsEntry.from_alipay_dict(i))
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
    def one_boost_status(self):
        return self._one_boost_status

    @one_boost_status.setter
    def one_boost_status(self, value):
        self._one_boost_status = value
    @property
    def os_list(self):
        return self._os_list

    @os_list.setter
    def os_list(self, value):
        if isinstance(value, list):
            self._os_list = list()
            for i in value:
                self._os_list.append(i)
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
    def region_list(self):
        return self._region_list

    @region_list.setter
    def region_list(self, value):
        if isinstance(value, list):
            self._region_list = list()
            for i in value:
                self._region_list.append(i)
    @property
    def region_type(self):
        return self._region_type

    @region_type.setter
    def region_type(self, value):
        self._region_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def target_cpa(self):
        return self._target_cpa

    @target_cpa.setter
    def target_cpa(self, value):
        self._target_cpa = value
    @property
    def theme_crowd_list(self):
        return self._theme_crowd_list

    @theme_crowd_list.setter
    def theme_crowd_list(self, value):
        if isinstance(value, list):
            self._theme_crowd_list = list()
            for i in value:
                self._theme_crowd_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignGroupQueryResponse, self).parse_response_content(response_content)
        if 'age_list' in response:
            self.age_list = response['age_list']
        if 'asset' in response:
            self.asset = response['asset']
        if 'behavior_list' in response:
            self.behavior_list = response['behavior_list']
        if 'bid_type' in response:
            self.bid_type = response['bid_type']
        if 'boost_budget' in response:
            self.boost_budget = response['boost_budget']
        if 'boost_end_date' in response:
            self.boost_end_date = response['boost_end_date']
        if 'boost_id' in response:
            self.boost_id = response['boost_id']
        if 'boost_start_date' in response:
            self.boost_start_date = response['boost_start_date']
        if 'city_level_list' in response:
            self.city_level_list = response['city_level_list']
        if 'converted_event' in response:
            self.converted_event = response['converted_event']
        if 'converted_event_grp' in response:
            self.converted_event_grp = response['converted_event_grp']
        if 'converted_id' in response:
            self.converted_id = response['converted_id']
        if 'district' in response:
            self.district = response['district']
        if 'exclude_customized_crowd_list' in response:
            self.exclude_customized_crowd_list = response['exclude_customized_crowd_list']
        if 'filter_converted_event_list' in response:
            self.filter_converted_event_list = response['filter_converted_event_list']
        if 'filter_converted_scope' in response:
            self.filter_converted_scope = response['filter_converted_scope']
        if 'filter_converted_time_range' in response:
            self.filter_converted_time_range = response['filter_converted_time_range']
        if 'gender_list' in response:
            self.gender_list = response['gender_list']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'group_budget' in response:
            self.group_budget = response['group_budget']
        if 'group_charge' in response:
            self.group_charge = response['group_charge']
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'group_inherit' in response:
            self.group_inherit = response['group_inherit']
        if 'group_name' in response:
            self.group_name = response['group_name']
        if 'group_status' in response:
            self.group_status = response['group_status']
        if 'include_customized_crowd_list' in response:
            self.include_customized_crowd_list = response['include_customized_crowd_list']
        if 'intelligent_target_switch' in response:
            self.intelligent_target_switch = response['intelligent_target_switch']
        if 'interest_list' in response:
            self.interest_list = response['interest_list']
        if 'lbs_list' in response:
            self.lbs_list = response['lbs_list']
        if 'market_target_code' in response:
            self.market_target_code = response['market_target_code']
        if 'market_target_name' in response:
            self.market_target_name = response['market_target_name']
        if 'one_boost_status' in response:
            self.one_boost_status = response['one_boost_status']
        if 'os_list' in response:
            self.os_list = response['os_list']
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'plan_name' in response:
            self.plan_name = response['plan_name']
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
        if 'region_list' in response:
            self.region_list = response['region_list']
        if 'region_type' in response:
            self.region_type = response['region_type']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'target_cpa' in response:
            self.target_cpa = response['target_cpa']
        if 'theme_crowd_list' in response:
            self.theme_crowd_list = response['theme_crowd_list']
