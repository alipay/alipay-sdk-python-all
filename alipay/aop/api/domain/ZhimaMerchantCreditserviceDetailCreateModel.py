#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BaseInfoConfig import BaseInfoConfig
from alipay.aop.api.domain.PromiseConfig import PromiseConfig
from alipay.aop.api.domain.RiskConfig import RiskConfig


class ZhimaMerchantCreditserviceDetailCreateModel(object):

    def __init__(self):
        self._base_info_config = None
        self._biz_no = None
        self._create_type = None
        self._extra_info = None
        self._promise_config = None
        self._risk_config = None
        self._smid = None
        self._solution_id = None

    @property
    def base_info_config(self):
        return self._base_info_config

    @base_info_config.setter
    def base_info_config(self, value):
        if isinstance(value, BaseInfoConfig):
            self._base_info_config = value
        else:
            self._base_info_config = BaseInfoConfig.from_alipay_dict(value)
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def create_type(self):
        return self._create_type

    @create_type.setter
    def create_type(self, value):
        self._create_type = value
    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        self._extra_info = value
    @property
    def promise_config(self):
        return self._promise_config

    @promise_config.setter
    def promise_config(self, value):
        if isinstance(value, PromiseConfig):
            self._promise_config = value
        else:
            self._promise_config = PromiseConfig.from_alipay_dict(value)
    @property
    def risk_config(self):
        return self._risk_config

    @risk_config.setter
    def risk_config(self, value):
        if isinstance(value, RiskConfig):
            self._risk_config = value
        else:
            self._risk_config = RiskConfig.from_alipay_dict(value)
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_info_config:
            if hasattr(self.base_info_config, 'to_alipay_dict'):
                params['base_info_config'] = self.base_info_config.to_alipay_dict()
            else:
                params['base_info_config'] = self.base_info_config
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.create_type:
            if hasattr(self.create_type, 'to_alipay_dict'):
                params['create_type'] = self.create_type.to_alipay_dict()
            else:
                params['create_type'] = self.create_type
        if self.extra_info:
            if hasattr(self.extra_info, 'to_alipay_dict'):
                params['extra_info'] = self.extra_info.to_alipay_dict()
            else:
                params['extra_info'] = self.extra_info
        if self.promise_config:
            if hasattr(self.promise_config, 'to_alipay_dict'):
                params['promise_config'] = self.promise_config.to_alipay_dict()
            else:
                params['promise_config'] = self.promise_config
        if self.risk_config:
            if hasattr(self.risk_config, 'to_alipay_dict'):
                params['risk_config'] = self.risk_config.to_alipay_dict()
            else:
                params['risk_config'] = self.risk_config
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantCreditserviceDetailCreateModel()
        if 'base_info_config' in d:
            o.base_info_config = d['base_info_config']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'create_type' in d:
            o.create_type = d['create_type']
        if 'extra_info' in d:
            o.extra_info = d['extra_info']
        if 'promise_config' in d:
            o.promise_config = d['promise_config']
        if 'risk_config' in d:
            o.risk_config = d['risk_config']
        if 'smid' in d:
            o.smid = d['smid']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        return o


