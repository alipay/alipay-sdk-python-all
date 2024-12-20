#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpDishonestDefendantInfo(object):

    def __init__(self):
        self._bzxrdlxqk = None
        self._case_no = None
        self._case_register_date = None
        self._execution_court = None
        self._fddbr = None
        self._issue_date = None
        self._province = None
        self._sxbzxrmc = None
        self._sxbzxrxw = None
        self._sxflwsyw = None
        self._zczxyjdw = None
        self._zxyjwh = None

    @property
    def bzxrdlxqk(self):
        return self._bzxrdlxqk

    @bzxrdlxqk.setter
    def bzxrdlxqk(self, value):
        self._bzxrdlxqk = value
    @property
    def case_no(self):
        return self._case_no

    @case_no.setter
    def case_no(self, value):
        self._case_no = value
    @property
    def case_register_date(self):
        return self._case_register_date

    @case_register_date.setter
    def case_register_date(self, value):
        self._case_register_date = value
    @property
    def execution_court(self):
        return self._execution_court

    @execution_court.setter
    def execution_court(self, value):
        self._execution_court = value
    @property
    def fddbr(self):
        return self._fddbr

    @fddbr.setter
    def fddbr(self, value):
        self._fddbr = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def sxbzxrmc(self):
        return self._sxbzxrmc

    @sxbzxrmc.setter
    def sxbzxrmc(self, value):
        self._sxbzxrmc = value
    @property
    def sxbzxrxw(self):
        return self._sxbzxrxw

    @sxbzxrxw.setter
    def sxbzxrxw(self, value):
        self._sxbzxrxw = value
    @property
    def sxflwsyw(self):
        return self._sxflwsyw

    @sxflwsyw.setter
    def sxflwsyw(self, value):
        self._sxflwsyw = value
    @property
    def zczxyjdw(self):
        return self._zczxyjdw

    @zczxyjdw.setter
    def zczxyjdw(self, value):
        self._zczxyjdw = value
    @property
    def zxyjwh(self):
        return self._zxyjwh

    @zxyjwh.setter
    def zxyjwh(self, value):
        self._zxyjwh = value


    def to_alipay_dict(self):
        params = dict()
        if self.bzxrdlxqk:
            if hasattr(self.bzxrdlxqk, 'to_alipay_dict'):
                params['bzxrdlxqk'] = self.bzxrdlxqk.to_alipay_dict()
            else:
                params['bzxrdlxqk'] = self.bzxrdlxqk
        if self.case_no:
            if hasattr(self.case_no, 'to_alipay_dict'):
                params['case_no'] = self.case_no.to_alipay_dict()
            else:
                params['case_no'] = self.case_no
        if self.case_register_date:
            if hasattr(self.case_register_date, 'to_alipay_dict'):
                params['case_register_date'] = self.case_register_date.to_alipay_dict()
            else:
                params['case_register_date'] = self.case_register_date
        if self.execution_court:
            if hasattr(self.execution_court, 'to_alipay_dict'):
                params['execution_court'] = self.execution_court.to_alipay_dict()
            else:
                params['execution_court'] = self.execution_court
        if self.fddbr:
            if hasattr(self.fddbr, 'to_alipay_dict'):
                params['fddbr'] = self.fddbr.to_alipay_dict()
            else:
                params['fddbr'] = self.fddbr
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.sxbzxrmc:
            if hasattr(self.sxbzxrmc, 'to_alipay_dict'):
                params['sxbzxrmc'] = self.sxbzxrmc.to_alipay_dict()
            else:
                params['sxbzxrmc'] = self.sxbzxrmc
        if self.sxbzxrxw:
            if hasattr(self.sxbzxrxw, 'to_alipay_dict'):
                params['sxbzxrxw'] = self.sxbzxrxw.to_alipay_dict()
            else:
                params['sxbzxrxw'] = self.sxbzxrxw
        if self.sxflwsyw:
            if hasattr(self.sxflwsyw, 'to_alipay_dict'):
                params['sxflwsyw'] = self.sxflwsyw.to_alipay_dict()
            else:
                params['sxflwsyw'] = self.sxflwsyw
        if self.zczxyjdw:
            if hasattr(self.zczxyjdw, 'to_alipay_dict'):
                params['zczxyjdw'] = self.zczxyjdw.to_alipay_dict()
            else:
                params['zczxyjdw'] = self.zczxyjdw
        if self.zxyjwh:
            if hasattr(self.zxyjwh, 'to_alipay_dict'):
                params['zxyjwh'] = self.zxyjwh.to_alipay_dict()
            else:
                params['zxyjwh'] = self.zxyjwh
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpDishonestDefendantInfo()
        if 'bzxrdlxqk' in d:
            o.bzxrdlxqk = d['bzxrdlxqk']
        if 'case_no' in d:
            o.case_no = d['case_no']
        if 'case_register_date' in d:
            o.case_register_date = d['case_register_date']
        if 'execution_court' in d:
            o.execution_court = d['execution_court']
        if 'fddbr' in d:
            o.fddbr = d['fddbr']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'province' in d:
            o.province = d['province']
        if 'sxbzxrmc' in d:
            o.sxbzxrmc = d['sxbzxrmc']
        if 'sxbzxrxw' in d:
            o.sxbzxrxw = d['sxbzxrxw']
        if 'sxflwsyw' in d:
            o.sxflwsyw = d['sxflwsyw']
        if 'zczxyjdw' in d:
            o.zczxyjdw = d['zczxyjdw']
        if 'zxyjwh' in d:
            o.zxyjwh = d['zxyjwh']
        return o


