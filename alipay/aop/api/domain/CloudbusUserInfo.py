#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudbusUserInfo(object):

    def __init__(self):
        self._age_chrild = None
        self._age_mider = None
        self._age_older = None
        self._age_youth = None
        self._sex_man = None
        self._sex_woman = None
        self._w_officer = None
        self._w_unofficer = None

    @property
    def age_chrild(self):
        return self._age_chrild

    @age_chrild.setter
    def age_chrild(self, value):
        self._age_chrild = value
    @property
    def age_mider(self):
        return self._age_mider

    @age_mider.setter
    def age_mider(self, value):
        self._age_mider = value
    @property
    def age_older(self):
        return self._age_older

    @age_older.setter
    def age_older(self, value):
        self._age_older = value
    @property
    def age_youth(self):
        return self._age_youth

    @age_youth.setter
    def age_youth(self, value):
        self._age_youth = value
    @property
    def sex_man(self):
        return self._sex_man

    @sex_man.setter
    def sex_man(self, value):
        self._sex_man = value
    @property
    def sex_woman(self):
        return self._sex_woman

    @sex_woman.setter
    def sex_woman(self, value):
        self._sex_woman = value
    @property
    def w_officer(self):
        return self._w_officer

    @w_officer.setter
    def w_officer(self, value):
        self._w_officer = value
    @property
    def w_unofficer(self):
        return self._w_unofficer

    @w_unofficer.setter
    def w_unofficer(self, value):
        self._w_unofficer = value


    def to_alipay_dict(self):
        params = dict()
        if self.age_chrild:
            if hasattr(self.age_chrild, 'to_alipay_dict'):
                params['age_chrild'] = self.age_chrild.to_alipay_dict()
            else:
                params['age_chrild'] = self.age_chrild
        if self.age_mider:
            if hasattr(self.age_mider, 'to_alipay_dict'):
                params['age_mider'] = self.age_mider.to_alipay_dict()
            else:
                params['age_mider'] = self.age_mider
        if self.age_older:
            if hasattr(self.age_older, 'to_alipay_dict'):
                params['age_older'] = self.age_older.to_alipay_dict()
            else:
                params['age_older'] = self.age_older
        if self.age_youth:
            if hasattr(self.age_youth, 'to_alipay_dict'):
                params['age_youth'] = self.age_youth.to_alipay_dict()
            else:
                params['age_youth'] = self.age_youth
        if self.sex_man:
            if hasattr(self.sex_man, 'to_alipay_dict'):
                params['sex_man'] = self.sex_man.to_alipay_dict()
            else:
                params['sex_man'] = self.sex_man
        if self.sex_woman:
            if hasattr(self.sex_woman, 'to_alipay_dict'):
                params['sex_woman'] = self.sex_woman.to_alipay_dict()
            else:
                params['sex_woman'] = self.sex_woman
        if self.w_officer:
            if hasattr(self.w_officer, 'to_alipay_dict'):
                params['w_officer'] = self.w_officer.to_alipay_dict()
            else:
                params['w_officer'] = self.w_officer
        if self.w_unofficer:
            if hasattr(self.w_unofficer, 'to_alipay_dict'):
                params['w_unofficer'] = self.w_unofficer.to_alipay_dict()
            else:
                params['w_unofficer'] = self.w_unofficer
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudbusUserInfo()
        if 'age_chrild' in d:
            o.age_chrild = d['age_chrild']
        if 'age_mider' in d:
            o.age_mider = d['age_mider']
        if 'age_older' in d:
            o.age_older = d['age_older']
        if 'age_youth' in d:
            o.age_youth = d['age_youth']
        if 'sex_man' in d:
            o.sex_man = d['sex_man']
        if 'sex_woman' in d:
            o.sex_woman = d['sex_woman']
        if 'w_officer' in d:
            o.w_officer = d['w_officer']
        if 'w_unofficer' in d:
            o.w_unofficer = d['w_unofficer']
        return o


