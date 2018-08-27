#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsCooperationProductQrcodeApplyModel(object):

    def __init__(self):
        self._agent_id = None
        self._agent_name = None
        self._agent_phone = None
        self._inst_id = None
        self._prod_code = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def agent_phone(self):
        return self._agent_phone

    @agent_phone.setter
    def agent_phone(self, value):
        self._agent_phone = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.agent_phone:
            if hasattr(self.agent_phone, 'to_alipay_dict'):
                params['agent_phone'] = self.agent_phone.to_alipay_dict()
            else:
                params['agent_phone'] = self.agent_phone
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsCooperationProductQrcodeApplyModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'agent_phone' in d:
            o.agent_phone = d['agent_phone']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        return o


