#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntforestWelfareforestTransferModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_no = None
        self._energy = None
        self._open_id = None
        self._source = None
        self._user_id = None
        self._welfare_forest_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def welfare_forest_id(self):
        return self._welfare_forest_id

    @welfare_forest_id.setter
    def welfare_forest_id(self, value):
        self._welfare_forest_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.energy:
            if hasattr(self.energy, 'to_alipay_dict'):
                params['energy'] = self.energy.to_alipay_dict()
            else:
                params['energy'] = self.energy
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.welfare_forest_id:
            if hasattr(self.welfare_forest_id, 'to_alipay_dict'):
                params['welfare_forest_id'] = self.welfare_forest_id.to_alipay_dict()
            else:
                params['welfare_forest_id'] = self.welfare_forest_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialAntforestWelfareforestTransferModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'energy' in d:
            o.energy = d['energy']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'welfare_forest_id' in d:
            o.welfare_forest_id = d['welfare_forest_id']
        return o


