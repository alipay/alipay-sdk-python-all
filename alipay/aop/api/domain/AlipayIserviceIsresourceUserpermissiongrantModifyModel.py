#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceUserpermissiongrantModifyModel(object):

    def __init__(self):
        self._clv_skill_group_ids = None
        self._clv_user_id = None
        self._grant = None
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
    def clv_user_id(self):
        return self._clv_user_id

    @clv_user_id.setter
    def clv_user_id(self, value):
        self._clv_user_id = value
    @property
    def grant(self):
        return self._grant

    @grant.setter
    def grant(self, value):
        self._grant = value
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
        if self.clv_user_id:
            if hasattr(self.clv_user_id, 'to_alipay_dict'):
                params['clv_user_id'] = self.clv_user_id.to_alipay_dict()
            else:
                params['clv_user_id'] = self.clv_user_id
        if self.grant:
            if hasattr(self.grant, 'to_alipay_dict'):
                params['grant'] = self.grant.to_alipay_dict()
            else:
                params['grant'] = self.grant
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
        o = AlipayIserviceIsresourceUserpermissiongrantModifyModel()
        if 'clv_skill_group_ids' in d:
            o.clv_skill_group_ids = d['clv_skill_group_ids']
        if 'clv_user_id' in d:
            o.clv_user_id = d['clv_user_id']
        if 'grant' in d:
            o.grant = d['grant']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


