#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceGrpquerybyclvgrpidsQueryModel(object):

    def __init__(self):
        self._clv_skill_group_ids = None
        self._query_scene_instance = None
        self._query_transfer_skill_groups = None
        self._tnt_inst_id = None

    @property
    def clv_skill_group_ids(self):
        return self._clv_skill_group_ids

    @clv_skill_group_ids.setter
    def clv_skill_group_ids(self, value):
        if isinstance(value, list):
            self._clv_skill_group_ids = list()
            for i in value:
                self._clv_skill_group_ids.append(i)
    @property
    def query_scene_instance(self):
        return self._query_scene_instance

    @query_scene_instance.setter
    def query_scene_instance(self, value):
        self._query_scene_instance = value
    @property
    def query_transfer_skill_groups(self):
        return self._query_transfer_skill_groups

    @query_transfer_skill_groups.setter
    def query_transfer_skill_groups(self, value):
        self._query_transfer_skill_groups = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.clv_skill_group_ids:
            if isinstance(self.clv_skill_group_ids, list):
                for i in range(0, len(self.clv_skill_group_ids)):
                    element = self.clv_skill_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.clv_skill_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.clv_skill_group_ids, 'to_alipay_dict'):
                params['clv_skill_group_ids'] = self.clv_skill_group_ids.to_alipay_dict()
            else:
                params['clv_skill_group_ids'] = self.clv_skill_group_ids
        if self.query_scene_instance:
            if hasattr(self.query_scene_instance, 'to_alipay_dict'):
                params['query_scene_instance'] = self.query_scene_instance.to_alipay_dict()
            else:
                params['query_scene_instance'] = self.query_scene_instance
        if self.query_transfer_skill_groups:
            if hasattr(self.query_transfer_skill_groups, 'to_alipay_dict'):
                params['query_transfer_skill_groups'] = self.query_transfer_skill_groups.to_alipay_dict()
            else:
                params['query_transfer_skill_groups'] = self.query_transfer_skill_groups
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceGrpquerybyclvgrpidsQueryModel()
        if 'clv_skill_group_ids' in d:
            o.clv_skill_group_ids = d['clv_skill_group_ids']
        if 'query_scene_instance' in d:
            o.query_scene_instance = d['query_scene_instance']
        if 'query_transfer_skill_groups' in d:
            o.query_transfer_skill_groups = d['query_transfer_skill_groups']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


