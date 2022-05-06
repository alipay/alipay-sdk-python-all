#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchBoxBasicInfo(object):

    def __init__(self):
        self._box_id = None
        self._brand_id = None
        self._name = None
        self._status = None
        self._target_appid = None

    @property
    def box_id(self):
        return self._box_id

    @box_id.setter
    def box_id(self, value):
        self._box_id = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_appid(self):
        return self._target_appid

    @target_appid.setter
    def target_appid(self, value):
        self._target_appid = value


    def to_alipay_dict(self):
        params = dict()
        if self.box_id:
            if hasattr(self.box_id, 'to_alipay_dict'):
                params['box_id'] = self.box_id.to_alipay_dict()
            else:
                params['box_id'] = self.box_id
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_appid:
            if hasattr(self.target_appid, 'to_alipay_dict'):
                params['target_appid'] = self.target_appid.to_alipay_dict()
            else:
                params['target_appid'] = self.target_appid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBoxBasicInfo()
        if 'box_id' in d:
            o.box_id = d['box_id']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        if 'target_appid' in d:
            o.target_appid = d['target_appid']
        return o


