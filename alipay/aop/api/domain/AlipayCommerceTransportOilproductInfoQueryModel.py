#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportOilproductInfoQueryModel(object):

    def __init__(self):
        self._agent = None
        self._ext_info = None
        self._shop_id = None

    @property
    def agent(self):
        return self._agent

    @agent.setter
    def agent(self, value):
        self._agent = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent:
            if hasattr(self.agent, 'to_alipay_dict'):
                params['agent'] = self.agent.to_alipay_dict()
            else:
                params['agent'] = self.agent
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportOilproductInfoQueryModel()
        if 'agent' in d:
            o.agent = d['agent']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


