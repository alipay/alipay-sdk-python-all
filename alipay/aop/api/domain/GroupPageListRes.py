#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupPageListRes(object):

    def __init__(self):
        self._bid_type = None
        self._boost_budget = None
        self._boost_end_date = None
        self._boost_id = None
        self._boost_start_date = None
        self._gmt_modified = None
        self._group_budget = None
        self._group_charge = None
        self._group_id = None
        self._group_name = None
        self._group_status = None
        self._market_target_code = None
        self._market_target_name = None
        self._one_boost_status = None
        self._plan_id = None
        self._plan_name = None
        self._principal_id = None
        self._scene_code = None
        self._target_cpa = None

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
    def target_cpa(self):
        return self._target_cpa

    @target_cpa.setter
    def target_cpa(self, value):
        self._target_cpa = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.boost_end_date:
            if hasattr(self.boost_end_date, 'to_alipay_dict'):
                params['boost_end_date'] = self.boost_end_date.to_alipay_dict()
            else:
                params['boost_end_date'] = self.boost_end_date
        if self.boost_id:
            if hasattr(self.boost_id, 'to_alipay_dict'):
                params['boost_id'] = self.boost_id.to_alipay_dict()
            else:
                params['boost_id'] = self.boost_id
        if self.boost_start_date:
            if hasattr(self.boost_start_date, 'to_alipay_dict'):
                params['boost_start_date'] = self.boost_start_date.to_alipay_dict()
            else:
                params['boost_start_date'] = self.boost_start_date
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
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
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.group_status:
            if hasattr(self.group_status, 'to_alipay_dict'):
                params['group_status'] = self.group_status.to_alipay_dict()
            else:
                params['group_status'] = self.group_status
        if self.market_target_code:
            if hasattr(self.market_target_code, 'to_alipay_dict'):
                params['market_target_code'] = self.market_target_code.to_alipay_dict()
            else:
                params['market_target_code'] = self.market_target_code
        if self.market_target_name:
            if hasattr(self.market_target_name, 'to_alipay_dict'):
                params['market_target_name'] = self.market_target_name.to_alipay_dict()
            else:
                params['market_target_name'] = self.market_target_name
        if self.one_boost_status:
            if hasattr(self.one_boost_status, 'to_alipay_dict'):
                params['one_boost_status'] = self.one_boost_status.to_alipay_dict()
            else:
                params['one_boost_status'] = self.one_boost_status
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.target_cpa:
            if hasattr(self.target_cpa, 'to_alipay_dict'):
                params['target_cpa'] = self.target_cpa.to_alipay_dict()
            else:
                params['target_cpa'] = self.target_cpa
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupPageListRes()
        if 'bid_type' in d:
            o.bid_type = d['bid_type']
        if 'boost_budget' in d:
            o.boost_budget = d['boost_budget']
        if 'boost_end_date' in d:
            o.boost_end_date = d['boost_end_date']
        if 'boost_id' in d:
            o.boost_id = d['boost_id']
        if 'boost_start_date' in d:
            o.boost_start_date = d['boost_start_date']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'group_budget' in d:
            o.group_budget = d['group_budget']
        if 'group_charge' in d:
            o.group_charge = d['group_charge']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'group_status' in d:
            o.group_status = d['group_status']
        if 'market_target_code' in d:
            o.market_target_code = d['market_target_code']
        if 'market_target_name' in d:
            o.market_target_name = d['market_target_name']
        if 'one_boost_status' in d:
            o.one_boost_status = d['one_boost_status']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'target_cpa' in d:
            o.target_cpa = d['target_cpa']
        return o


