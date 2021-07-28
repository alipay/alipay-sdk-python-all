#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserFamilyArchiveQueryModel(object):

    def __init__(self):
        self._archive_token = None

    @property
    def archive_token(self):
        return self._archive_token

    @archive_token.setter
    def archive_token(self, value):
        self._archive_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.archive_token:
            if hasattr(self.archive_token, 'to_alipay_dict'):
                params['archive_token'] = self.archive_token.to_alipay_dict()
            else:
                params['archive_token'] = self.archive_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserFamilyArchiveQueryModel()
        if 'archive_token' in d:
            o.archive_token = d['archive_token']
        return o


