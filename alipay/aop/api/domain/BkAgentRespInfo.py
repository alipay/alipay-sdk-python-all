#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BkAgentRespInfo(object):

    def __init__(self):
        self._bindclrissr_id = None
        self._bindpyeracctbk_id = None
        self._bindtrx_id = None
        self._bkpyeruser_code = None
        self._estter_location = None

    @property
    def bindclrissr_id(self):
        return self._bindclrissr_id

    @bindclrissr_id.setter
    def bindclrissr_id(self, value):
        self._bindclrissr_id = value
    @property
    def bindpyeracctbk_id(self):
        return self._bindpyeracctbk_id

    @bindpyeracctbk_id.setter
    def bindpyeracctbk_id(self, value):
        self._bindpyeracctbk_id = value
    @property
    def bindtrx_id(self):
        return self._bindtrx_id

    @bindtrx_id.setter
    def bindtrx_id(self, value):
        self._bindtrx_id = value
    @property
    def bkpyeruser_code(self):
        return self._bkpyeruser_code

    @bkpyeruser_code.setter
    def bkpyeruser_code(self, value):
        self._bkpyeruser_code = value
    @property
    def estter_location(self):
        return self._estter_location

    @estter_location.setter
    def estter_location(self, value):
        self._estter_location = value


    def to_alipay_dict(self):
        params = dict()
        if self.bindclrissr_id:
            if hasattr(self.bindclrissr_id, 'to_alipay_dict'):
                params['bindclrissr_id'] = self.bindclrissr_id.to_alipay_dict()
            else:
                params['bindclrissr_id'] = self.bindclrissr_id
        if self.bindpyeracctbk_id:
            if hasattr(self.bindpyeracctbk_id, 'to_alipay_dict'):
                params['bindpyeracctbk_id'] = self.bindpyeracctbk_id.to_alipay_dict()
            else:
                params['bindpyeracctbk_id'] = self.bindpyeracctbk_id
        if self.bindtrx_id:
            if hasattr(self.bindtrx_id, 'to_alipay_dict'):
                params['bindtrx_id'] = self.bindtrx_id.to_alipay_dict()
            else:
                params['bindtrx_id'] = self.bindtrx_id
        if self.bkpyeruser_code:
            if hasattr(self.bkpyeruser_code, 'to_alipay_dict'):
                params['bkpyeruser_code'] = self.bkpyeruser_code.to_alipay_dict()
            else:
                params['bkpyeruser_code'] = self.bkpyeruser_code
        if self.estter_location:
            if hasattr(self.estter_location, 'to_alipay_dict'):
                params['estter_location'] = self.estter_location.to_alipay_dict()
            else:
                params['estter_location'] = self.estter_location
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BkAgentRespInfo()
        if 'bindclrissr_id' in d:
            o.bindclrissr_id = d['bindclrissr_id']
        if 'bindpyeracctbk_id' in d:
            o.bindpyeracctbk_id = d['bindpyeracctbk_id']
        if 'bindtrx_id' in d:
            o.bindtrx_id = d['bindtrx_id']
        if 'bkpyeruser_code' in d:
            o.bkpyeruser_code = d['bkpyeruser_code']
        if 'estter_location' in d:
            o.estter_location = d['estter_location']
        return o


