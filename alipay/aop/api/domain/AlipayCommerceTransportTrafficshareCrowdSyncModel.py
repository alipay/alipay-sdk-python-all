#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrafficshareCrowdUserSync import TrafficshareCrowdUserSync


class AlipayCommerceTransportTrafficshareCrowdSyncModel(object):

    def __init__(self):
        self._biz_crowd_type_identity = None
        self._biz_date = None
        self._biz_scene = None
        self._data_list = None

    @property
    def biz_crowd_type_identity(self):
        return self._biz_crowd_type_identity

    @biz_crowd_type_identity.setter
    def biz_crowd_type_identity(self, value):
        self._biz_crowd_type_identity = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, TrafficshareCrowdUserSync):
                    self._data_list.append(i)
                else:
                    self._data_list.append(TrafficshareCrowdUserSync.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_crowd_type_identity:
            if hasattr(self.biz_crowd_type_identity, 'to_alipay_dict'):
                params['biz_crowd_type_identity'] = self.biz_crowd_type_identity.to_alipay_dict()
            else:
                params['biz_crowd_type_identity'] = self.biz_crowd_type_identity
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTrafficshareCrowdSyncModel()
        if 'biz_crowd_type_identity' in d:
            o.biz_crowd_type_identity = d['biz_crowd_type_identity']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'data_list' in d:
            o.data_list = d['data_list']
        return o


