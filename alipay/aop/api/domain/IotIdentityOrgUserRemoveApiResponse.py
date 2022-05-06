#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotIdentityOrgUserRemoveApiResponse(object):

    def __init__(self):
        self._event_id = None

    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotIdentityOrgUserRemoveApiResponse()
        if 'event_id' in d:
            o.event_id = d['event_id']
        return o


