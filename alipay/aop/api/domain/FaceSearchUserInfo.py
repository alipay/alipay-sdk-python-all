#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaceSearchUserInfo(object):

    def __init__(self):
        self._customuserid = None
        self._merchantid = None
        self._merchantuid = None
        self._score = None

    @property
    def customuserid(self):
        return self._customuserid

    @customuserid.setter
    def customuserid(self, value):
        self._customuserid = value
    @property
    def merchantid(self):
        return self._merchantid

    @merchantid.setter
    def merchantid(self, value):
        self._merchantid = value
    @property
    def merchantuid(self):
        return self._merchantuid

    @merchantuid.setter
    def merchantuid(self, value):
        self._merchantuid = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.customuserid:
            if hasattr(self.customuserid, 'to_alipay_dict'):
                params['customuserid'] = self.customuserid.to_alipay_dict()
            else:
                params['customuserid'] = self.customuserid
        if self.merchantid:
            if hasattr(self.merchantid, 'to_alipay_dict'):
                params['merchantid'] = self.merchantid.to_alipay_dict()
            else:
                params['merchantid'] = self.merchantid
        if self.merchantuid:
            if hasattr(self.merchantuid, 'to_alipay_dict'):
                params['merchantuid'] = self.merchantuid.to_alipay_dict()
            else:
                params['merchantuid'] = self.merchantuid
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaceSearchUserInfo()
        if 'customuserid' in d:
            o.customuserid = d['customuserid']
        if 'merchantid' in d:
            o.merchantid = d['merchantid']
        if 'merchantuid' in d:
            o.merchantuid = d['merchantuid']
        if 'score' in d:
            o.score = d['score']
        return o


