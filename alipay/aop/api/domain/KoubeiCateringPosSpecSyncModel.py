#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpecEntity import SpecEntity


class KoubeiCateringPosSpecSyncModel(object):

    def __init__(self):
        self._spec = None
        self._spec_ids = None
        self._type = None

    @property
    def spec(self):
        return self._spec

    @spec.setter
    def spec(self, value):
        if isinstance(value, SpecEntity):
            self._spec = value
        else:
            self._spec = SpecEntity.from_alipay_dict(value)
    @property
    def spec_ids(self):
        return self._spec_ids

    @spec_ids.setter
    def spec_ids(self, value):
        if isinstance(value, list):
            self._spec_ids = list()
            for i in value:
                self._spec_ids.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.spec:
            if hasattr(self.spec, 'to_alipay_dict'):
                params['spec'] = self.spec.to_alipay_dict()
            else:
                params['spec'] = self.spec
        if self.spec_ids:
            if isinstance(self.spec_ids, list):
                for i in range(0, len(self.spec_ids)):
                    element = self.spec_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.spec_ids[i] = element.to_alipay_dict()
            if hasattr(self.spec_ids, 'to_alipay_dict'):
                params['spec_ids'] = self.spec_ids.to_alipay_dict()
            else:
                params['spec_ids'] = self.spec_ids
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
        o = KoubeiCateringPosSpecSyncModel()
        if 'spec' in d:
            o.spec = d['spec']
        if 'spec_ids' in d:
            o.spec_ids = d['spec_ids']
        if 'type' in d:
            o.type = d['type']
        return o


