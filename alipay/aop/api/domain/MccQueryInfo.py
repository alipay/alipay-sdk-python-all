#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MccQueryInfo(object):

    def __init__(self):
        self._is_special = None
        self._mcc_level_1 = None
        self._mcc_level_1_name = None
        self._mcc_level_2 = None
        self._mcc_level_2_name = None
        self._mcc_requirements = None
        self._special_qual_required = None

    @property
    def is_special(self):
        return self._is_special

    @is_special.setter
    def is_special(self, value):
        self._is_special = value
    @property
    def mcc_level_1(self):
        return self._mcc_level_1

    @mcc_level_1.setter
    def mcc_level_1(self, value):
        self._mcc_level_1 = value
    @property
    def mcc_level_1_name(self):
        return self._mcc_level_1_name

    @mcc_level_1_name.setter
    def mcc_level_1_name(self, value):
        self._mcc_level_1_name = value
    @property
    def mcc_level_2(self):
        return self._mcc_level_2

    @mcc_level_2.setter
    def mcc_level_2(self, value):
        self._mcc_level_2 = value
    @property
    def mcc_level_2_name(self):
        return self._mcc_level_2_name

    @mcc_level_2_name.setter
    def mcc_level_2_name(self, value):
        self._mcc_level_2_name = value
    @property
    def mcc_requirements(self):
        return self._mcc_requirements

    @mcc_requirements.setter
    def mcc_requirements(self, value):
        self._mcc_requirements = value
    @property
    def special_qual_required(self):
        return self._special_qual_required

    @special_qual_required.setter
    def special_qual_required(self, value):
        self._special_qual_required = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_special:
            if hasattr(self.is_special, 'to_alipay_dict'):
                params['is_special'] = self.is_special.to_alipay_dict()
            else:
                params['is_special'] = self.is_special
        if self.mcc_level_1:
            if hasattr(self.mcc_level_1, 'to_alipay_dict'):
                params['mcc_level_1'] = self.mcc_level_1.to_alipay_dict()
            else:
                params['mcc_level_1'] = self.mcc_level_1
        if self.mcc_level_1_name:
            if hasattr(self.mcc_level_1_name, 'to_alipay_dict'):
                params['mcc_level_1_name'] = self.mcc_level_1_name.to_alipay_dict()
            else:
                params['mcc_level_1_name'] = self.mcc_level_1_name
        if self.mcc_level_2:
            if hasattr(self.mcc_level_2, 'to_alipay_dict'):
                params['mcc_level_2'] = self.mcc_level_2.to_alipay_dict()
            else:
                params['mcc_level_2'] = self.mcc_level_2
        if self.mcc_level_2_name:
            if hasattr(self.mcc_level_2_name, 'to_alipay_dict'):
                params['mcc_level_2_name'] = self.mcc_level_2_name.to_alipay_dict()
            else:
                params['mcc_level_2_name'] = self.mcc_level_2_name
        if self.mcc_requirements:
            if hasattr(self.mcc_requirements, 'to_alipay_dict'):
                params['mcc_requirements'] = self.mcc_requirements.to_alipay_dict()
            else:
                params['mcc_requirements'] = self.mcc_requirements
        if self.special_qual_required:
            if hasattr(self.special_qual_required, 'to_alipay_dict'):
                params['special_qual_required'] = self.special_qual_required.to_alipay_dict()
            else:
                params['special_qual_required'] = self.special_qual_required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MccQueryInfo()
        if 'is_special' in d:
            o.is_special = d['is_special']
        if 'mcc_level_1' in d:
            o.mcc_level_1 = d['mcc_level_1']
        if 'mcc_level_1_name' in d:
            o.mcc_level_1_name = d['mcc_level_1_name']
        if 'mcc_level_2' in d:
            o.mcc_level_2 = d['mcc_level_2']
        if 'mcc_level_2_name' in d:
            o.mcc_level_2_name = d['mcc_level_2_name']
        if 'mcc_requirements' in d:
            o.mcc_requirements = d['mcc_requirements']
        if 'special_qual_required' in d:
            o.special_qual_required = d['special_qual_required']
        return o


