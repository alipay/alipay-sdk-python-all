#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AutohomeContactStatusModel import AutohomeContactStatusModel
from alipay.aop.api.domain.AutohomeDealStatusModel import AutohomeDealStatusModel
from alipay.aop.api.domain.AutohomeDistributeStatusModel import AutohomeDistributeStatusModel


class AlipayEcoMycarAutohomeleadsStatusSyncModel(object):

    def __init__(self):
        self._contact_status = None
        self._deal_status = None
        self._distribute_status = None
        self._key_push_id = None
        self._key_split_id = None
        self._key_unique_id = None
        self._status_type = None

    @property
    def contact_status(self):
        return self._contact_status

    @contact_status.setter
    def contact_status(self, value):
        if isinstance(value, AutohomeContactStatusModel):
            self._contact_status = value
        else:
            self._contact_status = AutohomeContactStatusModel.from_alipay_dict(value)
    @property
    def deal_status(self):
        return self._deal_status

    @deal_status.setter
    def deal_status(self, value):
        if isinstance(value, AutohomeDealStatusModel):
            self._deal_status = value
        else:
            self._deal_status = AutohomeDealStatusModel.from_alipay_dict(value)
    @property
    def distribute_status(self):
        return self._distribute_status

    @distribute_status.setter
    def distribute_status(self, value):
        if isinstance(value, AutohomeDistributeStatusModel):
            self._distribute_status = value
        else:
            self._distribute_status = AutohomeDistributeStatusModel.from_alipay_dict(value)
    @property
    def key_push_id(self):
        return self._key_push_id

    @key_push_id.setter
    def key_push_id(self, value):
        self._key_push_id = value
    @property
    def key_split_id(self):
        return self._key_split_id

    @key_split_id.setter
    def key_split_id(self, value):
        self._key_split_id = value
    @property
    def key_unique_id(self):
        return self._key_unique_id

    @key_unique_id.setter
    def key_unique_id(self, value):
        self._key_unique_id = value
    @property
    def status_type(self):
        return self._status_type

    @status_type.setter
    def status_type(self, value):
        self._status_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_status:
            if hasattr(self.contact_status, 'to_alipay_dict'):
                params['contact_status'] = self.contact_status.to_alipay_dict()
            else:
                params['contact_status'] = self.contact_status
        if self.deal_status:
            if hasattr(self.deal_status, 'to_alipay_dict'):
                params['deal_status'] = self.deal_status.to_alipay_dict()
            else:
                params['deal_status'] = self.deal_status
        if self.distribute_status:
            if hasattr(self.distribute_status, 'to_alipay_dict'):
                params['distribute_status'] = self.distribute_status.to_alipay_dict()
            else:
                params['distribute_status'] = self.distribute_status
        if self.key_push_id:
            if hasattr(self.key_push_id, 'to_alipay_dict'):
                params['key_push_id'] = self.key_push_id.to_alipay_dict()
            else:
                params['key_push_id'] = self.key_push_id
        if self.key_split_id:
            if hasattr(self.key_split_id, 'to_alipay_dict'):
                params['key_split_id'] = self.key_split_id.to_alipay_dict()
            else:
                params['key_split_id'] = self.key_split_id
        if self.key_unique_id:
            if hasattr(self.key_unique_id, 'to_alipay_dict'):
                params['key_unique_id'] = self.key_unique_id.to_alipay_dict()
            else:
                params['key_unique_id'] = self.key_unique_id
        if self.status_type:
            if hasattr(self.status_type, 'to_alipay_dict'):
                params['status_type'] = self.status_type.to_alipay_dict()
            else:
                params['status_type'] = self.status_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarAutohomeleadsStatusSyncModel()
        if 'contact_status' in d:
            o.contact_status = d['contact_status']
        if 'deal_status' in d:
            o.deal_status = d['deal_status']
        if 'distribute_status' in d:
            o.distribute_status = d['distribute_status']
        if 'key_push_id' in d:
            o.key_push_id = d['key_push_id']
        if 'key_split_id' in d:
            o.key_split_id = d['key_split_id']
        if 'key_unique_id' in d:
            o.key_unique_id = d['key_unique_id']
        if 'status_type' in d:
            o.status_type = d['status_type']
        return o


