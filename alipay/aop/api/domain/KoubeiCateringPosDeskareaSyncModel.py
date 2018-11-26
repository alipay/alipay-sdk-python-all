#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeskAreaEntity import DeskAreaEntity


class KoubeiCateringPosDeskareaSyncModel(object):

    def __init__(self):
        self._desk_area = None
        self._type = None

    @property
    def desk_area(self):
        return self._desk_area

    @desk_area.setter
    def desk_area(self, value):
        if isinstance(value, DeskAreaEntity):
            self._desk_area = value
        else:
            self._desk_area = DeskAreaEntity.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.desk_area:
            if hasattr(self.desk_area, 'to_alipay_dict'):
                params['desk_area'] = self.desk_area.to_alipay_dict()
            else:
                params['desk_area'] = self.desk_area
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
        o = KoubeiCateringPosDeskareaSyncModel()
        if 'desk_area' in d:
            o.desk_area = d['desk_area']
        if 'type' in d:
            o.type = d['type']
        return o


