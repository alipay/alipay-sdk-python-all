#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceCloudbusPredictresultQueryModel(object):

    def __init__(self):
        self._app_version = None
        self._min_volume = None
        self._partner_id = None
        self._plan_id = None
        self._type = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def min_volume(self):
        return self._min_volume

    @min_volume.setter
    def min_volume(self, value):
        self._min_volume = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.min_volume:
            if hasattr(self.min_volume, 'to_alipay_dict'):
                params['min_volume'] = self.min_volume.to_alipay_dict()
            else:
                params['min_volume'] = self.min_volume
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceCloudbusPredictresultQueryModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'min_volume' in d:
            o.min_volume = d['min_volume']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'type' in d:
            o.type = d['type']
        return o


