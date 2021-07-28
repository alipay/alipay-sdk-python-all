#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FixCooperationDTO(object):

    def __init__(self):
        self._conclusion = None
        self._cooperation_id = None
        self._deal_time = None
        self._description = None
        self._duty_owner_name = None
        self._gmt_create = None
        self._owner_name = None
        self._result = None

    @property
    def conclusion(self):
        return self._conclusion

    @conclusion.setter
    def conclusion(self, value):
        self._conclusion = value
    @property
    def cooperation_id(self):
        return self._cooperation_id

    @cooperation_id.setter
    def cooperation_id(self, value):
        self._cooperation_id = value
    @property
    def deal_time(self):
        return self._deal_time

    @deal_time.setter
    def deal_time(self, value):
        self._deal_time = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def duty_owner_name(self):
        return self._duty_owner_name

    @duty_owner_name.setter
    def duty_owner_name(self, value):
        self._duty_owner_name = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.conclusion:
            if hasattr(self.conclusion, 'to_alipay_dict'):
                params['conclusion'] = self.conclusion.to_alipay_dict()
            else:
                params['conclusion'] = self.conclusion
        if self.cooperation_id:
            if hasattr(self.cooperation_id, 'to_alipay_dict'):
                params['cooperation_id'] = self.cooperation_id.to_alipay_dict()
            else:
                params['cooperation_id'] = self.cooperation_id
        if self.deal_time:
            if hasattr(self.deal_time, 'to_alipay_dict'):
                params['deal_time'] = self.deal_time.to_alipay_dict()
            else:
                params['deal_time'] = self.deal_time
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.duty_owner_name:
            if hasattr(self.duty_owner_name, 'to_alipay_dict'):
                params['duty_owner_name'] = self.duty_owner_name.to_alipay_dict()
            else:
                params['duty_owner_name'] = self.duty_owner_name
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FixCooperationDTO()
        if 'conclusion' in d:
            o.conclusion = d['conclusion']
        if 'cooperation_id' in d:
            o.cooperation_id = d['cooperation_id']
        if 'deal_time' in d:
            o.deal_time = d['deal_time']
        if 'description' in d:
            o.description = d['description']
        if 'duty_owner_name' in d:
            o.duty_owner_name = d['duty_owner_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'result' in d:
            o.result = d['result']
        return o


