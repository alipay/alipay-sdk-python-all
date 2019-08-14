#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArchiveFaceExtInfo(object):

    def __init__(self):
        self._provider_uid = None

    @property
    def provider_uid(self):
        return self._provider_uid

    @provider_uid.setter
    def provider_uid(self, value):
        self._provider_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.provider_uid:
            if hasattr(self.provider_uid, 'to_alipay_dict'):
                params['provider_uid'] = self.provider_uid.to_alipay_dict()
            else:
                params['provider_uid'] = self.provider_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArchiveFaceExtInfo()
        if 'provider_uid' in d:
            o.provider_uid = d['provider_uid']
        return o


