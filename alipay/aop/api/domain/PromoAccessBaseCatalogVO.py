#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoAccessBaseCatalogVO(object):

    def __init__(self):
        self._desc = None
        self._node_name = None
        self._nodei_d = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def nodei_d(self):
        return self._nodei_d

    @nodei_d.setter
    def nodei_d(self, value):
        self._nodei_d = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
        if self.nodei_d:
            if hasattr(self.nodei_d, 'to_alipay_dict'):
                params['nodei_d'] = self.nodei_d.to_alipay_dict()
            else:
                params['nodei_d'] = self.nodei_d
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoAccessBaseCatalogVO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'nodei_d' in d:
            o.nodei_d = d['nodei_d']
        return o


