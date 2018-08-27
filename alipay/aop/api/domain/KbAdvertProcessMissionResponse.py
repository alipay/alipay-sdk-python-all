#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertProcessMissionResponse(object):

    def __init__(self):
        self._identify = None
        self._identify_type = None
        self._promote_status = None

    @property
    def identify(self):
        return self._identify

    @identify.setter
    def identify(self, value):
        self._identify = value
    @property
    def identify_type(self):
        return self._identify_type

    @identify_type.setter
    def identify_type(self, value):
        self._identify_type = value
    @property
    def promote_status(self):
        return self._promote_status

    @promote_status.setter
    def promote_status(self, value):
        self._promote_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.identify:
            if hasattr(self.identify, 'to_alipay_dict'):
                params['identify'] = self.identify.to_alipay_dict()
            else:
                params['identify'] = self.identify
        if self.identify_type:
            if hasattr(self.identify_type, 'to_alipay_dict'):
                params['identify_type'] = self.identify_type.to_alipay_dict()
            else:
                params['identify_type'] = self.identify_type
        if self.promote_status:
            if hasattr(self.promote_status, 'to_alipay_dict'):
                params['promote_status'] = self.promote_status.to_alipay_dict()
            else:
                params['promote_status'] = self.promote_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertProcessMissionResponse()
        if 'identify' in d:
            o.identify = d['identify']
        if 'identify_type' in d:
            o.identify_type = d['identify_type']
        if 'promote_status' in d:
            o.promote_status = d['promote_status']
        return o


