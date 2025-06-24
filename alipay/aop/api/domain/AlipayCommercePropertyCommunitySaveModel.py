#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomConfigVO import CustomConfigVO
from alipay.aop.api.domain.LocationAuthConfigVO import LocationAuthConfigVO
from alipay.aop.api.domain.SavePatrolReportConfigVO import SavePatrolReportConfigVO
from alipay.aop.api.domain.VisitorConfigVO import VisitorConfigVO


class AlipayCommercePropertyCommunitySaveModel(object):

    def __init__(self):
        self._action = None
        self._city_code = None
        self._city_name = None
        self._community_id = None
        self._community_name = None
        self._contact_number = None
        self._custom_config = None
        self._detail = None
        self._district_code = None
        self._district_name = None
        self._enable_monitor_room = None
        self._location_auth_config = None
        self._out_community_id = None
        self._patrol_report_config = None
        self._province_code = None
        self._province_name = None
        self._visitor_config = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def community_name(self):
        return self._community_name

    @community_name.setter
    def community_name(self, value):
        self._community_name = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
    @property
    def custom_config(self):
        return self._custom_config

    @custom_config.setter
    def custom_config(self, value):
        if isinstance(value, CustomConfigVO):
            self._custom_config = value
        else:
            self._custom_config = CustomConfigVO.from_alipay_dict(value)
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def enable_monitor_room(self):
        return self._enable_monitor_room

    @enable_monitor_room.setter
    def enable_monitor_room(self, value):
        self._enable_monitor_room = value
    @property
    def location_auth_config(self):
        return self._location_auth_config

    @location_auth_config.setter
    def location_auth_config(self, value):
        if isinstance(value, LocationAuthConfigVO):
            self._location_auth_config = value
        else:
            self._location_auth_config = LocationAuthConfigVO.from_alipay_dict(value)
    @property
    def out_community_id(self):
        return self._out_community_id

    @out_community_id.setter
    def out_community_id(self, value):
        self._out_community_id = value
    @property
    def patrol_report_config(self):
        return self._patrol_report_config

    @patrol_report_config.setter
    def patrol_report_config(self, value):
        if isinstance(value, SavePatrolReportConfigVO):
            self._patrol_report_config = value
        else:
            self._patrol_report_config = SavePatrolReportConfigVO.from_alipay_dict(value)
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def visitor_config(self):
        return self._visitor_config

    @visitor_config.setter
    def visitor_config(self, value):
        if isinstance(value, VisitorConfigVO):
            self._visitor_config = value
        else:
            self._visitor_config = VisitorConfigVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.community_name:
            if hasattr(self.community_name, 'to_alipay_dict'):
                params['community_name'] = self.community_name.to_alipay_dict()
            else:
                params['community_name'] = self.community_name
        if self.contact_number:
            if hasattr(self.contact_number, 'to_alipay_dict'):
                params['contact_number'] = self.contact_number.to_alipay_dict()
            else:
                params['contact_number'] = self.contact_number
        if self.custom_config:
            if hasattr(self.custom_config, 'to_alipay_dict'):
                params['custom_config'] = self.custom_config.to_alipay_dict()
            else:
                params['custom_config'] = self.custom_config
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.enable_monitor_room:
            if hasattr(self.enable_monitor_room, 'to_alipay_dict'):
                params['enable_monitor_room'] = self.enable_monitor_room.to_alipay_dict()
            else:
                params['enable_monitor_room'] = self.enable_monitor_room
        if self.location_auth_config:
            if hasattr(self.location_auth_config, 'to_alipay_dict'):
                params['location_auth_config'] = self.location_auth_config.to_alipay_dict()
            else:
                params['location_auth_config'] = self.location_auth_config
        if self.out_community_id:
            if hasattr(self.out_community_id, 'to_alipay_dict'):
                params['out_community_id'] = self.out_community_id.to_alipay_dict()
            else:
                params['out_community_id'] = self.out_community_id
        if self.patrol_report_config:
            if hasattr(self.patrol_report_config, 'to_alipay_dict'):
                params['patrol_report_config'] = self.patrol_report_config.to_alipay_dict()
            else:
                params['patrol_report_config'] = self.patrol_report_config
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.visitor_config:
            if hasattr(self.visitor_config, 'to_alipay_dict'):
                params['visitor_config'] = self.visitor_config.to_alipay_dict()
            else:
                params['visitor_config'] = self.visitor_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePropertyCommunitySaveModel()
        if 'action' in d:
            o.action = d['action']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'community_name' in d:
            o.community_name = d['community_name']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        if 'custom_config' in d:
            o.custom_config = d['custom_config']
        if 'detail' in d:
            o.detail = d['detail']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'enable_monitor_room' in d:
            o.enable_monitor_room = d['enable_monitor_room']
        if 'location_auth_config' in d:
            o.location_auth_config = d['location_auth_config']
        if 'out_community_id' in d:
            o.out_community_id = d['out_community_id']
        if 'patrol_report_config' in d:
            o.patrol_report_config = d['patrol_report_config']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'visitor_config' in d:
            o.visitor_config = d['visitor_config']
        return o


