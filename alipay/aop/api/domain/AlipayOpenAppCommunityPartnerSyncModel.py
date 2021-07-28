#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommunityPartnerRelationDataSyncDTO import CommunityPartnerRelationDataSyncDTO


class AlipayOpenAppCommunityPartnerSyncModel(object):

    def __init__(self):
        self._action = None
        self._rela_type = None
        self._source_channel = None
        self._source_id = None
        self._target_list = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def rela_type(self):
        return self._rela_type

    @rela_type.setter
    def rela_type(self, value):
        self._rela_type = value
    @property
    def source_channel(self):
        return self._source_channel

    @source_channel.setter
    def source_channel(self, value):
        self._source_channel = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def target_list(self):
        return self._target_list

    @target_list.setter
    def target_list(self, value):
        if isinstance(value, list):
            self._target_list = list()
            for i in value:
                if isinstance(i, CommunityPartnerRelationDataSyncDTO):
                    self._target_list.append(i)
                else:
                    self._target_list.append(CommunityPartnerRelationDataSyncDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.rela_type:
            if hasattr(self.rela_type, 'to_alipay_dict'):
                params['rela_type'] = self.rela_type.to_alipay_dict()
            else:
                params['rela_type'] = self.rela_type
        if self.source_channel:
            if hasattr(self.source_channel, 'to_alipay_dict'):
                params['source_channel'] = self.source_channel.to_alipay_dict()
            else:
                params['source_channel'] = self.source_channel
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.target_list:
            if isinstance(self.target_list, list):
                for i in range(0, len(self.target_list)):
                    element = self.target_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_list[i] = element.to_alipay_dict()
            if hasattr(self.target_list, 'to_alipay_dict'):
                params['target_list'] = self.target_list.to_alipay_dict()
            else:
                params['target_list'] = self.target_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppCommunityPartnerSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'rela_type' in d:
            o.rela_type = d['rela_type']
        if 'source_channel' in d:
            o.source_channel = d['source_channel']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'target_list' in d:
            o.target_list = d['target_list']
        return o


