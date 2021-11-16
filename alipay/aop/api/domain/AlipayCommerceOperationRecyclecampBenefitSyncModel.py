#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationRecyclecampBenefitSyncModel(object):

    def __init__(self):
        self._outer_benefit_id = None
        self._remain_inventory = None
        self._sync_timestamp = None
        self._sync_type = None

    @property
    def outer_benefit_id(self):
        return self._outer_benefit_id

    @outer_benefit_id.setter
    def outer_benefit_id(self, value):
        self._outer_benefit_id = value
    @property
    def remain_inventory(self):
        return self._remain_inventory

    @remain_inventory.setter
    def remain_inventory(self, value):
        self._remain_inventory = value
    @property
    def sync_timestamp(self):
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, value):
        self._sync_timestamp = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.outer_benefit_id:
            if hasattr(self.outer_benefit_id, 'to_alipay_dict'):
                params['outer_benefit_id'] = self.outer_benefit_id.to_alipay_dict()
            else:
                params['outer_benefit_id'] = self.outer_benefit_id
        if self.remain_inventory:
            if hasattr(self.remain_inventory, 'to_alipay_dict'):
                params['remain_inventory'] = self.remain_inventory.to_alipay_dict()
            else:
                params['remain_inventory'] = self.remain_inventory
        if self.sync_timestamp:
            if hasattr(self.sync_timestamp, 'to_alipay_dict'):
                params['sync_timestamp'] = self.sync_timestamp.to_alipay_dict()
            else:
                params['sync_timestamp'] = self.sync_timestamp
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationRecyclecampBenefitSyncModel()
        if 'outer_benefit_id' in d:
            o.outer_benefit_id = d['outer_benefit_id']
        if 'remain_inventory' in d:
            o.remain_inventory = d['remain_inventory']
        if 'sync_timestamp' in d:
            o.sync_timestamp = d['sync_timestamp']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


