#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInsserviceprodContractCheckavailableModel(object):

    def __init__(self):
        self._ant_ser_contract_no = None

    @property
    def ant_ser_contract_no(self):
        return self._ant_ser_contract_no

    @ant_ser_contract_no.setter
    def ant_ser_contract_no(self, value):
        self._ant_ser_contract_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_contract_no:
            if hasattr(self.ant_ser_contract_no, 'to_alipay_dict'):
                params['ant_ser_contract_no'] = self.ant_ser_contract_no.to_alipay_dict()
            else:
                params['ant_ser_contract_no'] = self.ant_ser_contract_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInsserviceprodContractCheckavailableModel()
        if 'ant_ser_contract_no' in d:
            o.ant_ser_contract_no = d['ant_ser_contract_no']
        return o


