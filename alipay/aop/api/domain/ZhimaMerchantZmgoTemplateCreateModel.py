#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZMGOBasicConfig import ZMGOBasicConfig
from alipay.aop.api.domain.ZMGOExtConfig import ZMGOExtConfig
from alipay.aop.api.domain.ZMGOObligationConfig import ZMGOObligationConfig
from alipay.aop.api.domain.ZMGOOpenConfig import ZMGOOpenConfig
from alipay.aop.api.domain.ZMGOQuitConfig import ZMGOQuitConfig
from alipay.aop.api.domain.ZMGORightConfig import ZMGORightConfig
from alipay.aop.api.domain.ZMGOSettlementConfig import ZMGOSettlementConfig


class ZhimaMerchantZmgoTemplateCreateModel(object):

    def __init__(self):
        self._basic_config = None
        self._ext_config = None
        self._obligation_config = None
        self._open_config = None
        self._quit_config = None
        self._right_config = None
        self._settlement_config = None

    @property
    def basic_config(self):
        return self._basic_config

    @basic_config.setter
    def basic_config(self, value):
        if isinstance(value, ZMGOBasicConfig):
            self._basic_config = value
        else:
            self._basic_config = ZMGOBasicConfig.from_alipay_dict(value)
    @property
    def ext_config(self):
        return self._ext_config

    @ext_config.setter
    def ext_config(self, value):
        if isinstance(value, ZMGOExtConfig):
            self._ext_config = value
        else:
            self._ext_config = ZMGOExtConfig.from_alipay_dict(value)
    @property
    def obligation_config(self):
        return self._obligation_config

    @obligation_config.setter
    def obligation_config(self, value):
        if isinstance(value, ZMGOObligationConfig):
            self._obligation_config = value
        else:
            self._obligation_config = ZMGOObligationConfig.from_alipay_dict(value)
    @property
    def open_config(self):
        return self._open_config

    @open_config.setter
    def open_config(self, value):
        if isinstance(value, ZMGOOpenConfig):
            self._open_config = value
        else:
            self._open_config = ZMGOOpenConfig.from_alipay_dict(value)
    @property
    def quit_config(self):
        return self._quit_config

    @quit_config.setter
    def quit_config(self, value):
        if isinstance(value, ZMGOQuitConfig):
            self._quit_config = value
        else:
            self._quit_config = ZMGOQuitConfig.from_alipay_dict(value)
    @property
    def right_config(self):
        return self._right_config

    @right_config.setter
    def right_config(self, value):
        if isinstance(value, ZMGORightConfig):
            self._right_config = value
        else:
            self._right_config = ZMGORightConfig.from_alipay_dict(value)
    @property
    def settlement_config(self):
        return self._settlement_config

    @settlement_config.setter
    def settlement_config(self, value):
        if isinstance(value, ZMGOSettlementConfig):
            self._settlement_config = value
        else:
            self._settlement_config = ZMGOSettlementConfig.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.basic_config:
            if hasattr(self.basic_config, 'to_alipay_dict'):
                params['basic_config'] = self.basic_config.to_alipay_dict()
            else:
                params['basic_config'] = self.basic_config
        if self.ext_config:
            if hasattr(self.ext_config, 'to_alipay_dict'):
                params['ext_config'] = self.ext_config.to_alipay_dict()
            else:
                params['ext_config'] = self.ext_config
        if self.obligation_config:
            if hasattr(self.obligation_config, 'to_alipay_dict'):
                params['obligation_config'] = self.obligation_config.to_alipay_dict()
            else:
                params['obligation_config'] = self.obligation_config
        if self.open_config:
            if hasattr(self.open_config, 'to_alipay_dict'):
                params['open_config'] = self.open_config.to_alipay_dict()
            else:
                params['open_config'] = self.open_config
        if self.quit_config:
            if hasattr(self.quit_config, 'to_alipay_dict'):
                params['quit_config'] = self.quit_config.to_alipay_dict()
            else:
                params['quit_config'] = self.quit_config
        if self.right_config:
            if hasattr(self.right_config, 'to_alipay_dict'):
                params['right_config'] = self.right_config.to_alipay_dict()
            else:
                params['right_config'] = self.right_config
        if self.settlement_config:
            if hasattr(self.settlement_config, 'to_alipay_dict'):
                params['settlement_config'] = self.settlement_config.to_alipay_dict()
            else:
                params['settlement_config'] = self.settlement_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantZmgoTemplateCreateModel()
        if 'basic_config' in d:
            o.basic_config = d['basic_config']
        if 'ext_config' in d:
            o.ext_config = d['ext_config']
        if 'obligation_config' in d:
            o.obligation_config = d['obligation_config']
        if 'open_config' in d:
            o.open_config = d['open_config']
        if 'quit_config' in d:
            o.quit_config = d['quit_config']
        if 'right_config' in d:
            o.right_config = d['right_config']
        if 'settlement_config' in d:
            o.settlement_config = d['settlement_config']
        return o


