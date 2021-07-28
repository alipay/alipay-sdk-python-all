#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstAllocationQuotaVO import InstAllocationQuotaVO


class AlipayAccountCashpoolRulegroupCreateModel(object):

    def __init__(self):
        self._cash_pool_id = None
        self._effective_time = None
        self._expire_time = None
        self._inst_allocation_quota_vo_list = None
        self._memo = None
        self._operator = None
        self._out_biz_no = None
        self._parent_target_water_line = None
        self._rule_group_name = None
        self._rule_group_type = None
        self._trigger_time = None
        self._water_mode = None

    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
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
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def parent_target_water_line(self):
        return self._parent_target_water_line

    @parent_target_water_line.setter
    def parent_target_water_line(self, value):
        self._parent_target_water_line = value
    @property
    def rule_group_name(self):
        return self._rule_group_name

    @rule_group_name.setter
    def rule_group_name(self, value):
        self._rule_group_name = value
    @property
    def rule_group_type(self):
        return self._rule_group_type

    @rule_group_type.setter
    def rule_group_type(self, value):
        self._rule_group_type = value
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
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.parent_target_water_line:
            if hasattr(self.parent_target_water_line, 'to_alipay_dict'):
                params['parent_target_water_line'] = self.parent_target_water_line.to_alipay_dict()
            else:
                params['parent_target_water_line'] = self.parent_target_water_line
        if self.rule_group_name:
            if hasattr(self.rule_group_name, 'to_alipay_dict'):
                params['rule_group_name'] = self.rule_group_name.to_alipay_dict()
            else:
                params['rule_group_name'] = self.rule_group_name
        if self.rule_group_type:
            if hasattr(self.rule_group_type, 'to_alipay_dict'):
                params['rule_group_type'] = self.rule_group_type.to_alipay_dict()
            else:
                params['rule_group_type'] = self.rule_group_type
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
        o = AlipayAccountCashpoolRulegroupCreateModel()
        if 'cash_pool_id' in d:
            o.cash_pool_id = d['cash_pool_id']
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'inst_allocation_quota_vo_list' in d:
            o.inst_allocation_quota_vo_list = d['inst_allocation_quota_vo_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'parent_target_water_line' in d:
            o.parent_target_water_line = d['parent_target_water_line']
        if 'rule_group_name' in d:
            o.rule_group_name = d['rule_group_name']
        if 'rule_group_type' in d:
            o.rule_group_type = d['rule_group_type']
        if 'trigger_time' in d:
            o.trigger_time = d['trigger_time']
        if 'water_mode' in d:
            o.water_mode = d['water_mode']
        return o


