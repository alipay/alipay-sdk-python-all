#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExternalSyncRequest import ExternalSyncRequest


class AlipayEbppCommunityExternalbillsyncUploadModel(object):

    def __init__(self):
        self._community_short_name = None
        self._external_sync_list = None

    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def external_sync_list(self):
        return self._external_sync_list

    @external_sync_list.setter
    def external_sync_list(self, value):
        if isinstance(value, list):
            self._external_sync_list = list()
            for i in value:
                if isinstance(i, ExternalSyncRequest):
                    self._external_sync_list.append(i)
                else:
                    self._external_sync_list.append(ExternalSyncRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.external_sync_list:
            if isinstance(self.external_sync_list, list):
                for i in range(0, len(self.external_sync_list)):
                    element = self.external_sync_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.external_sync_list[i] = element.to_alipay_dict()
            if hasattr(self.external_sync_list, 'to_alipay_dict'):
                params['external_sync_list'] = self.external_sync_list.to_alipay_dict()
            else:
                params['external_sync_list'] = self.external_sync_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityExternalbillsyncUploadModel()
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'external_sync_list' in d:
            o.external_sync_list = d['external_sync_list']
        return o


