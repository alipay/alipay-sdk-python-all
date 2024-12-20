#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpEquityPledgeInfo(object):

    def __init__(self):
        self._czbd = None
        self._czgqe = None
        self._czr = None
        self._dj_time = None
        self._djbh = None
        self._issue_date = None
        self._status = None
        self._zqr = None

    @property
    def czbd(self):
        return self._czbd

    @czbd.setter
    def czbd(self, value):
        self._czbd = value
    @property
    def czgqe(self):
        return self._czgqe

    @czgqe.setter
    def czgqe(self, value):
        self._czgqe = value
    @property
    def czr(self):
        return self._czr

    @czr.setter
    def czr(self, value):
        self._czr = value
    @property
    def dj_time(self):
        return self._dj_time

    @dj_time.setter
    def dj_time(self, value):
        self._dj_time = value
    @property
    def djbh(self):
        return self._djbh

    @djbh.setter
    def djbh(self, value):
        self._djbh = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def zqr(self):
        return self._zqr

    @zqr.setter
    def zqr(self, value):
        self._zqr = value


    def to_alipay_dict(self):
        params = dict()
        if self.czbd:
            if hasattr(self.czbd, 'to_alipay_dict'):
                params['czbd'] = self.czbd.to_alipay_dict()
            else:
                params['czbd'] = self.czbd
        if self.czgqe:
            if hasattr(self.czgqe, 'to_alipay_dict'):
                params['czgqe'] = self.czgqe.to_alipay_dict()
            else:
                params['czgqe'] = self.czgqe
        if self.czr:
            if hasattr(self.czr, 'to_alipay_dict'):
                params['czr'] = self.czr.to_alipay_dict()
            else:
                params['czr'] = self.czr
        if self.dj_time:
            if hasattr(self.dj_time, 'to_alipay_dict'):
                params['dj_time'] = self.dj_time.to_alipay_dict()
            else:
                params['dj_time'] = self.dj_time
        if self.djbh:
            if hasattr(self.djbh, 'to_alipay_dict'):
                params['djbh'] = self.djbh.to_alipay_dict()
            else:
                params['djbh'] = self.djbh
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.zqr:
            if hasattr(self.zqr, 'to_alipay_dict'):
                params['zqr'] = self.zqr.to_alipay_dict()
            else:
                params['zqr'] = self.zqr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpEquityPledgeInfo()
        if 'czbd' in d:
            o.czbd = d['czbd']
        if 'czgqe' in d:
            o.czgqe = d['czgqe']
        if 'czr' in d:
            o.czr = d['czr']
        if 'dj_time' in d:
            o.dj_time = d['dj_time']
        if 'djbh' in d:
            o.djbh = d['djbh']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'status' in d:
            o.status = d['status']
        if 'zqr' in d:
            o.zqr = d['zqr']
        return o


