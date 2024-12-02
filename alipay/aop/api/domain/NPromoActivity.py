#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NPromoSubActivity import NPromoSubActivity


class NPromoActivity(object):

    def __init__(self):
        self._activity_desc = None
        self._activity_dvc_sn = None
        self._activity_id = None
        self._activity_type = None
        self._create_time = None
        self._effect_time = None
        self._end_time = None
        self._ignore_date = None
        self._status = None
        self._sub_activity_lists = None

    @property
    def activity_desc(self):
        return self._activity_desc

    @activity_desc.setter
    def activity_desc(self, value):
        self._activity_desc = value
    @property
    def activity_dvc_sn(self):
        return self._activity_dvc_sn

    @activity_dvc_sn.setter
    def activity_dvc_sn(self, value):
        self._activity_dvc_sn = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ignore_date(self):
        return self._ignore_date

    @ignore_date.setter
    def ignore_date(self, value):
        if isinstance(value, list):
            self._ignore_date = list()
            for i in value:
                self._ignore_date.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_activity_lists(self):
        return self._sub_activity_lists

    @sub_activity_lists.setter
    def sub_activity_lists(self, value):
        if isinstance(value, list):
            self._sub_activity_lists = list()
            for i in value:
                if isinstance(i, NPromoSubActivity):
                    self._sub_activity_lists.append(i)
                else:
                    self._sub_activity_lists.append(NPromoSubActivity.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_desc:
            if hasattr(self.activity_desc, 'to_alipay_dict'):
                params['activity_desc'] = self.activity_desc.to_alipay_dict()
            else:
                params['activity_desc'] = self.activity_desc
        if self.activity_dvc_sn:
            if hasattr(self.activity_dvc_sn, 'to_alipay_dict'):
                params['activity_dvc_sn'] = self.activity_dvc_sn.to_alipay_dict()
            else:
                params['activity_dvc_sn'] = self.activity_dvc_sn
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ignore_date:
            if isinstance(self.ignore_date, list):
                for i in range(0, len(self.ignore_date)):
                    element = self.ignore_date[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ignore_date[i] = element.to_alipay_dict()
            if hasattr(self.ignore_date, 'to_alipay_dict'):
                params['ignore_date'] = self.ignore_date.to_alipay_dict()
            else:
                params['ignore_date'] = self.ignore_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_activity_lists:
            if isinstance(self.sub_activity_lists, list):
                for i in range(0, len(self.sub_activity_lists)):
                    element = self.sub_activity_lists[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_activity_lists[i] = element.to_alipay_dict()
            if hasattr(self.sub_activity_lists, 'to_alipay_dict'):
                params['sub_activity_lists'] = self.sub_activity_lists.to_alipay_dict()
            else:
                params['sub_activity_lists'] = self.sub_activity_lists
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NPromoActivity()
        if 'activity_desc' in d:
            o.activity_desc = d['activity_desc']
        if 'activity_dvc_sn' in d:
            o.activity_dvc_sn = d['activity_dvc_sn']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ignore_date' in d:
            o.ignore_date = d['ignore_date']
        if 'status' in d:
            o.status = d['status']
        if 'sub_activity_lists' in d:
            o.sub_activity_lists = d['sub_activity_lists']
        return o


