#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalChildgrowthDataQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._data_type = None
        self._interp_biz_id = None
        self._open_id = None
        self._org_id = None
        self._profile_id = None
        self._record_end_date = None
        self._record_start_date = None
        self._user_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def interp_biz_id(self):
        return self._interp_biz_id

    @interp_biz_id.setter
    def interp_biz_id(self, value):
        self._interp_biz_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def profile_id(self):
        return self._profile_id

    @profile_id.setter
    def profile_id(self, value):
        self._profile_id = value
    @property
    def record_end_date(self):
        return self._record_end_date

    @record_end_date.setter
    def record_end_date(self, value):
        self._record_end_date = value
    @property
    def record_start_date(self):
        return self._record_start_date

    @record_start_date.setter
    def record_start_date(self, value):
        self._record_start_date = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.interp_biz_id:
            if hasattr(self.interp_biz_id, 'to_alipay_dict'):
                params['interp_biz_id'] = self.interp_biz_id.to_alipay_dict()
            else:
                params['interp_biz_id'] = self.interp_biz_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.profile_id:
            if hasattr(self.profile_id, 'to_alipay_dict'):
                params['profile_id'] = self.profile_id.to_alipay_dict()
            else:
                params['profile_id'] = self.profile_id
        if self.record_end_date:
            if hasattr(self.record_end_date, 'to_alipay_dict'):
                params['record_end_date'] = self.record_end_date.to_alipay_dict()
            else:
                params['record_end_date'] = self.record_end_date
        if self.record_start_date:
            if hasattr(self.record_start_date, 'to_alipay_dict'):
                params['record_start_date'] = self.record_start_date.to_alipay_dict()
            else:
                params['record_start_date'] = self.record_start_date
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalChildgrowthDataQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'interp_biz_id' in d:
            o.interp_biz_id = d['interp_biz_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'profile_id' in d:
            o.profile_id = d['profile_id']
        if 'record_end_date' in d:
            o.record_end_date = d['record_end_date']
        if 'record_start_date' in d:
            o.record_start_date = d['record_start_date']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


