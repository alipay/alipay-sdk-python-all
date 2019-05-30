#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAntdataassetsCloudjobstatusQueryModel(object):

    def __init__(self):
        self._bizdate = None
        self._guid = None

    @property
    def bizdate(self):
        return self._bizdate

    @bizdate.setter
    def bizdate(self, value):
        self._bizdate = value
    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        self._guid = value


    def to_alipay_dict(self):
        params = dict()
        if self.bizdate:
            if hasattr(self.bizdate, 'to_alipay_dict'):
                params['bizdate'] = self.bizdate.to_alipay_dict()
            else:
                params['bizdate'] = self.bizdate
        if self.guid:
            if hasattr(self.guid, 'to_alipay_dict'):
                params['guid'] = self.guid.to_alipay_dict()
            else:
                params['guid'] = self.guid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAntdataassetsCloudjobstatusQueryModel()
        if 'bizdate' in d:
            o.bizdate = d['bizdate']
        if 'guid' in d:
            o.guid = d['guid']
        return o


