#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstAllocationQuotaVO import InstAllocationQuotaVO


class AlipayAccountCashpoolRulegroupModifyModel(object):

    def __init__(self):
        self._cash_pool_id = None
        self._config_type = None
        self._inst_allocation_quota_vo_list = None
        self._operator = None
        self._parent_target_water_line = None
        self._rule_group_id = None
        self._rule_group_status = None
        self._trigger_time = None
        self._water_mode = None

    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value
    @property
    def config_type(self):
        return self._config_type

    @config_type.setter
    def config_type(self, value):
        self._config_type = value
    @property
    def inst_allocation_quota_vo_list(self):
        return self._inst_allocation_quota_vo_list

    @inst_allocation_quota_vo_list.setter
    def inst_allocation_quota_vo_list(self, value):
        if isinstance(value, list):
            self._inst_allocation_quota_vo_list = list()
            for i in value:
                if isinstance(i, InstAllocationQuotaVO):
                    self._inst_allocation_quota_vo_list.append(i)
                else:
                    self._inst_allocation_quota_vo_list.append(InstAllocationQuotaVO.from_alipay_dict(i))
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def parent_target_water_line(self):
        return self._parent_target_water_line

    @parent_target_water_line.setter
    def parent_target_water_line(self, value):
        self._parent_target_water_line = value
    @property
    def rule_group_id(self):
        return self._rule_group_id

    @rule_group_id.setter
    def rule_group_id(self, value):
        self._rule_group_id = value
    @property
    def rule_group_status(self):
        return self._rule_group_status

    @rule_group_status.setter
    def rule_group_status(self, value):
        self._rule_group_status = value
    @property
    def trigger_time(self):
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, value):
        self._trigger_time = value
    @property
    def water_mode(self):
        return self._water_mode

    @water_mode.setter
    def water_mode(self, value):
        self._water_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.cash_pool_id:
            if hasattr(self.cash_pool_id, 'to_alipay_dict'):
                params['cash_pool_id'] = self.cash_pool_id.to_alipay_dict()
            else:
                params['cash_pool_id'] = self.cash_pool_id
        if self.config_type:
            if hasattr(self.config_type, 'to_alipay_dict'):
                params['config_type'] = self.config_type.to_alipay_dict()
            else:
                params['config_type'] = self.config_type
        if self.inst_allocation_quota_vo_list:
            if isinstance(self.inst_allocation_quota_vo_list, list):
                for i in range(0, len(self.inst_allocation_quota_vo_list)):
                    element = self.inst_allocation_quota_vo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inst_allocation_quota_vo_list[i] = element.to_alipay_dict()
            if hasattr(self.inst_allocation_quota_vo_list, 'to_alipay_dict'):
                params['inst_allocation_quota_vo_list'] = self.inst_allocation_quota_vo_list.to_alipay_dict()
            else:
                params['inst_allocation_quota_vo_list'] = self.inst_allocation_quota_vo_list
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.parent_target_water_line:
            if hasattr(self.parent_target_water_line, 'to_alipay_dict'):
                params['parent_target_water_line'] = self.parent_target_water_line.to_alipay_dict()
            else:
                params['parent_target_water_line'] = self.parent_target_water_line
        if self.rule_group_id:
            if hasattr(self.rule_group_id, 'to_alipay_dict'):
                params['rule_group_id'] = self.rule_group_id.to_alipay_dict()
            else:
                params['rule_group_id'] = self.rule_group_id
        if self.rule_group_status:
            if hasattr(self.rule_group_status, 'to_alipay_dict'):
                params['rule_group_status'] = self.rule_group_status.to_alipay_dict()
            else:
                params['rule_group_status'] = self.rule_group_status
        if self.trigger_time:
            if hasattr(self.trigger_time, 'to_alipay_dict'):
                params['trigger_time'] = self.trigger_time.to_alipay_dict()
            else:
                params['trigger_time'] = self.trigger_time
        if self.water_mode:
            if hasattr(self.water_mode, 'to_alipay_dict'):
                params['water_mode'] = self.water_mode.to_alipay_dict()
            else:
                params['water_mode'] = self.water_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountCashpoolRulegroupModifyModel()
        if 'cash_pool_id' in d:
            o.cash_pool_id = d['cash_pool_id']
        if 'config_type' in d:
            o.config_type = d['config_type']
        if 'inst_allocation_quota_vo_list' in d:
            o.inst_allocation_quota_vo_list = d['inst_allocation_quota_vo_list']
        if 'operator' in d:
            o.operator = d['operator']
        if 'parent_target_water_line' in d:
            o.parent_target_water_line = d['parent_target_water_line']
        if 'rule_group_id' in d:
            o.rule_group_id = d['rule_group_id']
        if 'rule_group_status' in d:
            o.rule_group_status = d['rule_group_status']
        if 'trigger_time' in d:
            o.trigger_time = d['trigger_time']
        if 'water_mode' in d:
            o.water_mode = d['water_mode']
        return o


