#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MarketTargetConfiguration import MarketTargetConfiguration


class AlipayDataDataserviceAdcampaignPlanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignPlanQueryResponse, self).__init__()
        self._budget = None
        self._charge_type = None
        self._end_date = None
        self._gmt_modified = None
        self._market_target_code = None
        self._market_target_config = None
        self._market_target_name = None
        self._plan_id = None
        self._plan_name = None
        self._plan_status = None
        self._plan_unlimited_budget_switch = None
        self._principal_id = None
        self._promote_target_app_id = None
        self._promote_target_app_name = None
        self._promote_target_app_type = None
        self._rtb_freeze_order_id = None
        self._scene_code = None
        self._sell_mode = None
        self._service_entity_name = None
        self._service_entity_outid = None
        self._special_name = None
        self._start_date = None
        self._time_schema = None
        self._tiny_app_id = None
        self._tiny_app_name = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        self._budget = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def market_target_code(self):
        return self._market_target_code

    @market_target_code.setter
    def market_target_code(self, value):
        self._market_target_code = value
    @property
    def market_target_config(self):
        return self._market_target_config

    @market_target_config.setter
    def market_target_config(self, value):
        if isinstance(value, MarketTargetConfiguration):
            self._market_target_config = value
        else:
            self._market_target_config = MarketTargetConfiguration.from_alipay_dict(value)
    @property
    def market_target_name(self):
        return self._market_target_name

    @market_target_name.setter
    def market_target_name(self, value):
        self._market_target_name = value
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
    def plan_status(self):
        return self._plan_status

    @plan_status.setter
    def plan_status(self, value):
        self._plan_status = value
    @property
    def plan_unlimited_budget_switch(self):
        return self._plan_unlimited_budget_switch

    @plan_unlimited_budget_switch.setter
    def plan_unlimited_budget_switch(self, value):
        self._plan_unlimited_budget_switch = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def promote_target_app_id(self):
        return self._promote_target_app_id

    @promote_target_app_id.setter
    def promote_target_app_id(self, value):
        self._promote_target_app_id = value
    @property
    def promote_target_app_name(self):
        return self._promote_target_app_name

    @promote_target_app_name.setter
    def promote_target_app_name(self, value):
        self._promote_target_app_name = value
    @property
    def promote_target_app_type(self):
        return self._promote_target_app_type

    @promote_target_app_type.setter
    def promote_target_app_type(self, value):
        self._promote_target_app_type = value
    @property
    def rtb_freeze_order_id(self):
        return self._rtb_freeze_order_id

    @rtb_freeze_order_id.setter
    def rtb_freeze_order_id(self, value):
        self._rtb_freeze_order_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sell_mode(self):
        return self._sell_mode

    @sell_mode.setter
    def sell_mode(self, value):
        self._sell_mode = value
    @property
    def service_entity_name(self):
        return self._service_entity_name

    @service_entity_name.setter
    def service_entity_name(self, value):
        self._service_entity_name = value
    @property
    def service_entity_outid(self):
        return self._service_entity_outid

    @service_entity_outid.setter
    def service_entity_outid(self, value):
        self._service_entity_outid = value
    @property
    def special_name(self):
        return self._special_name

    @special_name.setter
    def special_name(self, value):
        self._special_name = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def time_schema(self):
        return self._time_schema

    @time_schema.setter
    def time_schema(self, value):
        self._time_schema = value
    @property
    def tiny_app_id(self):
        return self._tiny_app_id

    @tiny_app_id.setter
    def tiny_app_id(self, value):
        self._tiny_app_id = value
    @property
    def tiny_app_name(self):
        return self._tiny_app_name

    @tiny_app_name.setter
    def tiny_app_name(self, value):
        self._tiny_app_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignPlanQueryResponse, self).parse_response_content(response_content)
        if 'budget' in response:
            self.budget = response['budget']
        if 'charge_type' in response:
            self.charge_type = response['charge_type']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'market_target_code' in response:
            self.market_target_code = response['market_target_code']
        if 'market_target_config' in response:
            self.market_target_config = response['market_target_config']
        if 'market_target_name' in response:
            self.market_target_name = response['market_target_name']
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'plan_name' in response:
            self.plan_name = response['plan_name']
        if 'plan_status' in response:
            self.plan_status = response['plan_status']
        if 'plan_unlimited_budget_switch' in response:
            self.plan_unlimited_budget_switch = response['plan_unlimited_budget_switch']
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
        if 'promote_target_app_id' in response:
            self.promote_target_app_id = response['promote_target_app_id']
        if 'promote_target_app_name' in response:
            self.promote_target_app_name = response['promote_target_app_name']
        if 'promote_target_app_type' in response:
            self.promote_target_app_type = response['promote_target_app_type']
        if 'rtb_freeze_order_id' in response:
            self.rtb_freeze_order_id = response['rtb_freeze_order_id']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'sell_mode' in response:
            self.sell_mode = response['sell_mode']
        if 'service_entity_name' in response:
            self.service_entity_name = response['service_entity_name']
        if 'service_entity_outid' in response:
            self.service_entity_outid = response['service_entity_outid']
        if 'special_name' in response:
            self.special_name = response['special_name']
        if 'start_date' in response:
            self.start_date = response['start_date']
        if 'time_schema' in response:
            self.time_schema = response['time_schema']
        if 'tiny_app_id' in response:
            self.tiny_app_id = response['tiny_app_id']
        if 'tiny_app_name' in response:
            self.tiny_app_name = response['tiny_app_name']
