#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AggregationInstance(object):

    def __init__(self):
        self._aggr_id = None
        self._biz_no = None
        self._gmt_active = None
        self._gmt_expire = None
        self._id = None
        self._name = None
        self._out_id = None
        self._user_id = None

    @property
    def aggr_id(self):
        return self._aggr_id

    @aggr_id.setter
    def aggr_id(self, value):
        self._aggr_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_expire(self):
        return self._gmt_expire

    @gmt_expire.setter
    def gmt_expire(self, value):
        self._gmt_expire = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggr_id:
            if hasattr(self.aggr_id, 'to_alipay_dict'):
                params['aggr_id'] = self.aggr_id.to_alipay_dict()
            else:
                params['aggr_id'] = self.aggr_id
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_expire:
            if hasattr(self.gmt_expire, 'to_alipay_dict'):
                params['gmt_expire'] = self.gmt_expire.to_alipay_dict()
            else:
                params['gmt_expire'] = self.gmt_expire
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
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
        o = AggregationInstance()
        if 'aggr_id' in d:
            o.aggr_id = d['aggr_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_expire' in d:
            o.gmt_expire = d['gmt_expire']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


