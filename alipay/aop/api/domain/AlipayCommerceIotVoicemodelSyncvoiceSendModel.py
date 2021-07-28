#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceModelContext import ServiceModelContext
from alipay.aop.api.domain.SyncVoiceVO import SyncVoiceVO


class AlipayCommerceIotVoicemodelSyncvoiceSendModel(object):

    def __init__(self):
        self._context = None
        self._sync_data = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, ServiceModelContext):
            self._context = value
        else:
            self._context = ServiceModelContext.from_alipay_dict(value)
    @property
    def sync_data(self):
        return self._sync_data

    @sync_data.setter
    def sync_data(self, value):
        if isinstance(value, SyncVoiceVO):
            self._sync_data = value
        else:
            self._sync_data = SyncVoiceVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.sync_data:
            if hasattr(self.sync_data, 'to_alipay_dict'):
                params['sync_data'] = self.sync_data.to_alipay_dict()
            else:
                params['sync_data'] = self.sync_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotVoicemodelSyncvoiceSendModel()
        if 'context' in d:
            o.context = d['context']
        if 'sync_data' in d:
            o.sync_data = d['sync_data']
        return o


