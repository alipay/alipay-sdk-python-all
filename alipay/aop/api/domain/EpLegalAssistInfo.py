#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpLegalAssistInfo(object):

    def __init__(self):
        self._assignee = None
        self._djqx = None
        self._djzxzi = None
        self._enforcement_actions = None
        self._execution_court = None
        self._gqdjzt = None
        self._gqszqymc = None
        self._person_subject_to_enforcement = None
        self._publicity_date = None
        self._sfxzlx = None
        self._stock_right_sum = None
        self._zjqxzhi = None
        self._zxcdswh = None
        self._zxtzswh = None

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        self._assignee = value
    @property
    def djqx(self):
        return self._djqx

    @djqx.setter
    def djqx(self, value):
        self._djqx = value
    @property
    def djzxzi(self):
        return self._djzxzi

    @djzxzi.setter
    def djzxzi(self, value):
        self._djzxzi = value
    @property
    def enforcement_actions(self):
        return self._enforcement_actions

    @enforcement_actions.setter
    def enforcement_actions(self, value):
        self._enforcement_actions = value
    @property
    def execution_court(self):
        return self._execution_court

    @execution_court.setter
    def execution_court(self, value):
        self._execution_court = value
    @property
    def gqdjzt(self):
        return self._gqdjzt

    @gqdjzt.setter
    def gqdjzt(self, value):
        self._gqdjzt = value
    @property
    def gqszqymc(self):
        return self._gqszqymc

    @gqszqymc.setter
    def gqszqymc(self, value):
        self._gqszqymc = value
    @property
    def person_subject_to_enforcement(self):
        return self._person_subject_to_enforcement

    @person_subject_to_enforcement.setter
    def person_subject_to_enforcement(self, value):
        self._person_subject_to_enforcement = value
    @property
    def publicity_date(self):
        return self._publicity_date

    @publicity_date.setter
    def publicity_date(self, value):
        self._publicity_date = value
    @property
    def sfxzlx(self):
        return self._sfxzlx

    @sfxzlx.setter
    def sfxzlx(self, value):
        self._sfxzlx = value
    @property
    def stock_right_sum(self):
        return self._stock_right_sum

    @stock_right_sum.setter
    def stock_right_sum(self, value):
        self._stock_right_sum = value
    @property
    def zjqxzhi(self):
        return self._zjqxzhi

    @zjqxzhi.setter
    def zjqxzhi(self, value):
        self._zjqxzhi = value
    @property
    def zxcdswh(self):
        return self._zxcdswh

    @zxcdswh.setter
    def zxcdswh(self, value):
        self._zxcdswh = value
    @property
    def zxtzswh(self):
        return self._zxtzswh

    @zxtzswh.setter
    def zxtzswh(self, value):
        self._zxtzswh = value


    def to_alipay_dict(self):
        params = dict()
        if self.assignee:
            if hasattr(self.assignee, 'to_alipay_dict'):
                params['assignee'] = self.assignee.to_alipay_dict()
            else:
                params['assignee'] = self.assignee
        if self.djqx:
            if hasattr(self.djqx, 'to_alipay_dict'):
                params['djqx'] = self.djqx.to_alipay_dict()
            else:
                params['djqx'] = self.djqx
        if self.djzxzi:
            if hasattr(self.djzxzi, 'to_alipay_dict'):
                params['djzxzi'] = self.djzxzi.to_alipay_dict()
            else:
                params['djzxzi'] = self.djzxzi
        if self.enforcement_actions:
            if hasattr(self.enforcement_actions, 'to_alipay_dict'):
                params['enforcement_actions'] = self.enforcement_actions.to_alipay_dict()
            else:
                params['enforcement_actions'] = self.enforcement_actions
        if self.execution_court:
            if hasattr(self.execution_court, 'to_alipay_dict'):
                params['execution_court'] = self.execution_court.to_alipay_dict()
            else:
                params['execution_court'] = self.execution_court
        if self.gqdjzt:
            if hasattr(self.gqdjzt, 'to_alipay_dict'):
                params['gqdjzt'] = self.gqdjzt.to_alipay_dict()
            else:
                params['gqdjzt'] = self.gqdjzt
        if self.gqszqymc:
            if hasattr(self.gqszqymc, 'to_alipay_dict'):
                params['gqszqymc'] = self.gqszqymc.to_alipay_dict()
            else:
                params['gqszqymc'] = self.gqszqymc
        if self.person_subject_to_enforcement:
            if hasattr(self.person_subject_to_enforcement, 'to_alipay_dict'):
                params['person_subject_to_enforcement'] = self.person_subject_to_enforcement.to_alipay_dict()
            else:
                params['person_subject_to_enforcement'] = self.person_subject_to_enforcement
        if self.publicity_date:
            if hasattr(self.publicity_date, 'to_alipay_dict'):
                params['publicity_date'] = self.publicity_date.to_alipay_dict()
            else:
                params['publicity_date'] = self.publicity_date
        if self.sfxzlx:
            if hasattr(self.sfxzlx, 'to_alipay_dict'):
                params['sfxzlx'] = self.sfxzlx.to_alipay_dict()
            else:
                params['sfxzlx'] = self.sfxzlx
        if self.stock_right_sum:
            if hasattr(self.stock_right_sum, 'to_alipay_dict'):
                params['stock_right_sum'] = self.stock_right_sum.to_alipay_dict()
            else:
                params['stock_right_sum'] = self.stock_right_sum
        if self.zjqxzhi:
            if hasattr(self.zjqxzhi, 'to_alipay_dict'):
                params['zjqxzhi'] = self.zjqxzhi.to_alipay_dict()
            else:
                params['zjqxzhi'] = self.zjqxzhi
        if self.zxcdswh:
            if hasattr(self.zxcdswh, 'to_alipay_dict'):
                params['zxcdswh'] = self.zxcdswh.to_alipay_dict()
            else:
                params['zxcdswh'] = self.zxcdswh
        if self.zxtzswh:
            if hasattr(self.zxtzswh, 'to_alipay_dict'):
                params['zxtzswh'] = self.zxtzswh.to_alipay_dict()
            else:
                params['zxtzswh'] = self.zxtzswh
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpLegalAssistInfo()
        if 'assignee' in d:
            o.assignee = d['assignee']
        if 'djqx' in d:
            o.djqx = d['djqx']
        if 'djzxzi' in d:
            o.djzxzi = d['djzxzi']
        if 'enforcement_actions' in d:
            o.enforcement_actions = d['enforcement_actions']
        if 'execution_court' in d:
            o.execution_court = d['execution_court']
        if 'gqdjzt' in d:
            o.gqdjzt = d['gqdjzt']
        if 'gqszqymc' in d:
            o.gqszqymc = d['gqszqymc']
        if 'person_subject_to_enforcement' in d:
            o.person_subject_to_enforcement = d['person_subject_to_enforcement']
        if 'publicity_date' in d:
            o.publicity_date = d['publicity_date']
        if 'sfxzlx' in d:
            o.sfxzlx = d['sfxzlx']
        if 'stock_right_sum' in d:
            o.stock_right_sum = d['stock_right_sum']
        if 'zjqxzhi' in d:
            o.zjqxzhi = d['zjqxzhi']
        if 'zxcdswh' in d:
            o.zxcdswh = d['zxcdswh']
        if 'zxtzswh' in d:
            o.zxtzswh = d['zxtzswh']
        return o


