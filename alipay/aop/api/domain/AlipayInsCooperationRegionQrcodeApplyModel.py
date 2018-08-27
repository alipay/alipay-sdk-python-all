#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsCooperationRegionQrcodeApplyModel(object):

    def __init__(self):
        self._agent_id = None
        self._agent_name = None
        self._agent_phone = None
        self._inst_id = None
        self._prod_code_list = None
        self._region_id = None
        self._region_name = None

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
    def prod_code_list(self):
        return self._prod_code_list

    @prod_code_list.setter
    def prod_code_list(self, value):
        if isinstance(value, list):
            self._prod_code_list = list()
            for i in value:
                self._prod_code_list.append(i)
    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self, value):
        self._region_id = value
    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, value):
        self._region_name = value


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
        if self.prod_code_list:
            if isinstance(self.prod_code_list, list):
                for i in range(0, len(self.prod_code_list)):
                    element = self.prod_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prod_code_list[i] = element.to_alipay_dict()
            if hasattr(self.prod_code_list, 'to_alipay_dict'):
                params['prod_code_list'] = self.prod_code_list.to_alipay_dict()
            else:
                params['prod_code_list'] = self.prod_code_list
        if self.region_id:
            if hasattr(self.region_id, 'to_alipay_dict'):
                params['region_id'] = self.region_id.to_alipay_dict()
            else:
                params['region_id'] = self.region_id
        if self.region_name:
            if hasattr(self.region_name, 'to_alipay_dict'):
                params['region_name'] = self.region_name.to_alipay_dict()
            else:
                params['region_name'] = self.region_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsCooperationRegionQrcodeApplyModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'agent_phone' in d:
            o.agent_phone = d['agent_phone']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'prod_code_list' in d:
            o.prod_code_list = d['prod_code_list']
        if 'region_id' in d:
            o.region_id = d['region_id']
        if 'region_name' in d:
            o.region_name = d['region_name']
        return o


