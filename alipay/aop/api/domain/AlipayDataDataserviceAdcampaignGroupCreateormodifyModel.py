#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenLbsEntry import OpenLbsEntry


class AlipayDataDataserviceAdcampaignGroupCreateormodifyModel(object):

    def __init__(self):
        self._age_list = None
        self._asset = None
        self._behavior_list = None
        self._bid_type = None
        self._boost_budget = None
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
        self._group_budget = None
        self._group_charge = None
        self._group_id = None
        self._group_inherit = None
        self._group_name = None
        self._include_customized_crowd_list = None
        self._interest_list = None
        self._lbs_list = None
        self._one_boost_status = None
        self._os_list = None
        self._plan_id = None
        self._principal_tag = None
        self._region_list = None
        self._region_type = None
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
    def include_customized_crowd_list(self):
        return self._include_customized_crowd_list

    @include_customized_crowd_list.setter
    def include_customized_crowd_list(self, value):
        if isinstance(value, list):
            self._include_customized_crowd_list = list()
            for i in value:
                self._include_customized_crowd_list.append(i)
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
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.age_list:
            if isinstance(self.age_list, list):
                for i in range(0, len(self.age_list)):
                    element = self.age_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.age_list[i] = element.to_alipay_dict()
            if hasattr(self.age_list, 'to_alipay_dict'):
                params['age_list'] = self.age_list.to_alipay_dict()
            else:
                params['age_list'] = self.age_list
        if self.asset:
            if hasattr(self.asset, 'to_alipay_dict'):
                params['asset'] = self.asset.to_alipay_dict()
            else:
                params['asset'] = self.asset
        if self.behavior_list:
            if isinstance(self.behavior_list, list):
                for i in range(0, len(self.behavior_list)):
                    element = self.behavior_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.behavior_list[i] = element.to_alipay_dict()
            if hasattr(self.behavior_list, 'to_alipay_dict'):
                params['behavior_list'] = self.behavior_list.to_alipay_dict()
            else:
                params['behavior_list'] = self.behavior_list
        if self.bid_type:
            if hasattr(self.bid_type, 'to_alipay_dict'):
                params['bid_type'] = self.bid_type.to_alipay_dict()
            else:
                params['bid_type'] = self.bid_type
        if self.boost_budget:
            if hasattr(self.boost_budget, 'to_alipay_dict'):
                params['boost_budget'] = self.boost_budget.to_alipay_dict()
            else:
                params['boost_budget'] = self.boost_budget
        if self.city_level_list:
            if isinstance(self.city_level_list, list):
                for i in range(0, len(self.city_level_list)):
                    element = self.city_level_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_level_list[i] = element.to_alipay_dict()
            if hasattr(self.city_level_list, 'to_alipay_dict'):
                params['city_level_list'] = self.city_level_list.to_alipay_dict()
            else:
                params['city_level_list'] = self.city_level_list
        if self.converted_event:
            if hasattr(self.converted_event, 'to_alipay_dict'):
                params['converted_event'] = self.converted_event.to_alipay_dict()
            else:
                params['converted_event'] = self.converted_event
        if self.converted_event_grp:
            if hasattr(self.converted_event_grp, 'to_alipay_dict'):
                params['converted_event_grp'] = self.converted_event_grp.to_alipay_dict()
            else:
                params['converted_event_grp'] = self.converted_event_grp
        if self.converted_id:
            if hasattr(self.converted_id, 'to_alipay_dict'):
                params['converted_id'] = self.converted_id.to_alipay_dict()
            else:
                params['converted_id'] = self.converted_id
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.exclude_customized_crowd_list:
            if isinstance(self.exclude_customized_crowd_list, list):
                for i in range(0, len(self.exclude_customized_crowd_list)):
                    element = self.exclude_customized_crowd_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exclude_customized_crowd_list[i] = element.to_alipay_dict()
            if hasattr(self.exclude_customized_crowd_list, 'to_alipay_dict'):
                params['exclude_customized_crowd_list'] = self.exclude_customized_crowd_list.to_alipay_dict()
            else:
                params['exclude_customized_crowd_list'] = self.exclude_customized_crowd_list
        if self.filter_converted_event_list:
            if isinstance(self.filter_converted_event_list, list):
                for i in range(0, len(self.filter_converted_event_list)):
                    element = self.filter_converted_event_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.filter_converted_event_list[i] = element.to_alipay_dict()
            if hasattr(self.filter_converted_event_list, 'to_alipay_dict'):
                params['filter_converted_event_list'] = self.filter_converted_event_list.to_alipay_dict()
            else:
                params['filter_converted_event_list'] = self.filter_converted_event_list
        if self.filter_converted_scope:
            if hasattr(self.filter_converted_scope, 'to_alipay_dict'):
                params['filter_converted_scope'] = self.filter_converted_scope.to_alipay_dict()
            else:
                params['filter_converted_scope'] = self.filter_converted_scope
        if self.filter_converted_time_range:
            if hasattr(self.filter_converted_time_range, 'to_alipay_dict'):
                params['filter_converted_time_range'] = self.filter_converted_time_range.to_alipay_dict()
            else:
                params['filter_converted_time_range'] = self.filter_converted_time_range
        if self.gender_list:
            if isinstance(self.gender_list, list):
                for i in range(0, len(self.gender_list)):
                    element = self.gender_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gender_list[i] = element.to_alipay_dict()
            if hasattr(self.gender_list, 'to_alipay_dict'):
                params['gender_list'] = self.gender_list.to_alipay_dict()
            else:
                params['gender_list'] = self.gender_list
        if self.group_budget:
            if hasattr(self.group_budget, 'to_alipay_dict'):
                params['group_budget'] = self.group_budget.to_alipay_dict()
            else:
                params['group_budget'] = self.group_budget
        if self.group_charge:
            if hasattr(self.group_charge, 'to_alipay_dict'):
                params['group_charge'] = self.group_charge.to_alipay_dict()
            else:
                params['group_charge'] = self.group_charge
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_inherit:
            if hasattr(self.group_inherit, 'to_alipay_dict'):
                params['group_inherit'] = self.group_inherit.to_alipay_dict()
            else:
                params['group_inherit'] = self.group_inherit
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.include_customized_crowd_list:
            if isinstance(self.include_customized_crowd_list, list):
                for i in range(0, len(self.include_customized_crowd_list)):
                    element = self.include_customized_crowd_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.include_customized_crowd_list[i] = element.to_alipay_dict()
            if hasattr(self.include_customized_crowd_list, 'to_alipay_dict'):
                params['include_customized_crowd_list'] = self.include_customized_crowd_list.to_alipay_dict()
            else:
                params['include_customized_crowd_list'] = self.include_customized_crowd_list
        if self.interest_list:
            if isinstance(self.interest_list, list):
                for i in range(0, len(self.interest_list)):
                    element = self.interest_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.interest_list[i] = element.to_alipay_dict()
            if hasattr(self.interest_list, 'to_alipay_dict'):
                params['interest_list'] = self.interest_list.to_alipay_dict()
            else:
                params['interest_list'] = self.interest_list
        if self.lbs_list:
            if isinstance(self.lbs_list, list):
                for i in range(0, len(self.lbs_list)):
                    element = self.lbs_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lbs_list[i] = element.to_alipay_dict()
            if hasattr(self.lbs_list, 'to_alipay_dict'):
                params['lbs_list'] = self.lbs_list.to_alipay_dict()
            else:
                params['lbs_list'] = self.lbs_list
        if self.one_boost_status:
            if hasattr(self.one_boost_status, 'to_alipay_dict'):
                params['one_boost_status'] = self.one_boost_status.to_alipay_dict()
            else:
                params['one_boost_status'] = self.one_boost_status
        if self.os_list:
            if isinstance(self.os_list, list):
                for i in range(0, len(self.os_list)):
                    element = self.os_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.os_list[i] = element.to_alipay_dict()
            if hasattr(self.os_list, 'to_alipay_dict'):
                params['os_list'] = self.os_list.to_alipay_dict()
            else:
                params['os_list'] = self.os_list
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.region_list:
            if isinstance(self.region_list, list):
                for i in range(0, len(self.region_list)):
                    element = self.region_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region_list[i] = element.to_alipay_dict()
            if hasattr(self.region_list, 'to_alipay_dict'):
                params['region_list'] = self.region_list.to_alipay_dict()
            else:
                params['region_list'] = self.region_list
        if self.region_type:
            if hasattr(self.region_type, 'to_alipay_dict'):
                params['region_type'] = self.region_type.to_alipay_dict()
            else:
                params['region_type'] = self.region_type
        if self.target_cpa:
            if hasattr(self.target_cpa, 'to_alipay_dict'):
                params['target_cpa'] = self.target_cpa.to_alipay_dict()
            else:
                params['target_cpa'] = self.target_cpa
        if self.theme_crowd_list:
            if isinstance(self.theme_crowd_list, list):
                for i in range(0, len(self.theme_crowd_list)):
                    element = self.theme_crowd_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.theme_crowd_list[i] = element.to_alipay_dict()
            if hasattr(self.theme_crowd_list, 'to_alipay_dict'):
                params['theme_crowd_list'] = self.theme_crowd_list.to_alipay_dict()
            else:
                params['theme_crowd_list'] = self.theme_crowd_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdcampaignGroupCreateormodifyModel()
        if 'age_list' in d:
            o.age_list = d['age_list']
        if 'asset' in d:
            o.asset = d['asset']
        if 'behavior_list' in d:
            o.behavior_list = d['behavior_list']
        if 'bid_type' in d:
            o.bid_type = d['bid_type']
        if 'boost_budget' in d:
            o.boost_budget = d['boost_budget']
        if 'city_level_list' in d:
            o.city_level_list = d['city_level_list']
        if 'converted_event' in d:
            o.converted_event = d['converted_event']
        if 'converted_event_grp' in d:
            o.converted_event_grp = d['converted_event_grp']
        if 'converted_id' in d:
            o.converted_id = d['converted_id']
        if 'district' in d:
            o.district = d['district']
        if 'exclude_customized_crowd_list' in d:
            o.exclude_customized_crowd_list = d['exclude_customized_crowd_list']
        if 'filter_converted_event_list' in d:
            o.filter_converted_event_list = d['filter_converted_event_list']
        if 'filter_converted_scope' in d:
            o.filter_converted_scope = d['filter_converted_scope']
        if 'filter_converted_time_range' in d:
            o.filter_converted_time_range = d['filter_converted_time_range']
        if 'gender_list' in d:
            o.gender_list = d['gender_list']
        if 'group_budget' in d:
            o.group_budget = d['group_budget']
        if 'group_charge' in d:
            o.group_charge = d['group_charge']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_inherit' in d:
            o.group_inherit = d['group_inherit']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'include_customized_crowd_list' in d:
            o.include_customized_crowd_list = d['include_customized_crowd_list']
        if 'interest_list' in d:
            o.interest_list = d['interest_list']
        if 'lbs_list' in d:
            o.lbs_list = d['lbs_list']
        if 'one_boost_status' in d:
            o.one_boost_status = d['one_boost_status']
        if 'os_list' in d:
            o.os_list = d['os_list']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'region_list' in d:
            o.region_list = d['region_list']
        if 'region_type' in d:
            o.region_type = d['region_type']
        if 'target_cpa' in d:
            o.target_cpa = d['target_cpa']
        if 'theme_crowd_list' in d:
            o.theme_crowd_list = d['theme_crowd_list']
        return o


