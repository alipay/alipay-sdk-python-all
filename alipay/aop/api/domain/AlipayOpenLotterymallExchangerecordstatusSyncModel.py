#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenLotterymallExchangerecordstatusSyncModel(object):

    def __init__(self):
        self._env = None
        self._extinfo = None
        self._mallexchangerecordid = None
        self._now = None
        self._outbizid = None
        self._target = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def extinfo(self):
        return self._extinfo

    @extinfo.setter
    def extinfo(self, value):
        self._extinfo = value
    @property
    def mallexchangerecordid(self):
        return self._mallexchangerecordid

    @mallexchangerecordid.setter
    def mallexchangerecordid(self, value):
        self._mallexchangerecordid = value
    @property
    def now(self):
        return self._now

    @now.setter
    def now(self, value):
        self._now = value
    @property
    def outbizid(self):
        return self._outbizid

    @outbizid.setter
    def outbizid(self, value):
        self._outbizid = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value


    def to_alipay_dict(self):
        params = dict()
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.extinfo:
            if hasattr(self.extinfo, 'to_alipay_dict'):
                params['extinfo'] = self.extinfo.to_alipay_dict()
            else:
                params['extinfo'] = self.extinfo
        if self.mallexchangerecordid:
            if hasattr(self.mallexchangerecordid, 'to_alipay_dict'):
                params['mallexchangerecordid'] = self.mallexchangerecordid.to_alipay_dict()
            else:
                params['mallexchangerecordid'] = self.mallexchangerecordid
        if self.now:
            if hasattr(self.now, 'to_alipay_dict'):
                params['now'] = self.now.to_alipay_dict()
            else:
                params['now'] = self.now
        if self.outbizid:
            if hasattr(self.outbizid, 'to_alipay_dict'):
                params['outbizid'] = self.outbizid.to_alipay_dict()
            else:
                params['outbizid'] = self.outbizid
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenLotterymallExchangerecordstatusSyncModel()
        if 'env' in d:
            o.env = d['env']
        if 'extinfo' in d:
            o.extinfo = d['extinfo']
        if 'mallexchangerecordid' in d:
            o.mallexchangerecordid = d['mallexchangerecordid']
        if 'now' in d:
            o.now = d['now']
        if 'outbizid' in d:
            o.outbizid = d['outbizid']
        if 'target' in d:
            o.target = d['target']
        return o


