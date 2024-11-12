#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BaseInfoApiConfig import BaseInfoApiConfig
from alipay.aop.api.domain.RiskApiConfig import RiskApiConfig
from alipay.aop.api.domain.ExtInfoApiConfig import ExtInfoApiConfig
from alipay.aop.api.domain.PromiseApiConfig import PromiseApiConfig
from alipay.aop.api.domain.RiskApiConfig import RiskApiConfig


class ZhimaMerchantCreditserviceCreateModel(object):

    def __init__(self):
        self._base_info_config = None
        self._biz_no = None
        self._create_type = None
        self._evaluation_risk_configs = None
        self._ext_info_config = None
        self._promise_config = None
        self._risk_config = None
        self._smid = None
        self._solution_id = None
        self._sub_pid = None

    @property
    def base_info_config(self):
        return self._base_info_config

    @base_info_config.setter
    def base_info_config(self, value):
        if isinstance(value, BaseInfoApiConfig):
            self._base_info_config = value
        else:
            self._base_info_config = BaseInfoApiConfig.from_alipay_dict(value)
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
    def evaluation_risk_configs(self):
        return self._evaluation_risk_configs

    @evaluation_risk_configs.setter
    def evaluation_risk_configs(self, value):
        if isinstance(value, list):
            self._evaluation_risk_configs = list()
            for i in value:
                if isinstance(i, RiskApiConfig):
                    self._evaluation_risk_configs.append(i)
                else:
                    self._evaluation_risk_configs.append(RiskApiConfig.from_alipay_dict(i))
    @property
    def ext_info_config(self):
        return self._ext_info_config

    @ext_info_config.setter
    def ext_info_config(self, value):
        if isinstance(value, ExtInfoApiConfig):
            self._ext_info_config = value
        else:
            self._ext_info_config = ExtInfoApiConfig.from_alipay_dict(value)
    @property
    def promise_config(self):
        return self._promise_config

    @promise_config.setter
    def promise_config(self, value):
        if isinstance(value, PromiseApiConfig):
            self._promise_config = value
        else:
            self._promise_config = PromiseApiConfig.from_alipay_dict(value)
    @property
    def risk_config(self):
        return self._risk_config

    @risk_config.setter
    def risk_config(self, value):
        if isinstance(value, RiskApiConfig):
            self._risk_config = value
        else:
            self._risk_config = RiskApiConfig.from_alipay_dict(value)
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
    @property
    def sub_pid(self):
        return self._sub_pid

    @sub_pid.setter
    def sub_pid(self, value):
        self._sub_pid = value


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
        if self.evaluation_risk_configs:
            if isinstance(self.evaluation_risk_configs, list):
                for i in range(0, len(self.evaluation_risk_configs)):
                    element = self.evaluation_risk_configs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.evaluation_risk_configs[i] = element.to_alipay_dict()
            if hasattr(self.evaluation_risk_configs, 'to_alipay_dict'):
                params['evaluation_risk_configs'] = self.evaluation_risk_configs.to_alipay_dict()
            else:
                params['evaluation_risk_configs'] = self.evaluation_risk_configs
        if self.ext_info_config:
            if hasattr(self.ext_info_config, 'to_alipay_dict'):
                params['ext_info_config'] = self.ext_info_config.to_alipay_dict()
            else:
                params['ext_info_config'] = self.ext_info_config
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
        if self.sub_pid:
            if hasattr(self.sub_pid, 'to_alipay_dict'):
                params['sub_pid'] = self.sub_pid.to_alipay_dict()
            else:
                params['sub_pid'] = self.sub_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantCreditserviceCreateModel()
        if 'base_info_config' in d:
            o.base_info_config = d['base_info_config']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'create_type' in d:
            o.create_type = d['create_type']
        if 'evaluation_risk_configs' in d:
            o.evaluation_risk_configs = d['evaluation_risk_configs']
        if 'ext_info_config' in d:
            o.ext_info_config = d['ext_info_config']
        if 'promise_config' in d:
            o.promise_config = d['promise_config']
        if 'risk_config' in d:
            o.risk_config = d['risk_config']
        if 'smid' in d:
            o.smid = d['smid']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        if 'sub_pid' in d:
            o.sub_pid = d['sub_pid']
        return o


