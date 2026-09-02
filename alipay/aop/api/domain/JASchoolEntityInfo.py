#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JASchoolEntityInfo(object):

    def __init__(self):
        self._entity_id = None
        self._gmt_create = None
        self._has_member = None
        self._in_school_alert = None
        self._out_school_alert = None
        self._sign_withhold = None
        self._upgrade_time = None

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def has_member(self):
        return self._has_member

    @has_member.setter
    def has_member(self, value):
        self._has_member = value
    @property
    def in_school_alert(self):
        return self._in_school_alert

    @in_school_alert.setter
    def in_school_alert(self, value):
        self._in_school_alert = value
    @property
    def out_school_alert(self):
        return self._out_school_alert

    @out_school_alert.setter
    def out_school_alert(self, value):
        self._out_school_alert = value
    @property
    def sign_withhold(self):
        return self._sign_withhold

    @sign_withhold.setter
    def sign_withhold(self, value):
        self._sign_withhold = value
    @property
    def upgrade_time(self):
        return self._upgrade_time

    @upgrade_time.setter
    def upgrade_time(self, value):
        self._upgrade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.has_member:
            if hasattr(self.has_member, 'to_alipay_dict'):
                params['has_member'] = self.has_member.to_alipay_dict()
            else:
                params['has_member'] = self.has_member
        if self.in_school_alert:
            if hasattr(self.in_school_alert, 'to_alipay_dict'):
                params['in_school_alert'] = self.in_school_alert.to_alipay_dict()
            else:
                params['in_school_alert'] = self.in_school_alert
        if self.out_school_alert:
            if hasattr(self.out_school_alert, 'to_alipay_dict'):
                params['out_school_alert'] = self.out_school_alert.to_alipay_dict()
            else:
                params['out_school_alert'] = self.out_school_alert
        if self.sign_withhold:
            if hasattr(self.sign_withhold, 'to_alipay_dict'):
                params['sign_withhold'] = self.sign_withhold.to_alipay_dict()
            else:
                params['sign_withhold'] = self.sign_withhold
        if self.upgrade_time:
            if hasattr(self.upgrade_time, 'to_alipay_dict'):
                params['upgrade_time'] = self.upgrade_time.to_alipay_dict()
            else:
                params['upgrade_time'] = self.upgrade_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JASchoolEntityInfo()
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'has_member' in d:
            o.has_member = d['has_member']
        if 'in_school_alert' in d:
            o.in_school_alert = d['in_school_alert']
        if 'out_school_alert' in d:
            o.out_school_alert = d['out_school_alert']
        if 'sign_withhold' in d:
            o.sign_withhold = d['sign_withhold']
        if 'upgrade_time' in d:
            o.upgrade_time = d['upgrade_time']
        return o


