#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpAdminLicensePermissionTableInfo import EpAdminLicensePermissionTableInfo


class EpAdminLicenseInfo(object):

    def __init__(self):
        self._dsr = None
        self._issue_date = None
        self._source = None
        self._xkbg = None
        self._xkjg = None
        self._xknr = None
        self._xksxmc = None

    @property
    def dsr(self):
        return self._dsr

    @dsr.setter
    def dsr(self, value):
        self._dsr = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def xkbg(self):
        return self._xkbg

    @xkbg.setter
    def xkbg(self, value):
        if isinstance(value, EpAdminLicensePermissionTableInfo):
            self._xkbg = value
        else:
            self._xkbg = EpAdminLicensePermissionTableInfo.from_alipay_dict(value)
    @property
    def xkjg(self):
        return self._xkjg

    @xkjg.setter
    def xkjg(self, value):
        self._xkjg = value
    @property
    def xknr(self):
        return self._xknr

    @xknr.setter
    def xknr(self, value):
        self._xknr = value
    @property
    def xksxmc(self):
        return self._xksxmc

    @xksxmc.setter
    def xksxmc(self, value):
        self._xksxmc = value


    def to_alipay_dict(self):
        params = dict()
        if self.dsr:
            if hasattr(self.dsr, 'to_alipay_dict'):
                params['dsr'] = self.dsr.to_alipay_dict()
            else:
                params['dsr'] = self.dsr
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.xkbg:
            if hasattr(self.xkbg, 'to_alipay_dict'):
                params['xkbg'] = self.xkbg.to_alipay_dict()
            else:
                params['xkbg'] = self.xkbg
        if self.xkjg:
            if hasattr(self.xkjg, 'to_alipay_dict'):
                params['xkjg'] = self.xkjg.to_alipay_dict()
            else:
                params['xkjg'] = self.xkjg
        if self.xknr:
            if hasattr(self.xknr, 'to_alipay_dict'):
                params['xknr'] = self.xknr.to_alipay_dict()
            else:
                params['xknr'] = self.xknr
        if self.xksxmc:
            if hasattr(self.xksxmc, 'to_alipay_dict'):
                params['xksxmc'] = self.xksxmc.to_alipay_dict()
            else:
                params['xksxmc'] = self.xksxmc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpAdminLicenseInfo()
        if 'dsr' in d:
            o.dsr = d['dsr']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'source' in d:
            o.source = d['source']
        if 'xkbg' in d:
            o.xkbg = d['xkbg']
        if 'xkjg' in d:
            o.xkjg = d['xkjg']
        if 'xknr' in d:
            o.xknr = d['xknr']
        if 'xksxmc' in d:
            o.xksxmc = d['xksxmc']
        return o


