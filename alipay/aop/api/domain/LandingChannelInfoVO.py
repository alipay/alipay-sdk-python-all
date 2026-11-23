#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LandingChannelInfoVO(object):

    def __init__(self):
        self._scene_id = None
        self._source_scenario_context = None
        self._source_scenario_type = None
        self._union_rent_tag = None

    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def source_scenario_context(self):
        return self._source_scenario_context

    @source_scenario_context.setter
    def source_scenario_context(self, value):
        self._source_scenario_context = value
    @property
    def source_scenario_type(self):
        return self._source_scenario_type

    @source_scenario_type.setter
    def source_scenario_type(self, value):
        self._source_scenario_type = value
    @property
    def union_rent_tag(self):
        return self._union_rent_tag

    @union_rent_tag.setter
    def union_rent_tag(self, value):
        self._union_rent_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.source_scenario_context:
            if hasattr(self.source_scenario_context, 'to_alipay_dict'):
                params['source_scenario_context'] = self.source_scenario_context.to_alipay_dict()
            else:
                params['source_scenario_context'] = self.source_scenario_context
        if self.source_scenario_type:
            if hasattr(self.source_scenario_type, 'to_alipay_dict'):
                params['source_scenario_type'] = self.source_scenario_type.to_alipay_dict()
            else:
                params['source_scenario_type'] = self.source_scenario_type
        if self.union_rent_tag:
            if hasattr(self.union_rent_tag, 'to_alipay_dict'):
                params['union_rent_tag'] = self.union_rent_tag.to_alipay_dict()
            else:
                params['union_rent_tag'] = self.union_rent_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LandingChannelInfoVO()
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'source_scenario_context' in d:
            o.source_scenario_context = d['source_scenario_context']
        if 'source_scenario_type' in d:
            o.source_scenario_type = d['source_scenario_type']
        if 'union_rent_tag' in d:
            o.union_rent_tag = d['union_rent_tag']
        return o


