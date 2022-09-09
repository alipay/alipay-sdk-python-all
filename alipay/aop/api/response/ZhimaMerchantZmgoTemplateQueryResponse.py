#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZMGOBasicConfig import ZMGOBasicConfig
from alipay.aop.api.domain.ZMGOExtConfig import ZMGOExtConfig
from alipay.aop.api.domain.ZMGOObligationConfig import ZMGOObligationConfig
from alipay.aop.api.domain.ZMGOOpenConfig import ZMGOOpenConfig
from alipay.aop.api.domain.ZMGOQuitConfig import ZMGOQuitConfig
from alipay.aop.api.domain.ZMGORightConfig import ZMGORightConfig
from alipay.aop.api.domain.ZMGOSettlementConfig import ZMGOSettlementConfig


class ZhimaMerchantZmgoTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantZmgoTemplateQueryResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantZmgoTemplateQueryResponse, self).parse_response_content(response_content)
        if 'basic_config' in response:
            self.basic_config = response['basic_config']
        if 'ext_config' in response:
            self.ext_config = response['ext_config']
        if 'obligation_config' in response:
            self.obligation_config = response['obligation_config']
        if 'open_config' in response:
            self.open_config = response['open_config']
        if 'quit_config' in response:
            self.quit_config = response['quit_config']
        if 'right_config' in response:
            self.right_config = response['right_config']
        if 'settlement_config' in response:
            self.settlement_config = response['settlement_config']
