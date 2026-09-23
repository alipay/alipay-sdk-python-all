#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneFlowcardBindcardNotifyModel(object):

    def __init__(self):
        self._ant_ser_apply_no = None
        self._ant_ser_contract_no = None
        self._bind_card_time = None
        self._iccid = None
        self._sim_no = None

    @property
    def ant_ser_apply_no(self):
        return self._ant_ser_apply_no

    @ant_ser_apply_no.setter
    def ant_ser_apply_no(self, value):
        self._ant_ser_apply_no = value
    @property
    def ant_ser_contract_no(self):
        return self._ant_ser_contract_no

    @ant_ser_contract_no.setter
    def ant_ser_contract_no(self, value):
        self._ant_ser_contract_no = value
    @property
    def bind_card_time(self):
        return self._bind_card_time

    @bind_card_time.setter
    def bind_card_time(self, value):
        self._bind_card_time = value
    @property
    def iccid(self):
        return self._iccid

    @iccid.setter
    def iccid(self, value):
        self._iccid = value
    @property
    def sim_no(self):
        return self._sim_no

    @sim_no.setter
    def sim_no(self, value):
        self._sim_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_apply_no:
            if hasattr(self.ant_ser_apply_no, 'to_alipay_dict'):
                params['ant_ser_apply_no'] = self.ant_ser_apply_no.to_alipay_dict()
            else:
                params['ant_ser_apply_no'] = self.ant_ser_apply_no
        if self.ant_ser_contract_no:
            if hasattr(self.ant_ser_contract_no, 'to_alipay_dict'):
                params['ant_ser_contract_no'] = self.ant_ser_contract_no.to_alipay_dict()
            else:
                params['ant_ser_contract_no'] = self.ant_ser_contract_no
        if self.bind_card_time:
            if hasattr(self.bind_card_time, 'to_alipay_dict'):
                params['bind_card_time'] = self.bind_card_time.to_alipay_dict()
            else:
                params['bind_card_time'] = self.bind_card_time
        if self.iccid:
            if hasattr(self.iccid, 'to_alipay_dict'):
                params['iccid'] = self.iccid.to_alipay_dict()
            else:
                params['iccid'] = self.iccid
        if self.sim_no:
            if hasattr(self.sim_no, 'to_alipay_dict'):
                params['sim_no'] = self.sim_no.to_alipay_dict()
            else:
                params['sim_no'] = self.sim_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneFlowcardBindcardNotifyModel()
        if 'ant_ser_apply_no' in d:
            o.ant_ser_apply_no = d['ant_ser_apply_no']
        if 'ant_ser_contract_no' in d:
            o.ant_ser_contract_no = d['ant_ser_contract_no']
        if 'bind_card_time' in d:
            o.bind_card_time = d['bind_card_time']
        if 'iccid' in d:
            o.iccid = d['iccid']
        if 'sim_no' in d:
            o.sim_no = d['sim_no']
        return o


